import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

isMC = True

process = cms.Process("ZeroBias",eras.Run2_2018)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

options = VarParsing.VarParsing ('analysis')

options.register ('skipEvents',
                  -1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Number of events to skip")
options.register ('JSONfile',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "JSON file (empty for no JSON)")
options.outputFile = 'NTuple_ZeroBias.root'
options.inputFiles = []
options.maxEvents  = -999

options.parseArguments()

import FWCore.Utilities.FileUtils as FileUtils

if not isMC:
    from Configuration.AlCa.autoCond import autoCond
    process.GlobalTag.globaltag = '120X_mcRun3_2021_realistic_v6'
    process.load('TauTagAndProbe.TauTagAndProbe.zeroBias_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            # dummy for creation
            '/store/mc/Run3Winter20DRPremixMiniAOD/VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8/GEN-SIM-RAW/110X_mcRun3_2021_realistic_v6-v1/20000/2D4F0AC7-86ED-1F45-8E14-58D72D98667C.root'
        ),
    )

else: # will use 80X
    from Configuration.AlCa.autoCond import autoCond
    process.GlobalTag.globaltag = '100X_upgrade2018_realistic_v10'
    #process.GlobalTag.globaltag = '102X_upgrade2018_realistic_v15'
    #process.GlobalTag.globaltag = '120X_mcRun3_2021_realistic_v6'
    #process.GlobalTag.globaltag = '112X_mcRun3_2021_realistic_v16'
    process.load('TauTagAndProbe.TauTagAndProbe.zeroBias_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            # dummy for creation
            '/store/mc/Run3Winter20DRPremixMiniAOD/VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8/GEN-SIM-RAW/110X_mcRun3_2021_realistic_v6-v1/20000/2D4F0AC7-86ED-1F45-8E14-58D72D98667C.root'
        ),
    )

process.schedule = cms.Schedule()

if options.JSONfile:
    print("Using JSON: " , options.JSONfile)
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

if options.maxEvents >= -1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)
if options.skipEvents >= 0:
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.p = cms.Path (
    process.NtupleZeroBiasSeq
)
process.schedule = cms.Schedule(process.p) # do my sequence pls

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
