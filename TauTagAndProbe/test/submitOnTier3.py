import os

# isMC = True
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

njobs = 2600
filedir="/home/llr/cms/motta/Run3preparation/CMSSW_13_0_0_pre2/src/TauTagAndProbe/TauTagAndProbe/inputFiles"

list_filelists = []
list_folders = []
list_njobs = []
list_JSON = []

# 100X signal RunII MC
#filelist = open(filedir+"/VBFHToTauTau_M125_13TeV_powheg_pythia8__RunIISpring18MiniAOD-NZSPU28to70_100X_upgrade2018_realistic_v10-v1_MINIAODSIM.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/2022_06_10_optimizationV12/Run2_MC_VBFHToTauTau_M125_MINIAOD100X_2022_06_10"

# 102X signal RunII MC
# filelist = open(filedir+"/VBFHToTauTau_M125_13TeV_powheg_pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v1__MINIAODSIM.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/2022_06_10_optimizationV12/Run2_MC_VBFHToTauTau_M125_MINIAOD102X_2022_06_10"

# 120X signal Run3 MC
# filelist = open(filedir+"/VBFHToTauTau_M125_TuneCP5_14TeV-powheg-pythia8__Run3Summer21MiniAOD-120X_mcRun3_2021_realistic_v5-v2__MINIAODSIM.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/2022_06_10_optimizationV12/Run3_MC_VBFHToTauTau_M125_MINIAOD_2022_06_10"

# ZeroBias 900GeV data
# filelist = open(filedir+"/ZeroBias1__Run2022A-PromptReco-v1__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/ZeroBias1__Run2022A-PromptReco-v1__MINIAOD"

## ZerioBias 13TeV
#filelist = open(filedir+"/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323755.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323755"
#filelist = open(filedir+"/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323775.txt")
#folder = "/data_CMS/cms/motta/Run3preparation/EphemeralZeroBias_PromptRecoMINIAOD_2018D_Run323775"


## ZerioBias 13.6TeV
# filelist = open(filedir+"/ZeroBias1__Run2022B-PromptReco-v1__Run355414__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355414_MINIAOD"

# filelist = open(filedir+"/ZeroBias1__Run2022B-PromptReco-v1__Run355417__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355417_MINIAOD"

# filelist = open(filedir+"/ZeroBias1__Run2022B-PromptReco-v1__Run355418__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/ZeroBias1_Run2022B_Run355418_MINIAOD"


## SingleMuon 13.6TeV
# filelist = open(filedir+"/SingleMuon__Run2022B-PromptReco-v1__Run355414__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022B_Run355414_MINIAOD"

# filelist = open(filedir+"/SingleMuon__Run2022B-PromptReco-v1__Run355417__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022B_Run355417_MINIAOD"

# filelist = open(filedir+"/SingleMuon__Run2022B-PromptReco-v1__Run355418__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022B_Run355418_MINIAOD"

# filelist = open(filedir+"/SingleMuon__Run2022B-PromptReco-v1__Run355769__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022B_Run355769_MINIAOD"

# filelist = open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run355865__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run355865_MINIAOD"
# njobs=1

# filelist = open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run355872__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run355872_MINIAOD"
# njobs=1

# filelist = open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run355913__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run355913_MINIAOD"
# njobs=1

# list_filelists.append(open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run356375__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356375_MINIAOD")
# list_njobs.append(50)

# list_filelists.append(open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run356378__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356378_MINIAOD")
# list_njobs.append(50)

# list_filelists.append(open(filedir+"/SingleMuon__Run2022C-PromptReco-v1__Run356381__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_Run356381_MINIAOD")
# list_njobs.append(50)



# SingleMuon data 2018
# filelist = open(filedir+"/Run323775__Run2018D__SingleMuon__UL2018_MiniAODv2-v3__MINIAOD.txt")
# folder = "/data_CMS/cms/motta/Run3preparation/Run323775__SingleMuon__Run2018D-v1__MINIAOD"

