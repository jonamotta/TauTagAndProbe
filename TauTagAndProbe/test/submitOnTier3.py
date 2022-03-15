import os

isMC = True
#isMC = False

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

njobs = 150
filedir="/home/llr/cms/motta/Run3preparation/CMSSW_12_3_0_pre1/src/TauTagAndProbe/TauTagAndProbe/inputFiles"

# 100X signal RunII MC
filelist = open(filedir+"/VBFHToTauTau_M125_13TeV_powheg_pythia8__RunIISpring18MiniAOD-NZSPU28to70_100X_upgrade2018_realistic_v10-v1_MINIAODSIM.txt")
folder = "/data_CMS/cms/motta/Run3preparation/2022_02_28_optimizationV9/Run2_MC_VBFHToTauTau_M125_MINIAOD100X_2022_02_28"

# 102X signal RunII MC
#filelist = open(filedir+"/VBFHToTauTau_M125_13TeV_powheg_pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1__MINIAODSIM.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/2022_02_28_optimizationV9/Run2_MC_VBFHToTauTau_M125_MINIAOD102X_2022_02_28"

# 120X signal Run3 MC
#filelist = open(filedir+"/VBFHToTauTau_M125_TuneCP5_14TeV-powheg-pythia8__Run3Summer21MiniAOD-120X_mcRun3_2021_realistic_v5-v2__MINIAODSIM.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/2022_02_28_optimizationV9/Run3_MC_VBFHToTauTau_M125_MINIAOD_2022_02_28"

# EphemeralZeroBias data
#filelist = open(filedir+"/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323755.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323755"
#filelist = open(filedir+"/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323775.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323775"

# SingleMuon data
#filelist = open(filedir+"/Run323775__Run2018D__SingleMuon__MINIAOD__UL2018_MiniAODv2-v3.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_2018D_Run323775_MINIAOD_UL2018v2"


#JSONfile = "/home/llr/cms/davignon/json_NoL1T.txt"
#JSONfile = "/home/llr/cms/davignon/json_DCSONLY.txt"
#/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt

###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

os.system('mkdir -p ' + folder)
files = [f.strip() for f in filelist]
print("Input has" , len(files) , "files")
if njobs > len(files) : njobs = len(files)
filelist.close()

fileblocks = splitInBlocks (files, njobs)

for idx, block in enumerate(fileblocks):
    outRootName = folder + '/Ntuple_' + str(idx) + '.root'
    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outListName = folder + "/filelist_" + str(idx) + ".txt"
    outLogName  = folder + "/log_" + str(idx) + ".txt"

    jobfilelist = open(outListName, 'w')
    for f in block: jobfilelist.write(f+"\n")
    jobfilelist.close()

    if not isMC:
        cmsRun = "cmsRun test.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
        #cmsRun = "cmsRun test.py maxEvents=200 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
    else:
        cmsRun = "cmsRun test_noTagAndProbe.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName        

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
    command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
    #command = ('/home/llr/cms/motta/t3submit -short -q cms \'' + outJobName +"\'")
    print(command)
    os.system (command)
