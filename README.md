# TauTagAndProbe
Set of tools to evaluate tau trigger performance on T&amp;P

## Install instructions
```bash
cmsrel CMSSW_12_4_0
cd CMSSW_12_4_0/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline l1t-integration-CMSSW_12_4_0
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v129.0-CMSSW_12_4_0
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

git clone git@github.com:jonamotta/TauTagAndProbe.git -b CMSSW_12_4_0-l1t-integration-v125.0 # package for the production of the starting NTuples

git cms-checkdeps -A -a

scram b -j 12
```

L1T emulation relevant GlobalTags in CMSSW_12_4_0 are:
* for run2 data reprocessing `124X_dataRun2_v2`
* for run2 mc `123X_mcRun2_asymptotic_v1` (to be updated)
* for run3 mc `124X_mcRun3_2022_realistic_v6`
* for run3 (CRUZET) data `124X_dataRun3_v2`
* for run3 (900GeV COLLISION) data `124X_dataRun3_v4`


## Tool utilization
To do the optimization two things are needed:
* L1 objects (sometimes re-emulated) that are extracted from the RAW tier (in principle, non-re-emulated L1 objects can also be extracted from MiniAOD, but for consistency we never do that)
* Offline objects that are extracted from the AOD or MiniAOD tier

### Production of the input objects
To produce the input NTuples to the optimization the `TauTagAndProbe` package is used. The useful scripts for this are mainly in the `test` subfolder.

Jobs on ***RAW*** are submitted using `submitOnTier3_reEmulL1_zeroBias.py` which in turn launches `reEmulL1_X.py`
Before launching this you need to fix
* the Global Tag
* the configuration of the L1Calorimeter (`process.load("L1Trigger.L1TCalorimeter.caloStage2Params_20XX_vX_X_XXX_cfi")`)

Jobs on ***MiniAOD*** are submitted using `submitOnTier3.py` which in turn launches `test_noTagAndProbe.py`
Before launching this you need to fix
* the Global Tag

Jobs on ***Data*** are submitted using `submitOnTier3_reEmulL1_zeroBias.py` which in turn launches `reEmulL1_X.py`.
Before launching this you need to fix
* the `isMC` flag
* the input folder and file list
The datasets that have to be used are among the ones listed here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/TriggerStudiesChangesInDataTaking2018

For Monte Carlo (MC), we implemented a truth matching rather than a Tag & Probe technique which would dramatically and artificially decrease the available statistics.

After having produced the input object `hadd` all the files.

### Optimization
The optimization is run in several sequential steps:
* Merge of the two inputs, match of the L1 objects to the offline ones, compression of the variables
* Calculation of the calibration, pruduction of its LUTs, and its application
* Calculation of the isolation, pruduction of its LUTs, and its application
* Prodution of turnon curves
* Evaluation of the L1 rate

All of this steps for the optimization are done using this second tool: https://github.com/jonamotta/TauObjectsOptimization

Due to the package's lack of forward-compatibility with CMSSW, the optimzation is run into CMSSW_11_0_2.

## Ntuples content
The Ntuple produced that way contain basic tau offline quantities (kinematics, DM, various discriminators) + bits corresponding to various HLT triggers (tauTriggerBits variable) + L1-HLT specific variables (for expert user).

The events stored pass basic mu+tauh T&P selections (OS requirement not applied for filter! isOS variable stored in Ntuple).

The tree triggerNames has the name of all the HLT paths included in the tauTriggerBits variable.

This can be checked for instance with
```
triggerNames->Scan("triggerNames","","colsize=100")
*******************************************************************************************************************
*    Row   *                                                                                         triggerNames *
*******************************************************************************************************************
*        0 *                                                 HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_SingleL1_v *
*        1 *                                         HLT_IsoMu24_eta2p1_LooseChargedIsoPFTau20_TightID_SingleL1_v *
*        2 *                                                HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_SingleL1_v *
*        3 *                                        HLT_IsoMu24_eta2p1_MediumChargedIsoPFTau20_TightID_SingleL1_v *
*        4 *                                                 HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_SingleL1_v *
*        5 *                                         HLT_IsoMu24_eta2p1_TightChargedIsoPFTau20_TightID_SingleL1_v *
...
```
The Row of the path correspond to the bit number in the tauTriggerBits variable.

In the example presented here, the decision of the MediumChargedIsoPFTau20 leg can be checked for instance by requiring (tauTriggerBits>>2)&1 (matching with tag muon + offline tau of 0.5 included).
