import FWCore.ParameterSet.Config as cms

print("Running on data")

# filter HLT paths for T&P
import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt


HLTLIST_TAG = cms.VPSet(
    ##Mu SingleL1
    
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p08"),
        path2 = cms.vstring (""),
        leg1 = cms.int32(13),
        leg2 = cms.int32(13)
    ),

    # cms.PSet (
    #     HLT = cms.string("HLT_IsoMu30_v"),
    #     path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f30QL3trkIsoFiltered0p08"),
    #     path2 = cms.vstring (""),
    #     leg1 = cms.int32(13),
    #     leg2 = cms.int32(13)
    # ),
)


HLTLIST = cms.VPSet(
    ##MuTau SingleL1
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_LooseChargedIsoPFTauHPS20_Trk1_eta2p1_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu27LooseChargedIsoPFTau20"),
        path2 = cms.vstring ("hltHpsPFTau20TrackLooseChargedIsoAgainstMuon", "hltHpsOverlapFilterIsoMu27LooseChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_MediumChargedIsoPFTauHPS20_Trk1_eta2p1_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu27MediumChargedIsoPFTau20"),
        path2 = cms.vstring ("hltHpsPFTau20TrackMediumChargedIsoAgainstMuon", "hltHpsOverlapFilterIsoMu27MediumChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu27_TightChargedIsoPFTauHPS20_Trk1_eta2p1_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu27TightChargedIsoPFTau20"),
        path2 = cms.vstring ("hltHpsPFTau20TrackTightChargedIsoAgainstMuon", "hltHpsOverlapFilterIsoMu27TightChargedIsoPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),

    ##MuTau CrossL1
    cms.PSet (
        HLT = cms.string("HLT_IsoMu20_eta2p1_LooseDeepTauPFTauHPS27_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoBigORMu18erTauXXer2p1L1f0L2f10QL3f20QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu20LooseMuTauWPDeepTauPFTau27L1Seeded"),
        path2 = cms.vstring ("hltHpsSelectedPFTau27LooseMuTauWPDeepTauVsJetsAgainstMuonL1HLTMatched", "hltHpsOverlapFilterIsoMu20LooseMuTauWPDeepTauPFTau27L1Seeded"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoBigORMu18erTauXXer2p1L1f0L2f10QL3f20QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu20TightChargedIsoPFTau27L1Seeded"),
        path2 = cms.vstring ("hltHpsSelectedPFTau27TightChargedIsolationAgainstMuonL1HLTMatched", "hltHpsOverlapFilterIsoMu20TightChargedIsoPFTau27L1Seeded"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoBigORMu18erTauXXer2p1L1f0L2f10QL3f20QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu20TightChargedIsoTightOOSCPhotonsPFTau27L1Seeded"),
        path2 = cms.vstring ("hltHpsSelectedPFTau27TightChargedIsolationTightOOSCPhotonsAgainstMuonL1HLTMatched", "hltHpsOverlapFilterIsoMu20TightChargedIsoTightOOSCPhotonsPFTau27L1Seeded"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_LooseDeepTauPFTauHPS30_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltIsoMu24FilterEle24Tau30Monitoring", "hltHpsOverlapFilterIsoMu24LooseETauWPDeepTauPFTau30L1Seeded"),
        path2 = cms.vstring ("hltHpsSelectedPFTau30LooseETauWPDeepTauL1HLTMatchedMonitoring", "hltHpsOverlapFilterIsoMu24LooseETauWPDeepTauPFTau30L1Seeded"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS35_L2NN_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau35Monitoring"),
        path2 = cms.vstring ("hltHpsSelectedPFTau35MediumDitauWPDeepTauL1HLTBigOrMuXXerIsoTauYYerMatched", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau35Monitoring"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),

    ##################################
    ## NOT IN 'FIRST-COLLISIONS'
    
    ##MuTau SingleL1
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sSingleMu22erL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu24MediumDeepTauPFTau20"),
        path2 = cms.vstring ("hltHpsSinglePFTau20MediumDitauWPDeepTauNoMatchForVBFIsoTau", "hltHpsOverlapFilterIsoMu24MediumDeepTauPFTau20"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    ##MuTau CrossL1
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sVeryBigOrMu18erTauXXerL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau30Monitoring"),
        path2 = cms.vstring ("hltHpsSelectedPFTau30MediumDitauWPDeepTauL1HLTVeryBigOrMu18erTauXXerMatched", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau30Monitoring"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet60_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sVeryBigOrMu18erTauXXerL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterDeepTauPFTau30VeryBigOrMu18erTauXXPFJet60"),
        path2 = cms.vstring ("hltHpsSelectedPFTau30MediumDitauWPDeepTauL1HLTVeryBigOrMu18erTauXXerMatched", "hltHpsOverlapFilterDeepTauPFTau30VeryBigOrMu18erTauXXPFJet60"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS30_L2NN_eta2p1_PFJet75_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sVeryBigOrMu18erTauXXerL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterDeepTauPFTau30VeryBigOrMu18erTauXXPFJet75"),
        path2 = cms.vstring ("hltHpsSelectedPFTau30MediumDitauWPDeepTauL1HLTVeryBigOrMu18erTauXXerMatched", "hltHpsOverlapFilterDeepTauPFTau30VeryBigOrMu18erTauXXPFJet75"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
    cms.PSet (
        HLT = cms.string("HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS45_L2NN_eta2p1_CrossL1_v"),
        path1 = cms.vstring ("hltL3crIsoL1sBigOrMuXXerIsoTauYYerL1f0L2f10QL3f24QL3trkIsoFiltered0p08", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau45MonitoringForVBFIsoTau"),
        path2 = cms.vstring ("hltHpsSelectedPFTau45MediumDitauWPDeepTauL1HLTBigOrMuXXerIsoTauYYerMatchedForVBFIsoTau", "hltHpsOverlapFilterIsoMu24MediumDitauWPDeepTauPFTau45MonitoringForVBFIsoTau"),
        leg1 = cms.int32(13),
        leg2 = cms.int32(15)
    ),
)


hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = ['HLT_IsoMu27_v*'],
    andOr = cms.bool(True), # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(True) #if True: throws exception if a trigger path is invalid
)

## only events where slimmedMuons has exactly 1 muon
muonNumberFilter = cms.EDFilter ("muonNumberFilter",
    src = cms.InputTag("slimmedMuons")
)

## good muons for T&P
goodMuons = cms.EDFilter("PATMuonRefSelector",
        src = cms.InputTag("slimmedMuons"),
        cut = cms.string(
                'pt > 24 && abs(eta) < 2.1 ' # kinematics
                '&& ( (pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5 * pfIsolationR04().sumPUPt, 0.0)) / pt() ) < 0.1 ' # isolation
                '&& isMediumMuon()' # quality -- medium muon
                # 'pt>0 && abs(eta) < 2.1'
        ),
        filter = cms.bool(True)
)

## good taus - apply analysis selection
goodTaus = cms.EDFilter("PATTauRefSelector",
        src = cms.InputTag("slimmedTaus"),
        cut = cms.string(
                'pt > 20 && abs(eta) < 2.1 ' #kinematics
                '&& abs(charge) > 0 && abs(charge) < 2 ' #sometimes 2 prongs have charge != 1
                '&& tauID("decayModeFinding") > 0.5 ' # tau ID
                '&& tauID("byMediumDeepTau2017v2p1VSjet") > 0.5 ' # anti-Jet medium
                '&& tauID("byMediumDeepTau2017v2p1VSmu") > 0.5 ' # anti-Muon tight
                '&& tauID("byLooseDeepTau2017v2p1VSe") > 0.5 ' # anti-Ele loose
                # 'pt>0 && abs(eta) < 2.1'
        ),
        filter = cms.bool(True)
)

## b jet veto : no additional b jets in the event (reject tt) -- use in sequence with
bjets = cms.EDFilter("PATJetRefSelector",
        src = cms.InputTag("slimmedJets"),
        cut = cms.string(
                'pt > 20 && abs(eta) < 2.4 ' #kinematics
                '&& bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags") > 0.8484' # b tag with medium WP
        ),
)

TagAndProbe = cms.EDFilter("TauTagAndProbeFilterRun3",
                           taus  = cms.InputTag("goodTaus"),
                           muons = cms.InputTag("goodMuons"),
                           met   = cms.InputTag("slimmedMETs"),
                           useWMassCuts = cms.bool(True),
                           useZMassCuts = cms.bool(True),
                           electrons = cms.InputTag("slimmedElectrons"),
                           bjets = cms.InputTag("bjets")
)



patTriggerUnpacker = cms.EDProducer("PATTriggerObjectStandAloneUnpacker",
                                    patTriggerObjectsStandAlone = cms.InputTag("slimmedPatTrigger"),
                                    triggerResults = cms.InputTag('TriggerResults', '', "HLT"),
                                    unpackFilterLabels = cms.bool(True)
                                    )

Ntuplizer = cms.EDAnalyzer("NtuplizerRun3",
    treeName = cms.string("TagAndProbe"),
    isMC = cms.bool(False),
    genCollection = cms.InputTag(""),
    genPartCollection = cms.InputTag(""),
    muons = cms.InputTag("TagAndProbe"),
    taus = cms.InputTag("TagAndProbe"),
    puInfo = cms.InputTag("slimmedAddPileupInfo"), 
    met   = cms.InputTag("slimmedMETs"),
    triggerList = HLTLIST,
    triggerList_tag = HLTLIST_TAG,
    triggerSet = cms.InputTag("patTriggerUnpacker"),
    triggerResultsLabel = cms.InputTag("TriggerResults", "", "HLT"),
    L1Tau = cms.InputTag("caloStage2Digis", "Tau", "RECO"),
    #L1EmuTau = cms.InputTag("simCaloStage2Digis"),
    L1EmuTau = cms.InputTag("simCaloStage2Digis", "MP"),
    Vertexes = cms.InputTag("offlineSlimmedPrimaryVertices"),
    L2CaloJet_ForIsoPix_Collection = cms.InputTag("hltL2TausForPixelIsolation", "", "TEST"),
    L2CaloJet_ForIsoPix_IsoCollection = cms.InputTag("hltL2TauPixelIsoTagProducer", "", "TEST"),
    stageL1Trigger = cms.uint32(2)
)

TAndPseq = cms.Sequence(
    hltFilter        +
    muonNumberFilter +
    goodMuons        +
    goodTaus         +
    bjets            +
    TagAndProbe
)

NtupleSeq = cms.Sequence(
    patTriggerUnpacker +
    Ntuplizer
)
