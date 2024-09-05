import ROOT

# global parameters
intLumi        = 5.0e+06 #in pb-1
#intLumi        = 1e6
ana_tex        = 'e^{+}e^{-} #rightarrow l^{+}l^{-} + H + H'
delphesVersion = '3.4.2'
energy         = 365.0
collider       = 'FCC-ee'
inputDir       = 'iDM/finalNoCut/'
#inputDir       = '/eos/user/n/nnasser/FCC/iDMprod/Analysis/final_365/'
formats        = ['png','pdf']
yaxis          = ['lin','log']
stacksig       = ['nostack']
#outdir         = 'iDM/plotsNoCut/'
outdir         = '/eos/user/n/nnasser/FCC/iDMprod/Analysis/plotsNoCut/'
plotStatUnc    = True

###If scaleSig=0 or scaleBack=0, we don't apply any additional scaling, on top of the normalization to cross section and integrated luminosity, as defined in finalSel.py
###If scaleSig or scaleBack is not defined, plots will be normalized to 1
scaleSig       = 1.
#scaleBack      = 0.
#splitLeg       = True
#legendCoord = [0.45,0.65,0.92,0.9]

variables = ['n_seljets','n_photons',
             'mZ','mZzoom','ptZ','mZrecoil',
             'photon1_pt','photon1_eta','photon1_e',
             'lep1_pt','lep1_eta','lep1_e','lep1_charge',
             'lep2_pt','lep2_eta','lep2_e','lep2_charge',
             'lep_chargeprod',
             'jet1_pt','jet1_eta','jet1_e',
             'MET_e','MET_pt',
             'pZ','pzZ','eZ','povereZ','costhetaZ',
             'cosDphiLep','cosThetaStar','cosThetaR',
             #'bdt_output'
]

rebin = [1,1,
         1,1,1,1,
         1,1,1,
         1,1,1,1,
         1,1,1,1,
         1,
         1,1,1,
         1,1,
         1,1,1,1,1,
         1,1,1,
        # 1
]# uniform rebin per variable (optional)

###Dictonnary with the analysis name as a key, and the list of selections to be plotted for this analysis. The name of the selections should be the same than in the final selection
selections = {}
#selections['Zee']   = ["TwoEle","TwoEleVetoObj","TwoEleLepCuts", "TwoElePoverE"]
#selections['Zmumu']   = ["TwoMu","TwoMuVetoObj","TwoMuLepCuts", "TwoMuPoverE"]
selections['iDM_BP1'] = ["TwoMu"]
#selections['iDM_BP2'] = ["TwoMu"]
#selections['iDM_BP7'] = ["TwoMu"]
#selections['iDM_BP10'] = ["TwoMu"]

extralabel = {}
extralabel['TwoEle'] = "Selection: N_{e} = 2, |p_{z}^{ee}|<70 GeV, M_{ee}<120 GeV, MET p_{T}>5 GeV"
extralabel['TwoEleVetoObj'] = "Selection: N_{e} = 2, N_{jet}<1, no other lep or #gamma"
extralabel['TwoEleLepCuts'] = "Selection: N_{e} = 2, p^{e}_{T}<80,60 GeV"
extralabel['TwoElePoverE'] = "Selection: N_{e} = 2, p(ee)/E(ee)>0.1"
extralabel['TwoMu'] = "Selection: N_{#mu} = 2,  |p_{z}^{#mu#mu}|<70 GeV, M_{#mu#mu}<120 GeV, MET p_{T}>5 GeV"
extralabel['TwoMuVetoObj'] = "Selection: N_{#mu} = 2, N_{jet}<1, no other lep or #gamma"
extralabel['TwoMuLepCuts'] = "Selection: N_{#mu} = 2, p^{#mu}_{T}<80,60 GeV"
extralabel['TwoMuPoverE'] = "Selection: N_{#mu} = 2, p(#mu#mu)/E(#mu#mu)>0.1"


