#ifndef TAUTAGANDPROBEFILTERRUN3_H
#define TAUTAGANDPROBEFILTERRUN3_H

#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <FWCore/Framework/interface/Frameworkfwd.h>
#include <FWCore/Framework/interface/Event.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include <FWCore/MessageLogger/interface/MessageLogger.h>
#include <FWCore/Utilities/interface/InputTag.h>
#include <DataFormats/PatCandidates/interface/Tau.h>
#include <DataFormats/PatCandidates/interface/Muon.h>
#include <DataFormats/PatCandidates/interface/MET.h>
#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/PatCandidates/interface/Electron.h>
#include <DataFormats/PatCandidates/interface/CompositeCandidate.h>

#include <iostream>
#include <utility>
#include <vector>

using namespace edm;
using namespace std;
// using namespace reco;


class TauTagAndProbeFilterRun3 : public edm::EDFilter {

    public:
        TauTagAndProbeFilterRun3(const edm::ParameterSet &);
        ~TauTagAndProbeFilterRun3();

    private:
        bool filter(edm::Event &, edm::EventSetup const&);

        float ComputeMT(math::XYZTLorentzVector visP4, const pat::MET& met);

        EDGetTokenT<pat::TauRefVector>   _tausTag;
        EDGetTokenT<pat::MuonRefVector>  _muonsTag;
        EDGetTokenT<pat::METCollection>  _metTag;
        bool _useWMassCuts;
        bool _useZMassCuts;
        EDGetTokenT<edm::View<pat::Electron> >  _electronsTag;
        EDGetTokenT<pat::JetRefVector>  _bjetsTag;
};

TauTagAndProbeFilterRun3::TauTagAndProbeFilterRun3(const edm::ParameterSet & iConfig) :
_tausTag  (consumes<pat::TauRefVector>  (iConfig.getParameter<InputTag>("taus"))),
_muonsTag (consumes<pat::MuonRefVector> (iConfig.getParameter<InputTag>("muons"))),
_metTag   (consumes<pat::METCollection> (iConfig.getParameter<InputTag>("met"))),
_electronsTag (consumes<edm::View<pat::Electron>> (iConfig.getParameter<edm::InputTag>("electrons"))),
_bjetsTag  (consumes<pat::JetRefVector>  (iConfig.getParameter<InputTag>("bjets")))
{
    produces <pat::TauRefVector>  (); // probe
    produces <pat::MuonRefVector> (); // tag
    _useWMassCuts = iConfig.getParameter<bool>("useWMassCuts");
    _useZMassCuts = iConfig.getParameter<bool>("useZMassCuts");
}

TauTagAndProbeFilterRun3::~TauTagAndProbeFilterRun3()
{}

bool TauTagAndProbeFilterRun3::filter(edm::Event & iEvent, edm::EventSetup const& iSetup)
{

    std::unique_ptr<pat::MuonRefVector> resultMuon ( new pat::MuonRefVector );
    std::unique_ptr<pat::TauRefVector>  resultTau  ( new pat::TauRefVector  );  

    Handle<edm::View<pat::Electron> > electrons;
    iEvent.getByToken(_electronsTag, electrons);

    // veto events with loose electrons (acytually not super sure that wp80 is loose)
    for(const auto& ele : iEvent.get(_electronsTag) )
    {
        int isLooseID = ele.electronID("mvaEleID-Fall17-iso-V2-wp80");
        if(isLooseID && ele.p4().Pt()>10 && fabs(ele.p4().Eta())<2.5) return false;
    }

    // ---------------------   search for the tag in the event --------------------
    Handle<pat::MuonRefVector> muonHandle;
    iEvent.getByToken (_muonsTag, muonHandle);

    const pat::MuonRef mu = (*muonHandle)[0] ;

    //---------------------   get the met for mt computation etc. -----------------
    Handle<pat::METCollection> metHandle;
    iEvent.getByToken (_metTag, metHandle);
    const pat::MET& met = (*metHandle)[0];

    float mt = ComputeMT (mu->p4(), met);

    if (mt >= 30 && _useWMassCuts) return false; // reject W+jets


    // ------------------- get Taus -------------------------------
    Handle<pat::TauRefVector> tauHandle;
    iEvent.getByToken (_tausTag, tauHandle);
    if (tauHandle->size() < 1) return false;

    vector<pair<float, int>> tausIdxPtVec;
    for (uint itau = 0; itau < tauHandle->size(); ++itau)
    {
        const pat::TauRef tau = (*tauHandle)[itau] ;
        math::XYZTLorentzVector pSum = mu->p4() + tau->p4();
        if (_useZMassCuts && (pSum.mass() <= 40 || pSum.mass() >= 80)) continue; // visible mass in (40, 80)
        if (deltaR(*tau, *mu) < 0.5) continue;

        // store iso against jet and idx 
        float isoMVA = tau->tauID("byDeepTau2017v2p1VSjetraw");
        tausIdxPtVec.push_back(make_pair(isoMVA, itau));
    }

    pat::TauRef tau;
    if (tausIdxPtVec.size() == 0) return false; // no tau found
    if (tausIdxPtVec.size() > 1) sort(tausIdxPtVec.begin(), tausIdxPtVec.end()); // sort if multiple taus
    int tauIdx = tausIdxPtVec.back().second; // min iso --> max MVA score
    tau = (*tauHandle)[tauIdx]; // store most isolated tau that wil be used by the Ntuplizer


    // ----------------- b-jets veto ---------------------
    Handle<pat::JetRefVector> bjetHandle;
    iEvent.getByToken (_bjetsTag, bjetHandle);

    for(unsigned int ijet = 0; ijet < bjetHandle->size(); ijet++)
    {
        const pat::JetRef bjet = (*bjetHandle)[ijet];
        if( deltaR(*mu,*bjet)>0.5 && deltaR(*tau,*bjet)>0.5 ) return false;
    }

    // store taus and muons to be used by the Ntuplizer
    resultTau->push_back (tau);
    resultMuon->push_back (mu);
    iEvent.put(std::move(resultMuon));
    iEvent.put(std::move(resultTau));

    return true;
}

float TauTagAndProbeFilterRun3::ComputeMT (math::XYZTLorentzVector visP4, const pat::MET& met)
{
  math::XYZTLorentzVector METP4 (met.pt()*TMath::Cos(met.phi()), met.pt()*TMath::Sin(met.phi()), 0, met.pt());
  float scalSum = met.pt() + visP4.pt();

  math::XYZTLorentzVector vecSum (visP4);
  vecSum += METP4;
  float vecSumPt = vecSum.pt();
  return sqrt (scalSum*scalSum - vecSumPt*vecSumPt);
}

#include <FWCore/Framework/interface/MakerMacros.h>
DEFINE_FWK_MODULE(TauTagAndProbeFilterRun3);

#endif