# list_filelists.append(open(filedir+"/SingleMuon__Run2018D-PromptReco-v2__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon__Run2018D-PromptReco-v2__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
# list_njobs.append(300)
# Run2 = True; Run3 = False

# list_filelists.append(open(filedir+"/SingleMuon__Run2018D-UL2018_MiniAODv2-v3__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon__Run2018D-UL2018_MiniAODv2-v3__MINIAOD__GoldenJSON__WMassCutFalse__ZMassCutFalse")
# list_njobs.append(500)
# Run2 = True; Run3 = False



# extended datasets
# list_filelists.append(open(filedir+"/SingleMuon__Run2018A-UL2018_MiniAODv2-v3__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2018A_MINIAOD")
# list_njobs.append(100)

# list_filelists.append(open(filedir+"/SingleMuon__Run2022B-C-PromptReco-v1__MINIAOD__fromRun355100toRun356386.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/SingleMuon_Run2022C_fromRun355100toRun356386_MINIAOD")
# list_njobs.append(50)

# list_filelists.append(open(filedir+"/Muon__Run2022C-PromptReco-v1__MINIAOD__fromRun356709toRun357271.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon_Run2022C_fromRun356709toRun357271_MINIAOD")
# list_njobs.append(1000)

# list_filelists.append(open(filedir+"/test.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/test")
# list_njobs.append(2)

# list_filelists.append(open(filedir+"/Muon__Run2022C-PromptReco-v1__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022Cpre-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
# list_njobs.append(250)
# list_JSON.append("./Cert_Collisions2022_eraC_355862_357482_Golden_pre.json")
# Run2 = False; Run3 = True

# list_filelists.append(open(filedir+"/Muon__Run2022C-PromptReco-v1__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022Cpost-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
# list_njobs.append(250)
# list_JSON.append("./Cert_Collisions2022_eraC_355862_357482_Golden_post.json")
# Run2 = False; Run3 = True

# list_filelists.append(open(filedir+"/Muon__Run2022D-PromptReco-v1-2__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022D-PromptReco-v1-2__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
# list_njobs.append(150)
# list_JSON.append("./Cert_Collisions2022_eraD_357538_357900_Golden.json")
# Run2 = False; Run3 = True

# list_filelists.append(open(filedir+"/Muon__Run2022E-PromptReco-v1__MINIAOD.txt"))
# list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022E-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
# list_njobs.append(250)
# list_JSON.append("./Cert_Collisions2022_eraE_359022_360331_Golden.json")
# Run2 = False; Run3 = True

list_filelists.append(open(filedir+"/Muon__Run2022F-PromptReco-v1__MINIAOD.txt"))
list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022F-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
list_njobs.append(500)
list_JSON.append("./Cert_Collisions2022_eraF_360390_362167_Golden.json")
Run2 = False; Run3 = True

list_filelists.append(open(filedir+"/Muon__Run2022G-PromptReco-v1__MINIAOD.txt"))
list_folders.append("/data_CMS/cms/motta/Run3preparation/Muon__Run2022G-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue")
list_njobs.append(100)
list_JSON.append("./Cert_Collisions2022_eraG_362433_362760_Golden.json")
Run2 = False; Run3 = True

###########


os.system ('source /opt/exp_soft/cms/t3/t3setup')

for i in range(len(list_folders)):
    filelist = list_filelists[i]
    folder = list_folders[i]
    njobs = list_njobs[i]
    JSONfile = list_JSON[i]
    if Run2: JSONfile = "./Cert_Collisions2018_323414-325175_Golden.txt" # RUN2 GOLDEN JSON
    
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
            # cmsRun = "cmsRun test.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
            if Run3: cmsRun = "cmsRun testRun3.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
            if Run2: cmsRun = "cmsRun testRun2.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
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
        # command = ('/home/llr/cms/motta/t3submit -long \'' + outJobName +"\'")
        command = ('/home/llr/cms/motta/t3submit -short \'' + outJobName +"\'")
        print(command)
        os.system (command)
        # break