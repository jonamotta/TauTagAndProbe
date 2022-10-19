import os
import json
from subprocess import Popen, PIPE

# isMC = True
isMC = False

isNU = False

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def splitInBlocks (l, n):
    """split the list l in n blocks of equal size"""
    k = len(l) / n
    r = len(l) % n

    i = 0
    blocks = []
    while i < len(l):
        if len(blocks)<r:
            blocks.append(l[i:i+k+1])
            i += k+1
        else:
            blocks.append(l[i:i+k])
            i += k

    return blocks

###########

njobs = 1000 # 150
filedir="/home/llr/cms/motta/Run3preparation/CMSSW_12_4_0/src/TauTagAndProbe/TauTagAndProbe/inputFiles"

list_filelists = []
list_folders = []
list_njobs = []

if not isMC:
    ## 2018 data
    # list_filelists.append(open(filedir+"/Run323775__SingleMuon__Run2018D-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/Run323775__SingleMuon__Run2018D-v1__RAW")
    # list_njobs.append(50)

    ## ZerioBias 13TeV
    # list_filelists.append(open(filedir+"/EphemeralZeroBias_2018D_Run323755.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_2018D_Run323755_reEmuTPs")
    # list_filelists.append(open(filedir+"/EphemeralZeroBias_2018D_Run323775.txt"))
    
    ## ZerioBias 900GeV
    # list_filelists.append(open(filedir+"/ZeroBias1_Run2022A_Runs2bunches0p015lumi.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022A_Runs2bunches0p015lumi_reEmuTPs")
    # list_njobs.append(300)
    # list_filelists.append(open(filedir+"/ZeroBias1_Run2022A_Runs2bunches0p03lumi.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022A_Runs2bunches0p03lumi_reEmuTPs")
    # list_njobs.append(700)
    # list_filelists.append(open(filedir+"/ZeroBias1_Run2022A_Runs3bunches0p04lumi.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022A_Runs3bunches0p04lumi_reEmuTPs")
    # list_njobs.append(100)
    
    ## ZerioBias 13.6TeV
    # list_filelists.append(open(filedir+"/ZeroBias1__Run2022B-v1__Run355414__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355414_RAW")
    # list_njobs.append(300)

    # list_filelists.append(open(filedir+"/ZeroBias1__Run2022B-v1__Run355417__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355417_RAW")
    # list_njobs.append(300)

    # list_filelists.append(open(filedir+"/ZeroBias1__Run2022B-v1__Run355418__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355418_RAW")
    # list_njobs.append(300)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022B-v1__Run355769__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022B_Run355769_RAW_reEmuTPs")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run355865__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run355865_RAW")
    # list_njobs.append(75)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run355872__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run355872_RAW")
    # list_njobs.append(2)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run355913__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run355913_RAW")
    # list_njobs.append(75)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run356375__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run356375_RAW")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run356378__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run356378_RAW")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Run356381__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Run356381_RAW")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Fill8088-8094-8102__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Fill8088-8094-8102_RAW_reEmuTPs")
    # list_njobs.append(75)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022C-v1__Fill8112-8113-8115__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022C_Fill8112-8113-8115_RAW_reEmuTPs")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022D-v1__Run357802__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022D_Run357802__RAW")
    # list_njobs.append(8)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022Cpre-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022Cpre__RAW")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022Cpost-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022Cpost__RAW")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022D-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022D__RAW")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022E-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022E__RAW")
    # list_njobs.append(100)

    # list_filelists.append(open(filedir+"/ZeroBias__Run2022F-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/ZeroBias_Run2022F__RAW")
    # list_njobs.append(150)

    list_filelists.append(open(filedir+"/test.txt"))
    list_folders.append("/data_CMS/cms/motta/Run3preparation/test")
    list_njobs.append(10)


    ## SingleMuon 13.6TeV
    # list_filelists.append(open(filedir+"/SingleMuon__Run2022B-v1__Run355769__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022B_Run355769_RAW")
    # list_njobs.append(300)

    # list_filelists.append(open(filedir+"/SingleMuon__Run2022C-v1__Run355865__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run355865_RAW_reEmuTPs")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/SingleMuon__Run2022C-v1__Run355913__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run355913_RAW_reEmuTPs")
    # list_njobs.append(50)

    # list_filelists.append(open(filedir+"/SingleMuon__Run2022C-v1__Run356375__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356375_RAW_reEmuTPs")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/SingleMuon__Run2022C-v1__Run356378__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356378_RAW_reEmuTPs")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/SingleMuon__Run2022C-v1__Run356381__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356381_RAW_reEmuTPs")
    # list_njobs.append(25)

    # list_filelists.append(open(filedir+"/Muon__Run2022C-v1__RAW__fromRun356709toRun357271.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon_Run2022C_fromRun356709toRun357271_RAW_reEmuTPs")
    # list_njobs.append(350)

    # list_filelists.append(open(filedir+"/Muon__Run2022C-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022C-v1__RAW__GoldenJSON")
    # list_njobs.append(350)

    # list_filelists.append(open(filedir+"/Muon__Run2022D-v1__RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022D-v1__RAW__GoldenJSON")
    # list_njobs.append(350)

    # exit()

