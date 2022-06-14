  #ifndef NTUPLIZER_NOTAGANDPROBE_MULTIPLETAUS_H
  #define NTUPLIZER_NOTAGANDPROBE_MULTIPLETAUS_H

  #include <cmath>
  #include <vector>
  #include <algorithm>
  #include <string>
  #include <map>
  #include <vector>
  #include <utility>
  #include <TNtuple.h>
  #include <TString.h>
  #include <bitset>


  #include "FWCore/Framework/interface/EDAnalyzer.h"
  #include "FWCore/ParameterSet/interface/ParameterSet.h"
  #include <FWCore/Framework/interface/Frameworkfwd.h>
  #include <FWCore/Framework/interface/Event.h>
  #include <FWCore/Framework/interface/ESHandle.h>
  #include <FWCore/Utilities/interface/InputTag.h>
  #include <DataFormats/PatCandidates/interface/Muon.h>
  #include <DataFormats/PatCandidates/interface/Tau.h>
  #include "DataFormats/PatCandidates/interface/Jet.h"
  #include "DataFormats/PatCandidates/interface/MET.h"


  #include "DataFormats/L1Trigger/interface/Jet.h"

  #include "FWCore/ServiceRegistry/interface/Service.h"
  #include "FWCore/Common/interface/TriggerNames.h"
  #include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
  #include "DataFormats/L1Trigger/interface/Tau.h"
  #include "DataFormats/VertexReco/interface/Vertex.h"

  #include "FWCore/Framework/interface/EventSetup.h"
  #include "JetMETCorrections/Objects/interface/JetCorrector.h"
  #include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
  #include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
  #include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"

  #include "DataFormats/Common/interface/TriggerResults.h"

  #include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"


  #include "tParameterSet.h"

  #include "CommonTools/UtilAlgos/interface/TFileService.h"
  #include <DataFormats/Common/interface/View.h>


  //Set this variable to decide the number of triggers that you want to check simultaneously
  #define NUMBER_OF_MAXIMUM_TRIGGERS 64


  /*
    ██████  ███████  ██████ ██       █████  ██████   █████  ████████ ██  ██████  ███    ██
    ██   ██ ██      ██      ██      ██   ██ ██   ██ ██   ██    ██    ██ ██    ██ ████   ██
    ██   ██ █████   ██      ██      ███████ ██████  ███████    ██    ██ ██    ██ ██ ██  ██
    ██   ██ ██      ██      ██      ██   ██ ██   ██ ██   ██    ██    ██ ██    ██ ██  ██ ██
    ██████  ███████  ██████ ███████ ██   ██ ██   ██ ██   ██    ██    ██  ██████  ██   ████
  */

  class Ntuplizer_noTagAndProbe_multipleTaus : public edm::EDAnalyzer {
  public:
    /// Constructor
    explicit Ntuplizer_noTagAndProbe_multipleTaus(const edm::ParameterSet&);
    /// Destructor
    virtual ~Ntuplizer_noTagAndProbe_multipleTaus();

  private:
    //----edm control---
    virtual void beginJob() ;
    virtual void beginRun(edm::Run const&, edm::EventSetup const&);
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob();
    virtual void endRun(edm::Run const&, edm::EventSetup const&);
    void Initialize();
    bool hasFilters(const pat::TriggerObjectStandAlone&  obj , const std::vector<std::string>& filtersToLookFor);
    int FillJet(const edm::View<pat::Jet> *jets, const edm::Event& event);  
    //int FillJet(const edm::View<pat::Jet> *jets, const edm::Event& event, JetCorrectionUncertainty* jecUnc);  

    TTree *_tree;
    TTree *_triggerNamesTree;
    std::string _treeName;
    // -------------------------------------
    // variables to be filled in output tree
    ULong64_t       _indexevents;
    Int_t           _runNumber;
    Int_t           _lumi;
    float _MC_weight;
    unsigned long _tauTriggerBits;
    std::vector<float> _tauPt;
    std::vector<float> _tauEta;
    std::vector<float> _tauPhi;
    std::vector<int>   _tauCharge;
    std::vector<int>   _tauDecayMode;
    std::vector<float> _hltPt;
    std::vector<float> _hltEta;
    std::vector<float> _hltPhi;
    std::vector<int> _l1tQual;
    std::vector<float> _l1tPt;
    std::vector<float> _l1tEta;
    std::vector<float> _l1tPhi;
    std::vector<int> _l1tIso;
    int _l1tEmuQual;
    float _l1tEmuPt;
    float _l1tEmuEta;
    float _l1tEmuPhi;
    int _l1tEmuIso;
    int _l1tEmuNTT;
    int _l1tEmuHasEM;
    int _l1tEmuIsMerged;
    int _l1tEmuTowerIEta;
    int _l1tEmuTowerIPhi;
    int _l1tEmuRawEt;
    int _l1tEmuIsoEt;
    std::vector<int> _l1tQualJet;
    std::vector<float> _l1tPtJet;
    std::vector<float> _l1tEtaJet;
    std::vector<float> _l1tPhiJet;
    std::vector<int> _l1tIsoJet;
    std::vector<int> _l1tTowerIEtaJet;
    std::vector<int> _l1tTowerIPhiJet;
    std::vector<int> _l1tRawEtJet;

    Bool_t _hasTriggerMuonType;
    Bool_t _hasTriggerTauType;
    std::vector<Bool_t> _isMatched;
    Bool_t _isOS;
    int _foundJet;
    int _Nvtx;


    //Jets variables
    Int_t _numberOfJets;
    std::vector<Float_t> _jets_px;
    std::vector<Float_t> _jets_py;
    std::vector<Float_t> _jets_pz;
    std::vector<Float_t> _jets_e;
    std::vector<Float_t> _jets_rawPt;
    std::vector<Float_t> _jets_area;
    std::vector<Float_t> _jets_mT;
    std::vector<Float_t> _jets_PUJetID;
    std::vector<Float_t> _jets_PUJetIDupdated;
    std::vector<Float_t> _jets_vtxPt;
    std::vector<Float_t> _jets_vtxMass;
    std::vector<Float_t> _jets_vtx3dL;
    std::vector<Float_t> _jets_vtxNtrk;
    std::vector<Float_t> _jets_vtx3deL;
    std::vector<Float_t> _jets_leadTrackPt;
    std::vector<Float_t> _jets_leptonPtRel; 
    std::vector<Float_t> _jets_leptonPt;    
    std::vector<Float_t> _jets_leptonDeltaR;
    std::vector<Float_t> _jets_chEmEF;
    std::vector<Float_t> _jets_chHEF;
    std::vector<Float_t> _jets_nEmEF;
    std::vector<Float_t> _jets_nHEF;
    std::vector<Float_t> _jets_MUF;
    std::vector<Int_t>   _jets_neMult;
    std::vector<Int_t>   _jets_chMult;
    std::vector<Float_t> _jets_jecUnc;

    std::vector<Float_t> _jets_QGdiscr;

    std::vector<Int_t> _jets_Flavour; // parton flavour
    std::vector<Int_t> _jets_HadronFlavour; // hadron flavour
    std::vector<Int_t> _jets_genjetIndex;
    std::vector<Float_t> _bdiscr;
    std::vector<Float_t> _bdiscr2;
    std::vector<Float_t> _bdiscr3;
    std::vector<Int_t> _jetID; //1=loose, 2=tight, 3=tightlepveto
    std::vector<Float_t> _jetrawf;

    Double_t _PFMET_pt;
    Double_t _PFMET_phi;
    Double_t _PFMET_px;
    Double_t _PFMET_py;
    Double_t _PFMET_sumEt;

    Double_t _CaloMET_pt;
    Double_t _CaloMET_phi;
    Double_t _CaloMET_px;
    Double_t _CaloMET_py;
    Double_t _CaloMET_sumEt;

    std::vector<Float_t> _genJet_pt;
    std::vector<Float_t> _genJet_eta;
    std::vector<Float_t> _genJet_phi;
    std::vector<Float_t> _genJet_emEnergy;
    std::vector<Float_t> _genJet_hadEnergy;
    std::vector<Float_t> _genJet_invisibleEnergy;
    std::vector<Float_t> _genJet_muonEnergy;

    std::vector<Int_t> _genPart_id;
    std::vector<Int_t> _genPart_stat;
    std::vector<Int_t> _genPart_parent;
    std::vector<Float_t> _genPart_pt;
    std::vector<Float_t> _genPart_eta;
    std::vector<Float_t> _genPart_phi;
    std::vector<Float_t> _genPart_E;
    std::vector<Int_t> _genPart_ch;

    edm::EDGetTokenT<GenEventInfoProduct> _genTag;
    edm::EDGetTokenT<reco::GenJetCollection> _genJetTag;
    edm::EDGetTokenT<reco::GenParticleCollection> _genParticleTag;
    edm::EDGetTokenT<pat::TauRefVector>   _tauTag;
    edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> _triggerObjects;
    edm::EDGetTokenT<edm::TriggerResults> _triggerBits;
    edm::EDGetTokenT<l1t::TauBxCollection> _L1TauTag  ;
    edm::EDGetTokenT<l1t::TauBxCollection> _L1EmuTauTag  ;
    edm::EDGetTokenT<edm::View<pat::Jet>> _JetTag;
    edm::EDGetTokenT<edm::View<pat::MET>> _MetTag;
    edm::EDGetTokenT<BXVector<l1t::Jet>> _l1tJetTag;
    // edm::EDGetTokenT<BXVector<l1t::Jet>> _l1tEmuJetTag;
    edm::EDGetTokenT<std::vector<reco::Vertex>> _VtxTag;

    //!Contains the parameters
    tVParameterSet _parameters;

    edm::InputTag _processName;
    //! Maximum
    std::bitset<NUMBER_OF_MAXIMUM_TRIGGERS> _tauTriggerBitSet;



    HLTConfigProvider _hltConfig;


  };

  /*
    ██ ███    ███ ██████  ██      ███████ ███    ███ ███████ ███    ██ ████████  █████  ████████ ██  ██████  ███    ██
    ██ ████  ████ ██   ██ ██      ██      ████  ████ ██      ████   ██    ██    ██   ██    ██    ██ ██    ██ ████   ██
    ██ ██ ████ ██ ██████  ██      █████   ██ ████ ██ █████   ██ ██  ██    ██    ███████    ██    ██ ██    ██ ██ ██  ██
    ██ ██  ██  ██ ██      ██      ██      ██  ██  ██ ██      ██  ██ ██    ██    ██   ██    ██    ██ ██    ██ ██  ██ ██
    ██ ██      ██ ██      ███████ ███████ ██      ██ ███████ ██   ████    ██    ██   ██    ██    ██  ██████  ██   ████
  */

  // ----Constructor and Destructor -----
  Ntuplizer_noTagAndProbe_multipleTaus::Ntuplizer_noTagAndProbe_multipleTaus(const edm::ParameterSet& iConfig) :
    _genTag         (consumes<GenEventInfoProduct>                    (iConfig.getParameter<edm::InputTag>("genCollection"))),
    _genJetTag      (consumes<reco::GenJetCollection>                 (iConfig.getParameter<edm::InputTag>("genJetCollection"))),
    _genParticleTag (consumes<reco::GenParticleCollection>            (iConfig.getParameter<edm::InputTag>("genParticleCollection"))),
    _tauTag         (consumes<pat::TauRefVector>                      (iConfig.getParameter<edm::InputTag>("taus"))),
    _triggerObjects (consumes<pat::TriggerObjectStandAloneCollection> (iConfig.getParameter<edm::InputTag>("triggerSet"))),
    _triggerBits    (consumes<edm::TriggerResults>                    (iConfig.getParameter<edm::InputTag>("triggerResultsLabel"))),
    _L1TauTag       (consumes<l1t::TauBxCollection>                   (iConfig.getParameter<edm::InputTag>("L1Tau"))),
    _L1EmuTauTag    (consumes<l1t::TauBxCollection>                   (iConfig.getParameter<edm::InputTag>("L1EmuTau"))),
    _JetTag         (consumes<edm::View<pat::Jet>>                    (iConfig.getParameter<edm::InputTag>("jetCollection"))),
    _MetTag         (consumes<edm::View<pat::MET>>                    (iConfig.getParameter<edm::InputTag>("metCollection"))),
    _l1tJetTag      (consumes<BXVector<l1t::Jet>>                     (iConfig.getParameter<edm::InputTag>("l1tJetCollection"))),
    _VtxTag         (consumes<std::vector<reco::Vertex>>              (iConfig.getParameter<edm::InputTag>("Vertexes")))
  {
    this -> _treeName = iConfig.getParameter<std::string>("treeName");
    this -> _processName = iConfig.getParameter<edm::InputTag>("triggerResultsLabel");

    TString triggerName;
    edm::Service<TFileService> fs;
    this -> _triggerNamesTree = fs -> make<TTree>("triggerNames", "triggerNames");
    this -> _triggerNamesTree -> Branch("triggerNames",&triggerName);

    //Building the trigger arrays
    const std::vector<edm::ParameterSet>& HLTList = iConfig.getParameter <std::vector<edm::ParameterSet> > ("triggerList");
    for (const edm::ParameterSet& parameterSet : HLTList) {
      tParameterSet pSet;
      pSet.hltPath = parameterSet.getParameter<std::string>("HLT");
      triggerName = pSet.hltPath;
      pSet.hltFilters1 = parameterSet.getParameter<std::vector<std::string> >("path1");
      pSet.hltFilters2 = parameterSet.getParameter<std::vector<std::string> >("path2");
      pSet.leg1 = parameterSet.getParameter<int>("leg1");
      pSet.leg2 = parameterSet.getParameter<int>("leg2");
      this -> _parameters.push_back(pSet);

      this -> _triggerNamesTree -> Fill();
    }


    this -> Initialize();
    return;
  }

  Ntuplizer_noTagAndProbe_multipleTaus::~Ntuplizer_noTagAndProbe_multipleTaus()
  {}

  void Ntuplizer_noTagAndProbe_multipleTaus::beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
  {
    Bool_t changedConfig = false;

    if(!this -> _hltConfig.init(iRun, iSetup, this -> _processName.process(), changedConfig)){
      edm::LogError("HLTMatchingFilter") << "Initialization of HLTConfigProvider failed!!";
      return;
    }

    const edm::TriggerNames::Strings& triggerNames = this -> _hltConfig.triggerNames();
    //std::cout << " ===== LOOKING FOR THE PATH INDEXES =====" << std::endl;
    for (tParameterSet& parameter : this -> _parameters){
      const std::string& hltPath = parameter.hltPath;
      bool found = false;
      for(unsigned int j=0; j < triggerNames.size(); j++)
        {
    //std::cout << triggerNames[j] << std::endl;
    if (triggerNames[j].find(hltPath) != std::string::npos) {
      found = true;
      parameter.hltPathIndex = j;

      //std::cout << "### FOUND AT INDEX #" << j << " --> " << triggerNames[j] << std::endl;
    }
        }
      if (!found) parameter.hltPathIndex = -1;
    }

  }

  void Ntuplizer_noTagAndProbe_multipleTaus::Initialize() {
    this -> _indexevents = 0;
    this -> _runNumber = 0;
    this -> _lumi = 0;
    this -> _MC_weight = 1;
    this -> _tauPt.clear();
    this -> _tauEta.clear();
    this -> _tauPhi.clear();
    this -> _tauCharge.clear();
    this -> _tauDecayMode.clear();
    this -> _isMatched.clear();
    this -> _hltPt.clear();
    this -> _hltEta.clear();
    this -> _hltPhi.clear();
    this -> _l1tPt.clear();
    this -> _l1tEta.clear();
    this -> _l1tPhi.clear();
    this -> _l1tQual.clear();
    this -> _l1tIso.clear();
    this -> _l1tEmuPt = -1;
    this -> _l1tEmuEta = 666;
    this -> _l1tEmuPhi = 666;
    this -> _l1tEmuQual = -1;
    this -> _l1tEmuIso = -1;
    this -> _l1tEmuNTT = -1;
    this -> _l1tEmuHasEM = -1;
    this -> _l1tEmuIsMerged = -1;
    this -> _l1tEmuTowerIEta = -1;
    this -> _l1tEmuTowerIPhi = -1;
    this -> _l1tEmuRawEt = -1;
    this -> _l1tEmuIsoEt = -1;
    this -> _foundJet = 0;

    this -> _PFMET_pt = -1;
    this -> _PFMET_phi = -1;
    this -> _PFMET_px = -1;
    this -> _PFMET_py = -1;
    this -> _PFMET_sumEt = -1;

    this -> _CaloMET_pt = -1;
    this -> _CaloMET_phi = -1;
    this -> _CaloMET_px = -1;
    this -> _CaloMET_py = -1;
    this -> _CaloMET_sumEt = -1;

    this -> _genJet_pt . clear();
    this -> _genJet_eta . clear();
    this -> _genJet_phi . clear();
    this -> _genJet_emEnergy . clear();
    this -> _genJet_hadEnergy . clear();
    this -> _genJet_invisibleEnergy . clear();
    this -> _genJet_muonEnergy . clear();

    this -> _genPart_id . clear();
    this -> _genPart_stat . clear();
    this -> _genPart_parent . clear();
    this -> _genPart_pt . clear();
    this -> _genPart_eta . clear();
    this -> _genPart_phi . clear();
    this -> _genPart_E . clear();
    this -> _genPart_ch . clear();

    this -> _l1tPtJet . clear();
    this -> _l1tEtaJet  . clear();
    this -> _l1tPhiJet . clear();
    this -> _l1tQualJet . clear();
    this -> _l1tIsoJet . clear();
    this -> _l1tTowerIEtaJet . clear();
    this -> _l1tTowerIPhiJet . clear();
    this -> _l1tRawEtJet . clear();

    _jets_px.clear();
    _jets_py.clear();
    _jets_pz.clear();
    _jets_e.clear();
    _jets_rawPt.clear();
    _jets_area.clear();
    _jets_mT.clear();
    _jets_PUJetID.clear();
    _jets_PUJetIDupdated.clear();
    _jets_vtxPt.clear();
    _jets_vtxMass.clear();
    _jets_vtx3dL.clear();
    _jets_vtxNtrk.clear();
    _jets_vtx3deL.clear();
    _jets_leadTrackPt.clear();
    _jets_leptonPtRel.clear();
    _jets_leptonPt.clear();
    _jets_leptonDeltaR.clear();
    _jets_chEmEF.clear();
    _jets_chHEF.clear();
    _jets_nEmEF.clear();
    _jets_nHEF.clear();
    _jets_MUF.clear();
    _jets_neMult.clear();
    _jets_chMult.clear();
    _jets_Flavour.clear();
    _jets_HadronFlavour.clear();
    _jets_genjetIndex.clear();
    _jets_jecUnc.clear();
    _jets_QGdiscr.clear();
    _numberOfJets=0;
    _bdiscr.clear();
    _bdiscr2.clear();
    _bdiscr3.clear();
    _jetID.clear();
    _jetrawf.clear();

  }


  void Ntuplizer_noTagAndProbe_multipleTaus::beginJob()
  {
    edm::Service<TFileService> fs;
    this -> _tree = fs -> make<TTree>(this -> _treeName.c_str(), this -> _treeName.c_str());

    //Branches
    this -> _tree -> Branch("EventNumber",&_indexevents,"EventNumber/l");
    this -> _tree -> Branch("RunNumber",&_runNumber,"RunNumber/I");
    this -> _tree -> Branch("lumi",&_lumi,"lumi/I");
    this -> _tree -> Branch("MC_weight",&_MC_weight,"MC_weight/F");
    this -> _tree -> Branch("tauTriggerBits", &_tauTriggerBits, "tauTriggerBits/l");
    this -> _tree -> Branch("tauPt",  &_tauPt);
    this -> _tree -> Branch("tauEta", &_tauEta);
    this -> _tree -> Branch("tauPhi", &_tauPhi);
    this -> _tree -> Branch("tauCharge",  &_tauCharge);
    this -> _tree -> Branch("tauDecayMode",  &_tauDecayMode);
    this -> _tree -> Branch("hltPt",  &_hltPt);
    this -> _tree -> Branch("hltEta", &_hltEta);
    this -> _tree -> Branch("hltPhi", &_hltPhi);
    this -> _tree -> Branch("l1tPt",  &_l1tPt);
    this -> _tree -> Branch("l1tEta", &_l1tEta);
    this -> _tree -> Branch("l1tPhi", &_l1tPhi);
    this -> _tree -> Branch("l1tQual", &_l1tQual);
    this -> _tree -> Branch("l1tIso", &_l1tIso);
    this -> _tree -> Branch("l1tEmuPt",  &_l1tEmuPt,  "l1tEmuPt/F");
    this -> _tree -> Branch("l1tEmuEta", &_l1tEmuEta, "l1tEmuEta/F");
    this -> _tree -> Branch("l1tEmuPhi", &_l1tEmuPhi, "l1tEmuPhi/F");
    this -> _tree -> Branch("l1tEmuQual", &_l1tEmuQual, "l1tEmuQual/I");
    this -> _tree -> Branch("l1tEmuIso", &_l1tEmuIso, "l1tEmuIso/I");
    this -> _tree -> Branch("l1tEmuNTT", &_l1tEmuNTT, "l1tEmuNTT/I");
    this -> _tree -> Branch("l1tEmuHasEM", &_l1tEmuHasEM, "l1tEmuHasEM/I");
    this -> _tree -> Branch("l1tEmuIsMerged", &_l1tEmuIsMerged, "l1tEmuIsMerged/I");
    this -> _tree -> Branch("l1tEmuTowerIEta", &_l1tEmuTowerIEta, "l1tEmuTowerIEta/I");
    this -> _tree -> Branch("l1tEmuTowerIPhi", &_l1tEmuTowerIPhi, "l1tEmuTowerIPhi/I");
    this -> _tree -> Branch("l1tEmuRawEt", &_l1tEmuRawEt, "l1tEmuRawEt/I");
    this -> _tree -> Branch("l1tEmuIsoEt", &_l1tEmuIsoEt, "l1tEmuIsoEt/I");

    this -> _tree -> Branch("l1tPtJet",  &_l1tPtJet);
    this -> _tree -> Branch("l1tEtaJet", &_l1tEtaJet);
    this -> _tree -> Branch("l1tPhiJet", &_l1tPhiJet);
    this -> _tree -> Branch("l1tQualJet", &_l1tQualJet);
    this -> _tree -> Branch("l1tIsoJet", &_l1tIsoJet);
    this -> _tree -> Branch("l1tTowerIEtaJet", &_l1tTowerIEtaJet);
    this -> _tree -> Branch("l1tTowerIPhiJet", &_l1tTowerIPhiJet);
    this -> _tree -> Branch("l1tRawEtJet", &_l1tRawEtJet);

    this -> _tree -> Branch("hasTriggerMuonType", &_hasTriggerMuonType, "hasTriggerMuonType/O");
    this -> _tree -> Branch("hasTriggerTauType", &_hasTriggerTauType, "hasTriggerTauType/O");
    this -> _tree -> Branch("isMatched", &_isMatched);
    // this -> _tree -> Branch("isMatched", &_isMatched, "isMatched/O");
    this -> _tree -> Branch("isOS", &_isOS, "isOS/O");
    this -> _tree -> Branch("foundJet", &_foundJet, "foundJet/I");
    this -> _tree -> Branch("Nvtx", &_Nvtx, "Nvtx/I");
    
    this -> _tree->Branch("JetsNumber",&_numberOfJets,"JetsNumber/I");
    this -> _tree->Branch("jets_px",&_jets_px);
    this -> _tree->Branch("jets_py",&_jets_py);
    this -> _tree->Branch("jets_pz",&_jets_pz);
    this -> _tree->Branch("jets_e",&_jets_e);
    this -> _tree->Branch("jets_rawPt", &_jets_rawPt);
    this -> _tree->Branch("jets_area", &_jets_area);
    this -> _tree->Branch("jets_mT", &_jets_mT);
    this -> _tree->Branch("jets_Flavour",&_jets_Flavour);
    this -> _tree->Branch("jets_HadronFlavour",&_jets_HadronFlavour);
    this -> _tree->Branch("jets_genjetIndex", &_jets_genjetIndex);
    this -> _tree->Branch("jets_PUJetID",&_jets_PUJetID);
    this -> _tree->Branch("jets_PUJetIDupdated",&_jets_PUJetIDupdated);
    this -> _tree->Branch("jets_vtxPt", &_jets_vtxPt);
    this -> _tree->Branch("jets_vtxMass", &_jets_vtxMass);
    this -> _tree->Branch("jets_vtx3dL", &_jets_vtx3dL);
    this -> _tree->Branch("jets_vtxNtrk", &_jets_vtxNtrk);
    this -> _tree->Branch("jets_vtx3deL", &_jets_vtx3deL);
    this -> _tree->Branch("jets_leadTrackPt", &_jets_leadTrackPt);
    this -> _tree->Branch("jets_leptonPtRel", &_jets_leptonPtRel);
    this -> _tree->Branch("jets_leptonPt", &_jets_leptonPt);
    this -> _tree->Branch("jets_leptonDeltaR", &_jets_leptonDeltaR);
    this -> _tree->Branch("jets_chEmEF" , &_jets_chEmEF);
    this -> _tree->Branch("jets_chHEF"  , &_jets_chHEF);
    this -> _tree->Branch("jets_nEmEF"  , &_jets_nEmEF);
    this -> _tree->Branch("jets_nHEF"   , &_jets_nHEF);
    this -> _tree->Branch("jets_MUF"    , &_jets_MUF);
    this -> _tree->Branch("jets_neMult" , &_jets_neMult);
    this -> _tree->Branch("jets_chMult" , &_jets_chMult);
    this -> _tree->Branch("jets_jecUnc" , &_jets_jecUnc);

    this -> _tree -> Branch("PFMET_pt", &_PFMET_pt, "PFMET_pt/D");
    this -> _tree -> Branch("PFMET_phi", &_PFMET_phi, "PFMET_phi/D");
    this -> _tree -> Branch("PFMET_px", &_PFMET_px, "PFMET_px/D");
    this -> _tree -> Branch("PFMET_py", &_PFMET_py, "PFMET_py/D");
    this -> _tree -> Branch("PFMET_sumEt", &_PFMET_sumEt, "PFMET_sumEt/D");

    this -> _tree -> Branch("CaloMET_pt", &_CaloMET_pt, "CaloMET_pt/D");
    this -> _tree -> Branch("CaloMET_phi", &_CaloMET_phi, "CaloMET_phi/D");
    this -> _tree -> Branch("CaloMET_px", &_CaloMET_px, "CaloMET_px/D");
    this -> _tree -> Branch("CaloMET_py", &_CaloMET_py, "CaloMET_py/D");
    this -> _tree -> Branch("CaloMET_sumEt", &_CaloMET_sumEt, "CaloMET_sumEt/D");

    this -> _tree -> Branch("genJet_pt", &_genJet_pt);
    this -> _tree -> Branch("genJet_eta", &_genJet_eta);
    this -> _tree -> Branch("genJet_phi", &_genJet_phi);
    this -> _tree -> Branch("genJet_emEnergy", &_genJet_emEnergy);
    this -> _tree -> Branch("genJet_hadEnergy", &_genJet_hadEnergy);
    this -> _tree -> Branch("genJet_invisibleEnergy", &_genJet_invisibleEnergy);
    this -> _tree -> Branch("genJet_muonEnergy", &_genJet_muonEnergy);

    this -> _tree  -> Branch("genPart_id",&_genPart_id);
    this -> _tree  -> Branch("genPart_stat",&_genPart_stat);
    this -> _tree  -> Branch("genPart_parent",&_genPart_parent);
    this -> _tree  -> Branch("genPart_pt",&_genPart_pt);
    this -> _tree  -> Branch("genPart_eta",&_genPart_eta);
    this -> _tree  -> Branch("genPart_phi",&_genPart_phi);
    this -> _tree  -> Branch("genPart_E",&_genPart_E);
    this -> _tree  -> Branch("genPart_ch",&_genPart_ch);

    return;
  }


  void Ntuplizer_noTagAndProbe_multipleTaus::endJob()
  {
    return;
  }


  void Ntuplizer_noTagAndProbe_multipleTaus::endRun(edm::Run const& iRun, edm::EventSetup const& iSetup)
  {
    return;
  }


  void Ntuplizer_noTagAndProbe_multipleTaus::analyze(const edm::Event& iEvent, const edm::EventSetup& eSetup)
  {
    this -> Initialize();

    _indexevents = iEvent.id().event();
    _runNumber = iEvent.id().run();
    _lumi = iEvent.luminosityBlock();

    edm::Handle<GenEventInfoProduct> genEvt;
    try {iEvent.getByToken(_genTag, genEvt);}  catch (...) {;}

    if(genEvt.isValid())
      {
	this->_MC_weight = genEvt->weight();
      }

    edm::Handle<reco::GenJetCollection> genJets;
    iEvent.getByToken(_genJetTag, genJets);

    for (reco::GenJetCollection::const_iterator jetIt = genJets->begin(); jetIt != genJets->end() ; jetIt++)
      {
	_genJet_pt.push_back(jetIt->pt());
	_genJet_eta.push_back(jetIt->eta());
	_genJet_phi.push_back(jetIt->phi());
	_genJet_emEnergy.push_back(jetIt->emEnergy());
	_genJet_hadEnergy.push_back(jetIt->hadEnergy());
	_genJet_invisibleEnergy.push_back(jetIt->invisibleEnergy());
	_genJet_muonEnergy.push_back(jetIt->muonEnergy());
      } 

    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByToken(_genParticleTag, genParticles);

    if (genParticles.isValid()) {
      int nPart{0};

      for (size_t i = 0; i < genParticles->size(); ++i) {
	const reco::GenParticle& p = (*genParticles)[i];
	int id = p.pdgId();

	// See if the parent was interesting
	int parentID = -10000;
	unsigned int nMo = p.numberOfMothers();
	for (unsigned int i = 0; i < nMo; ++i) {
	  int thisParentID = dynamic_cast<const reco::GenParticle*>(p.mother(i))->pdgId();
	  //
	  // Is this a bottom hadron?
	  int hundredsIndex = abs(thisParentID) / 100;
	  int thousandsIndex = abs(thisParentID) / 1000;
	  if (((abs(thisParentID) >= 23) && (abs(thisParentID) <= 25)) || (abs(thisParentID) == 6) ||
	      (hundredsIndex == 5) || (hundredsIndex == 4) || (thousandsIndex == 5) || (thousandsIndex == 4))
	    parentID = thisParentID;
	}
	if ((parentID == -10000) && (nMo > 0))
	  parentID = dynamic_cast<const reco::GenParticle*>(p.mother(0))->pdgId();
	//
	// If the parent of this particle is interesting, store all of the info
	if ((parentID != p.pdgId()) &&
	    ((parentID > -9999) || (abs(id) == 11) || (abs(id) == 13) || (abs(id) == 23) || (abs(id) == 24) ||
	     (abs(id) == 25) || (abs(id) == 4) || (abs(id) == 5) || (abs(id) == 6)))
	  {

	    _genPart_id.push_back(p.pdgId());
	    _genPart_stat.push_back(p.status());
	    _genPart_parent.push_back(parentID);
	    _genPart_pt.push_back(p.pt());
	    _genPart_eta.push_back(p.eta());
	    _genPart_phi.push_back(p.phi());
	    _genPart_E.push_back(p.energy());
	    _genPart_ch.push_back(p.charge());
	    
	    ++nPart;
	  }
      }
      //l1GenData_->nPart = nPart;
    }

    // cout<<"EventNumber = "<<_indexevents<<endl;

    // std::auto_ptr<pat::MuonRefVector> resultMuon(new pat::MuonRefVector);

    // search for the tag in the event
    edm::Handle<pat::TauRefVector>  tauHandle;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<edm::View<pat::Jet>> jetHandle;
    edm::Handle<edm::View<pat::MET>> metHandle;
    edm::Handle<BXVector<l1t::Jet>> l1tJetHandle;
    edm::Handle<std::vector<reco::Vertex> >  vertexes;

    iEvent.getByToken(this -> _tauTag,   tauHandle);
    iEvent.getByToken(this -> _triggerObjects, triggerObjects);
    iEvent.getByToken(this -> _triggerBits, triggerBits);
    iEvent.getByToken(this -> _JetTag, jetHandle);
    iEvent.getByToken(this -> _MetTag, metHandle);
    iEvent.getByToken(this -> _l1tJetTag, l1tJetHandle);
    iEvent.getByToken(this -> _VtxTag,vertexes);

    for(BXVector<l1t::Jet>::const_iterator jet = l1tJetHandle -> begin(0); jet != l1tJetHandle -> end(0) ; jet++)
      {
        this -> _l1tPtJet        . push_back(jet -> pt());
        this -> _l1tEtaJet       . push_back(jet -> eta());
        this -> _l1tPhiJet       . push_back(jet -> phi());
        this -> _l1tIsoJet       . push_back(jet -> hwIso());
        //this -> _l1tNTTJet       . push_back(jet -> nTT());
        this -> _l1tQualJet      . push_back(jet -> hwQual());
        //this -> _l1tHasEMJet     . push_back(jet -> hasEM());
        //this -> _l1tIsMergedJet  . push_back(jet -> isMerged());
        this -> _l1tTowerIEtaJet . push_back(jet -> towerIEta());
        this -> _l1tTowerIPhiJet . push_back(jet -> towerIPhi());
        this -> _l1tRawEtJet     . push_back(jet -> rawEt());
        //this -> _l1tIsoEtJet     . push_back(jet -> isoEt());
      }

    edm::Handle< BXVector<l1t::Tau> >  L1TauHandle;
    iEvent.getByToken(_L1TauTag, L1TauHandle);

    for (l1t::TauBxCollection::const_iterator bx0TauIt = L1TauHandle->begin(0); bx0TauIt != L1TauHandle->end(0) ; bx0TauIt++)
      {
        this -> _l1tPt .push_back (bx0TauIt->pt());
        this -> _l1tEta .push_back (bx0TauIt->eta());
        this -> _l1tPhi .push_back (bx0TauIt->phi());
        this -> _l1tIso .push_back (bx0TauIt->hwIso());
        this -> _l1tQual .push_back (bx0TauIt->hwQual());
      }

    for(UInt_t iTau = 0 ; iTau < tauHandle->size() ; ++iTau)
      {
        const pat::TauRef tau = (*tauHandle)[iTau] ;
        this -> _tauPt.push_back( tau -> pt() );
        this -> _tauEta.push_back( tau -> eta() );
        this -> _tauPhi.push_back( tau -> phi() );
        this -> _tauCharge.push_back( tau -> charge() );
        this -> _tauDecayMode.push_back( tau -> decayMode() );
      }

    this -> _Nvtx = vertexes->size();

    this -> _tauTriggerBits = this -> _tauTriggerBitSet.to_ulong();

    const edm::View<pat::Jet>* jets = jetHandle.product();
    //edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
    //eSetup.get<JetCorrectionsRecord>().get("AK4PFchs",JetCorParColl); 
    //JetCorrectorParameters const & JetCorPar = (*JetCorParColl)["Uncertainty"];
    //JetCorrectionUncertainty jecUnc (JetCorPar);
    //_numberOfJets = FillJet(jets,iEvent, &jecUnc);
    _numberOfJets = FillJet(jets,iEvent);

    const edm::View<pat::MET>* mets = metHandle.product();

    for(edm::View<pat::MET>::const_iterator imet = mets->begin(); imet!=mets->end();++imet)
    {
      this -> _PFMET_pt = imet->corPt();
      this -> _PFMET_phi = imet->corPhi();
      this -> _PFMET_px = imet->corPx();
      this -> _PFMET_py = imet->corPy();
      this -> _PFMET_sumEt = imet->corSumEt();

      this -> _CaloMET_pt = imet->caloMETPt();
      this -> _CaloMET_phi = imet->caloMETPhi();
      this -> _CaloMET_px = -1;
      this -> _CaloMET_py = -1;
      this -> _CaloMET_sumEt = imet->caloMETSumEt();
    }


    this -> _tree -> Fill();

  }

  bool Ntuplizer_noTagAndProbe_multipleTaus::hasFilters(const pat::TriggerObjectStandAlone&  obj , const std::vector<std::string>& filtersToLookFor) {

    const std::vector<std::string>& eventLabels = obj.filterLabels();
    for (const std::string& filter : filtersToLookFor)
      {
        //Looking for matching filters
        bool found = false;
        for (const std::string& label : eventLabels)
          {
      if (label == filter)
              {
          found = true;
              }
          }
        if(!found) return false;
      }

    return true;
  }

  int Ntuplizer_noTagAndProbe_multipleTaus::FillJet(const edm::View<pat::Jet> *jets, const edm::Event& event){
    int nJets=0;
    vector <pair<float, int>> softLeptInJet; // pt, idx
    for(edm::View<pat::Jet>::const_iterator ijet = jets->begin(); ijet!=jets->end();++ijet){
      nJets++;
      _jets_px.push_back( (float) ijet->px());
      _jets_py.push_back( (float) ijet->py());
      _jets_pz.push_back( (float) ijet->pz());
      _jets_e.push_back( (float) ijet->energy());    
      _jets_mT.push_back( (float) ijet->mt());
      _jets_Flavour.push_back(ijet->partonFlavour());
      _jets_HadronFlavour.push_back(ijet->hadronFlavour());
      _jets_PUJetID.push_back(ijet->userFloat("pileupJetId:fullDiscriminant"));
      _jets_PUJetIDupdated.push_back(ijet->hasUserFloat("pileupJetIdUpdated:fullDiscriminant") ? ijet->userFloat("pileupJetIdUpdated:fullDiscriminant") : -999);
      // float vtxPx = ijet->userFloat ("vtxPx");
      // float vtxPy = ijet->userFloat ("vtxPy");
      // _jets_vtxPt.  push_back(TMath::Sqrt(vtxPx*vtxPx + vtxPy*vtxPy));
      // _jets_vtxMass.push_back(ijet->userFloat("vtxMass"));
      // _jets_vtx3dL. push_back(ijet->userFloat("vtx3DVal"));
      // _jets_vtxNtrk.push_back(ijet->userFloat("vtxNtracks"));
      // _jets_vtx3deL.push_back(ijet->userFloat("vtx3DSig"));

      _bdiscr.push_back(ijet->bDiscriminator("pfJetProbabilityBJetTags"));
      _bdiscr2.push_back(ijet->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"));
      _bdiscr3.push_back(ijet->bDiscriminator("pfCombinedMVAV2BJetTags"));

  
      //PF jet ID
      float NHF = ijet->neutralHadronEnergyFraction();
      float NEMF = ijet->neutralEmEnergyFraction();
      float CHF = ijet->chargedHadronEnergyFraction();
      float MUF = ijet->muonEnergyFraction();
      float CEMF = ijet->chargedEmEnergyFraction();
      int NumNeutralParticles =ijet->neutralMultiplicity();
      int chargedMult = ijet->chargedMultiplicity();
      int NumConst = ijet->chargedMultiplicity()+NumNeutralParticles;
      float CHM = ijet->chargedMultiplicity();
      float absjeta = fabs(ijet->eta());

      _jets_chEmEF .push_back(CEMF);  
      _jets_chHEF  .push_back(CHF); 
      _jets_nEmEF  .push_back(NEMF);
      _jets_nHEF   .push_back(NHF);
      _jets_chMult .push_back(chargedMult);  
      _jets_neMult .push_back(NumNeutralParticles);  
      _jets_MUF    .push_back(MUF);  

      int jetid=0; 
      bool looseJetID = false;
      bool tightJetID = false;
      bool tightLepVetoJetID = false;

      if (absjeta <= 2.7)
        {
    looseJetID = ( (NHF<0.99 && NEMF<0.99 && NumConst>1) && ((absjeta<=2.4 && CHF>0 && CHM>0 && CEMF<0.99) || absjeta>2.4) );
    tightJetID = ( (NHF<0.90 && NEMF<0.90 && NumConst>1) && ((absjeta<=2.4 && CHF>0 && CHM>0 && CEMF<0.99) || absjeta>2.4) );
    tightLepVetoJetID = ( (NHF<0.90 && NEMF<0.90 && NumConst>1 && MUF<0.8) && ((absjeta<=2.4 && CHF>0 && CHM>0 && CEMF<0.90) || absjeta>2.4) );
        }
      else if (absjeta <= 3.0)
        {
    looseJetID = (NEMF<0.90 && NumNeutralParticles>2 ) ;
    tightJetID = looseJetID;
        }
      else
        {
    looseJetID = (NEMF<0.90 && NumNeutralParticles>10 );
    tightJetID = looseJetID;   
        }
      if (looseJetID) ++jetid;
      if (tightJetID) ++jetid;
      if (tightLepVetoJetID) ++jetid;

      _jetID.push_back(jetid);
      float jecFactor = ijet->jecFactor("Uncorrected") ;
      float jetRawPt = jecFactor * ijet->pt();
      //float jetRawPt2 = ijet->pt() / jecFactor; // this is wrong
      _jets_rawPt.push_back ( jetRawPt );
      _jets_area.push_back (ijet->jetArea());
      _jetrawf.push_back(jecFactor);
    
      // loop on jet contituents to retrieve info for b jet regression
      int nDau = ijet -> numberOfDaughters();
      //cout << "JET: " << (ijet - jets->begin()) << " N daught: " << nDau << endl;

      // TLorentzVector vJet (0,0,0,0);
      // vJet.SetPxPyPzE (ijet->px(), ijet->py(), ijet->pz(), ijet->energy());
      // TLorentzVector vDau (0,0,0,0); 
      // TLorentzVector vSum (0,0,0,0); 

      float leadTrackPt = 0.;
      softLeptInJet.clear();
      for (int iDau = 0; iDau < nDau; ++iDau)
        {
    // pdg id for packed pf candidates meaning is:
    // the particle charge and pdgId: 11, 13, 22 for ele/mu/gamma, 211 for charged hadrons, 130 for neutral hadrons, 1 and 2 for hadronic and em particles in HF. 
    const reco::Candidate * dau = ijet->daughter(iDau);
    if (abs(dau->pdgId()) == 11 || abs(dau->pdgId()) == 13)
      {
        softLeptInJet.push_back( make_pair(dau->pt(), iDau) );
      }

    if (dau->charge() != 0 ) // tracks -> charged
      {
        float ptBuf = dau->pt();
        if (ptBuf > leadTrackPt) leadTrackPt = ptBuf;
      }
    // vDau.SetPxPyPzE (dau->px(), dau->py(), dau->pz(), dau->energy());
    // vSum += vDau;
    // cout << " - " << iDau << " pdg: " << dau->pdgId() << " pt: " << dau->pt() << " charge = " << dau->charge() << endl; 
        }

      //cout << " ## LEAD TRACK PT = " << leadTrackPt << endl;
      //cout << " ## jet eta: " << ijet->eta() << endl;
      _jets_leadTrackPt.push_back(leadTrackPt);
      float leptonPtRel = -1.;
      float leptonPt = -1.;
      float leptonDeltaR = -1.;
      int softLeptIdx = -1;
      if (softLeptInJet.size() > 0)
        {
    sort(softLeptInJet.begin(), softLeptInJet.end());
    softLeptIdx = softLeptInJet.back().second;
        }
      if (softLeptIdx >= 0)
        {
    const reco::Candidate * dau = ijet->daughter(softLeptIdx);
    leptonPtRel = dau->pt() / ijet->pt() ;
    leptonPt = dau->pt() ;
    leptonDeltaR = deltaR(*dau, *ijet) ;
        }
      _jets_leptonPtRel .push_back (leptonPtRel);
      _jets_leptonPt    .push_back (leptonPt);
      _jets_leptonDeltaR.push_back (leptonDeltaR);

      //cout << "     --> jet pt, eta, phi: " << vJet.Pt() << " " << vJet.Eta() << " " << vJet.Phi() << endl;
      //cout << "     --> sum pt, eta, phi: " << vSum.Pt() << " " << vSum.Eta() << " " << vSum.Phi() << endl;
      //if (abs(ijet->hadronFlavour()) == 5 ) cout << "     ------------ THIS WAS A B JET ------------" << endl;
      //cout << "RAW pt: " << jetRawPt << " | " << jetRawPt2 << " --> " << vSum.Pt() << endl;
      //jecUnc->setJetEta(ijet->eta());
      //jecUnc->setJetPt(ijet->pt()); // here you must use the CORRECTED jet pt
      //_jets_jecUnc.push_back(jecUnc->getUncertainty(true));
      _jets_jecUnc.push_back(0.);
    }

    return nJets;
  }


  #include <FWCore/Framework/interface/MakerMacros.h>
  DEFINE_FWK_MODULE(Ntuplizer_noTagAndProbe_multipleTaus);

  #endif //NTUPLIZER_NOTAGANDPROBE_MULTIPLETAUS_H
