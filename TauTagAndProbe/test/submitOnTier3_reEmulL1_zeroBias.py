import os
import json
from subprocess import Popen, PIPE

#isMC = True
isMC = False

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

njobs = 200
filedir="/home/llr/cms/motta/Run3preparation/CMSSW_11_0_2/src/TauTagAndProbe/TauTagAndProbe/inputFiles"

if not isMC:
    filelist = open(filedir+"/EphemeralZeroBias_2018D_Run323775.txt")
    folder = "/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_2018D_Run323775"
else:
    filelist = open(filedir+"/VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8__Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v1__GEN-SIM-RAW.txt")
    folder = "/data_CMS/cms/motta/Run3preparation/2022_01_15_optimizationV3_calibThr1p7/Run3_MC_VBFHToTauTau_M125_RAW_2022_01_15"


JSONfile = "/home/llr/cms/davignon/json_DCSONLY.txt"
#JSONfile = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt"

###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

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
        #cmsRun = "cmsRun reEmulL1_ZeroBias.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
    else:
        cmsRun = "cmsRun reEmulL1_MC_L1Only.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName

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
#    command = ('/home/llr/cms/motta/t3submit -short -q cms \'' + outJobName +"\'")
    print command
    os.system (command)