else:
    # 120X signal Run3 MC
    # list_filelists.append(open(filedir+"/VBFHToTauTau_M125_TuneCP5_14TeV-powheg-pythia8__Run3Summer21DRPremix-120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/2022_06_13_optimizationV13/Run3_MC_VBFHToTauTau_M125_RAW_2022_06_13")
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/2022_06_13_optimizationV13_ReOptReEmu/Run3_MC_VBFHToTauTau_M125_ReOptReEmu20kHz_2022_06_13")

    # 112X Neutrino
    # list_filelists.append(open(filedir+"/SingleNeutrino_Pt-2To20-gun__Run3Winter21DRMiniAOD-FlatPU30to80FEVT_SNB_112X_mcRun3_2021_realistic_v16-v2__GEN-SIM-DIGI-RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/2022_06_13_optimizationV13/Run3_MC_SingleNeutrinoGun_RAW112X_2022_06_13")
    # isNU = True

    # 120X Neutrino
    # list_filelists.append(open(filedir+"/SingleNeutrino_Pt-2To20-gun__Run3Summer21DRPremix-SNB_120X_mcRun3_2021_realistic_v6-v2__GEN-SIM-DIGI-RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/2022_06_13_optimizationV13/Run3_MC_SingleNeutrinoGun_RAW120X_2022_06_13")
    # isNU = True

    # 122X Neutrino
    # list_filelists.append(open(filedir+"/SingleNeutrino_Pt-2To20-gun__Run3Winter22DR-L1TPU0to99FEVT_SNB_122X_mcRun3_2021_realistic_v9-v2__GEN-SIM-DIGI-RAW.txt"))
    # list_folders.append("/data_CMS/cms/motta/Run3preparation/2022_06_13_optimizationV13/Run3_MC_SingleNeutrinoGun_RAW122X_2022_06_13")
    # isNU = True

    exit()

# JSONfile = "/home/llr/cms/davignon/json_DCSONLY.txt"
# JSONfile = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt"
# JSONfile = "./Cert_Collisions2022_357079_357900_Golden.txt"

###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

for i in range(len(list_folders)):
    filelist = list_filelists[i]
    folder = list_folders[i]
    njobs = list_njobs[i]

    os.system('mkdir -p ' + folder)
    files = [f.strip() for f in filelist]
    print "Input has" , len(files) , "files" 
    if njobs > len(files) : njobs = len(files)
    filelist.close()

    fileblocks = splitInBlocks (files, njobs)

    from das_client import get_data

    for idx, block in enumerate(fileblocks):
        #print idx, block

        outRootName = folder + '/Ntuple_' + str(idx) + '.root'
        outJobName  = folder + '/job_' + str(idx) + '.sh'
        outListName = folder + "/filelist_" + str(idx) + ".txt"
        outLogName  = folder + "/log_" + str(idx) + ".txt"

        jobfilelist = open(outListName, 'w')
        for f in block: jobfilelist.write(f+"\n")
        jobfilelist.close()

        if not isMC:
            cmsRun = "cmsRun reEmulL1_ZeroBias.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
            # cmsRun = "cmsRun reEmulL1_ZeroBias.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
        else:
            if not isNU: cmsRun = "cmsRun reEmulL1_MC_L1Only.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " isNU=0 >& " + outLogName
            else:        cmsRun = "cmsRun reEmulL1_MC_L1Only.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " isNU=1 >& " + outLogName
        
        skimjob = open (outJobName, 'w')
        skimjob.write ('#!/bin/bash\n')
        skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
        skimjob.write ('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
        skimjob.write ('cd %s\n' % os.getcwd())
        skimjob.write ('export SCRAM_ARCH=slc6_amd64_gcc472\n')
        skimjob.write ('eval `scram r -sh`\n')
        skimjob.write ('cd %s\n'%os.getcwd())
        skimjob.write (cmsRun+'\n')
        skimjob.close ()

        os.system ('chmod u+rwx ' + outJobName)
        # command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
        command = ('/home/llr/cms/motta/t3submit -short \'' + outJobName +"\'")
        print command
        os.system (command)
        # break
