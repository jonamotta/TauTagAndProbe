import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

isMC = True

process = cms.Process("ZeroBias",eras.Run3)

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
options.register ('isNU',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "is it SingleNeutrino Run3MC?")
options.outputFile = 'NTuple_ZeroBias.root'
options.inputFiles = []
options.maxEvents  = -999

options.parseArguments()

import FWCore.Utilities.FileUtils as FileUtils

from Configuration.AlCa.autoCond import autoCond
if options.isNU:
    process.GlobalTag.globaltag = '123X_mcRun3_2021_realistic_v5'
    process.load('TauTagAndProbe.TauTagAndProbe.Run3nuMC_cff')
else:
    process.GlobalTag.globaltag = '123X_mcRun3_2021_realistic_v5'
    process.load('TauTagAndProbe.TauTagAndProbe.zeroBias_cff')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # dummy for creation
        '/store/mc/Run3Winter20DRPremixMiniAOD/VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8/GEN-SIM-RAW/110X_mcRun3_2021_realistic_v6-v1/20000/2D4F0AC7-86ED-1F45-8E14-58D72D98667C.root'
    ),
)

process.schedule = cms.Schedule()

## L1 emulation stuff

if not isMC:
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 
    process = L1TReEmulFromRAW(process)
else:
    ## re-emulate starting from RAW information (here we do not re-emulate also the TPs)
    #from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW
    #process = L1TReEmulMCFromRAW(process)
    
    ## re-emulate starting from TPs (here we re-emulate also the TPs)
    from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAWSimHcalTP
    process = L1TReEmulMCFromRAWSimHcalTP(process)

    #from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFrom90xRAWSimHcalTP
    #process = L1TReEmulMCFrom90xRAWSimHcalTP(process)

    #4 lines below were here before
    #from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimTP
    #process = L1TReEmulFromRAWsimTP(process)
    #from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 
    #process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)


#process.load("L1Trigger.L1TCalorimeter.caloParams_2021_v0_1_cfi") # latest in CMSSW_11_2_0
#process.load("L1Trigger.L1TCalorimeter.caloParams_2018_v1_4_cfi") # latest in CMSSW_11_0_2
#process.load("L1Trigger.L1TCalorimeter.caloParams_2021_v0_2_cfi") # latest in CMSSW_12_0_2
#process.load("L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi") # latest in CMSSW_12_3_0_pre1
process.load("L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_reOpt14kHz_cfi") # reOptimized LUTs for 14kHz rate
#process.load("L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_reOpt16kHz_cfi") # reOptimized LUTs for 16kHz rate
#process.load("L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_reOpt18kHz_cfi") # reOptimized LUTs for 18kHz rate
#process.load("L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_reOpt20kHz_cfi") # reOptimized LUTs for 20kHz rate

############################
# PFA1' Filter
# --> HCAL pu mitigation

# process.load("SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff")

# process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHB = cms.bool(True)
# process.simHcalTriggerPrimitiveDigis.overrideDBweightsAndFilterHE = cms.bool(True)

# process.HcalTPGCoderULUT.overrideDBweightsAndFilterHB = cms.bool(True)
# process.HcalTPGCoderULUT.overrideDBweightsAndFilterHE = cms.bool(True)

# process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHBQIE11 = 1
# process.simHcalTriggerPrimitiveDigis.numberOfFilterPresamplesHEQIE11 = 1
# process.simHcalTriggerPrimitiveDigis.weightsQIE11 = {
#     "ieta1" :  [-0.47, 1.0],
#     "ieta2" :  [-0.47, 1.0],
#     "ieta3" :  [-0.47, 1.0],
#     "ieta4" :  [-0.47, 1.0],
#     "ieta5" :  [-0.47, 1.0],
#     "ieta6" :  [-0.47, 1.0],
#     "ieta7" :  [-0.47, 1.0],
#     "ieta8" :  [-0.47, 1.0],
#     "ieta9" :  [-0.47, 1.0],
#     "ieta10" : [-0.47, 1.0],
#     "ieta11" : [-0.47, 1.0],
#     "ieta12" : [-0.47, 1.0],
#     "ieta13" : [-0.47, 1.0],
#     "ieta14" : [-0.47, 1.0],
#     "ieta15" : [-0.47, 1.0],
#     "ieta16" : [-0.47, 1.0],
#     "ieta17" : [-0.47, 1.0],
#     "ieta18" : [-0.47, 1.0],
#     "ieta19" : [-0.47, 1.0],
#     "ieta20" : [-0.47, 1.0],
#     "ieta21" : [-0.43, 1.0],
#     "ieta22" : [-0.43, 1.0],
#     "ieta23" : [-0.43, 1.0],
#     "ieta24" : [-0.43, 1.0],
#     "ieta25" : [-0.43, 1.0],
#     "ieta26" : [-0.43, 1.0],
#     "ieta27" : [-0.43, 1.0],
#     "ieta28" : [-0.43, 1.0]
# }

# process.HcalTPGCoderULUT.contain1TSHB = True
# process.HcalTPGCoderULUT.contain1TSHE = True

############################




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
