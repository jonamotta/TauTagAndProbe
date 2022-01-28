import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

isMC = False

#process = cms.Process("ZeroBias",eras.Run2_2016)
#process = cms.Process("ZeroBias",eras.Run2_2017)
process = cms.Process("ZeroBias",eras.Run2_2018)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#all above present before
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
#process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
#process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')

#process.load('Configuration.StandardSequences.Services_cff')
#process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
#process.load('FWCore.MessageService.MessageLogger_cfi')
#process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
#process.load('Configuration.StandardSequences.MagneticField_cff')
#process.load('Configuration.StandardSequences.RawToDigi_cff')
#process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')



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

if not isMC: # will use 80X
    from Configuration.AlCa.autoCond import autoCond
    #process.GlobalTag.globaltag = '110X_dataRun2_v12'
    process.GlobalTag.globaltag = '120X_mcRun3_2021_realistic_v6'
    process.load('TauTagAndProbe.TauTagAndProbe.zeroBias_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            # dummy for creation
            '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/02506E54-CE47-A649-9F80-117E978DC69E.root'
        ),
    )

else: # will use 80X
    from Configuration.AlCa.autoCond import autoCond
    #process.GlobalTag.globaltag = '110X_dataRun2_v12'
    process.GlobalTag.globaltag = '120X_mcRun3_2021_realistic_v6'
    process.load('TauTagAndProbe.TauTagAndProbe.zeroBias_cff')
    process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            # dummy for creation
            '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/02506E54-CE47-A649-9F80-117E978DC69E.root'
        ),
    )

process.schedule = cms.Schedule()

## L1 emulation stuff

if not isMC:
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 
    process = L1TReEmulFromRAW(process)
else:
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW
    process = L1TReEmulMCFromRAW(process) 
    from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 
    process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)
    #from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimTP
    #process = L1TReEmulFromRAWsimTP(process)


#process.load("L1Trigger.L1TCalorimeter.caloParams_2021_v0_1_cfi") # latest in CMSSW_11_2_0
#process.load("L1Trigger.L1TCalorimeter.caloParams_2018_v1_4_cfi") # latest in CMSSW_11_0_2
process.load("L1Trigger.L1TCalorimeter.caloParams_2021_v0_2_cfi") # latest in CMSSW_12_0_2

#### handling of cms line options for tier3 submission
#### the following are dummy defaults, so that one can normally use the config changing file list by hand etc.



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

process.load('EventFilter.L1TRawToDigi.caloStage2Digis_cfi')
process.caloStage2Digis.InputLabel = cms.InputTag('rawDataCollector')

process.p = cms.Path (
    process.RawToDigi +
    process.caloStage2Digis +
    process.L1TReEmul +
    process.NtupleZeroBiasSeq
)
process.schedule = cms.Schedule(process.p) # do my sequence pls

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