colors = {}
#colors['All Bkg'] = ROOT.kBlack
colors['nunuH'] = ROOT.kRed
colors['llH'] = ROOT.kRed+2
#colors['mumuH'] = ROOT.kRed+4
#colors['tautauH'] = ROOT.kRed-2
colors['tt'] = ROOT.kRed-2 #####
#colors['qqH'] = ROOT.kRed-4
colors['qq'] = ROOT.kRed-4 #####
colors['eem30'] = ROOT.kViolet
colors['tautau'] = ROOT.kViolet-1
colors['mumu'] = ROOT.kViolet+1
colors['WW'] = ROOT.kBlue+1
colors['ZZ'] = ROOT.kGreen+2
colors['iDM1'] = ROOT.kBlack
colors['iDM2'] = ROOT.kGray+1
colors['iDM6'] = ROOT.kGray-1
colors['iDM8'] = ROOT.kGray

plots = {}
plots['iDM_BP1'] = {
    'signal':{
        'iDM1':['e365_bp1_h2h2ll','e365_bp1_h2h2llvv'],
        #'iDM2':['e365_bp2_h2h2ll','e365_bp2_h2h2llvv'],
        #'iDM6':['e365_bp6_h2h2ll','e365_bp6_h2h2llvv'],
        #'iDM8':['e365_bp8_h2h2ll','e365_bp8_h2h2llvv'],
    },
    'backgrounds':{
        #'eem30':['wzp6_ee_ee_Mee_30_150_ecm365'],
        'mumu':['wzp6_ee_mumu_ecm365'],
        'tautau':['wzp6_ee_tautau_ecm365'],
        'WW':['p8_ee_WW_ecm365'],
        'ZZ':['p8_ee_ZZ_ecm365'],
        'tt':['p8_ee_tt_ecm365'],
        'qq':['wzp6_ee_qq_ecm365'],

        #'llH':['wzp6_ee_eeH_ecm365','wzp6_ee_mumuH_ecm365','wzp6_ee_tautauH_ecm365'],
        #'mumuH':['wzp6_ee_mumuH_ecm240'], #was commented out
        #'tautauH':['wzp6_ee_tautauH_ecm240'], #was commented out
        #'qqH':['wzp6_ee_qqH_ecm240'],
        #'nunuH':['wzp6_ee_nunuH_ecm240'],
    }
}
'''
plots['Zmumu'] = {
    'signal':{
        'iDM1':['e365_bp1_h2h2ll','e365_bp1_h2h2llvv'],
        'iDM2':['e365_bp2_h2h2ll','e365_bp2_h2h2llvv'],
        #'iDM3':['e365_bp3_h2h2ll','e365_bp3_h2h2llvv'],
        #'iDM4':['e365_bp4_h2h2ll','e365_bp4_h2h2llvv'],
        #'iDM5':['e365_bp5_h2h2ll','e365_bp5_h2h2llvv'],
        'iDM7':['e365_bp7_h2h2ll','e365_bp7_h2h2llvv'],
        #'iDM7':['e365_bp7_h2h2ll','e365_bp7_h2h2llvv'],
        'iDM10':['e365_bp10_h2h2ll','e365_bp10_h2h2llvv'], 
    },
    'backgrounds':{
        'mumu':['wzp6_ee_mumu_ecm365'],
        'tautau':['wzp6_ee_tautau_ecm365'],
        'WW':['p8_ee_WW_ecm365'],
        'ZZ':['p8_ee_ZZ_ecm365'],
        #'All Bkg': ['p8_ee_ZZ_ecm365', 'p8_ee_WW_ecm365', 'wzp6_ee_mumu_ecm365', 'wzp6_ee_tautau_ecm365'],
       
    }
}
'''

#plots['Zee']= plots['Zmumu']

#plots['Zmumu'] = plots['Zee']

legend = {}
legend['All Bkg'] = 'All Backgrounds'
legend['nunuH'] = '#nu#nuH'
legend['llH'] = 'llH'
#legend['mumuH'] = '#mu#muH'
#legend['tautauH'] = '#tau#tauH'
#legend['qqH'] = 'qqH'
legend['eem30'] = 'ee30-150GeV'
legend['mumu'] = '#mu#mu'
legend['tautau'] = '#tau#tau'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['tt'] = 'tt'
legend['qq'] = 'qq'
legend['iDM1'] = 'iDM BP1'
legend['iDM2'] = 'iDM BP2'
legend['iDM7'] = 'iDM BP7'
legend['iDM10'] = 'iDM BP10'
