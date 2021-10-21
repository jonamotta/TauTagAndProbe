# TauTagAndProbe
Set of tools to evaluate tau trigger performance on T&amp;P

## Install instructions
```bash
cmsrel CMSSW_11_0_2
cd CMSSW_11_0_2/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline l1t-integration-CMSSW_11_0_2
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v104.5
git cms-addpkg L1Trigger/L1TCommon
git cms-addpkg L1Trigger/L1TMuon
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TMuon.git L1Trigger/L1TMuon/data
git cms-addpkg L1Trigger/L1TCalorimeter
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

mkdir HiggsAnalysis
cd HiggsAnalysis
git clone git@github.com:bendavid/GBRLikelihood.git
# modify the first line of `HiggsAnalysis/GBRLikelihood/BuildFile.xml` to have `-std=c++17`

cd ..
git clone https://github.com/davignon/TauTagAndProbe # package for the production of the starting NTuples

git cms-checkdeps -A -a

scram b -j 10

git clone https://github.com/jonamotta/TauObjectsOptimization # package for the full optimization
```

L1T emulation relevant GlobalTags in `CMSSW_11_0_2` are:
* for run2 data reprocessing `110X_dataRun2_v12`
* for run2 mc `110X_mcRun2_asymptotic_v6`
* for run3 mc `110X_mcRun3_2021_realistic_v6(9)`


## Tool utilization
To do the optimization two things are needed:
* L1 objects (sometimes re-emulated) that are extracted from the RAW tier (in principle, non-re-emulated L1 objects can also be extracted from MiniAOD, but for consistency we never do that)
* Offline objects that are extracted from the AOD or MiniAOD tier

### Production of the input objects
To produce the input NTuples to the optimization the `TauTagAndProbe` package is used. The useful scripts for this are mainly in the `test` subfolder.

Jobs on RAW are submitted using `submitOnTier3_reEmulL1_zeroBias.py` which in turn launches `reEmulL1_X.py`
Before launching this you need to fix
* the Global Tag
* the configuration of the L1Calorimeter (`process.load("L1Trigger.L1TCalorimeter.caloStage2Params_20XX_vX_X_XXX_cfi")`)


Jobs on MiniAOD are submitted using `submitOnTier3.py` which in turn launches `test_noTagAndProbe.py`
Before launching this you need to fix
* the Global Tag

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


### Plotting: mostly turn-ons
Any basic check can be performed using those Ntuples (efficiency vs pT, eta-phi...) using custom code developed by the user.

A more fancy package is available to produce turn-on plots with CB fits.

For this, the Ntuples must first be converted using the script test/convertTreeForFitting.py (blame RooFit for not being able to deal with custom boolean cuts).

The package for plotting is available in test/fitter/ (to be compiled with make).

The CB fit can be run using a as an example test/fitter/hlt_turnOn_fitter.par (includes example for L1 and HLT turnons w/ subtraction of SS mu+tauh events to take into account contamination from fake taus using bkgSubW weight).

To be launched with
```
./fit.exe run/hlt_turnOn_fitter.par
```
The "Michelangelo" turn-on plot can then be produced adapting the script test/fitter/results/plot_turnOn_Data_vs_MC.py

### Resolutions:
UNDER DEVELOPMENT


