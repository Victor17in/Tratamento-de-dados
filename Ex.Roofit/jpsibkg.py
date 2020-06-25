import ROOT 


f = ROOT.TFile("DataSet_lowstat.root")
dataset= f.Get("data")
mass = ROOT.RooRealVar("mass","#mu^{+}#mu^{-} invariant mass",2.,6.,"GeV")
mean = ROOT.RooRealVar("mean","the mean of the crystal ball",3.1,2.8,3.2)
sigma = ROOT.RooRealVar("sigma","the width of the crystal ball", 0.3,0.0001,1.)
alpha = ROOT.RooRealVar("alpha","the alpha of the crystal ball",1.5,-5.,5.)
n = ROOT.RooRealVar("n","the n of crystal ball",1.5,0.5,5.)

#RooCBShape signalModel("signal","signal pdf",massa,mean,sigma,alpha,n)
signalModel = ROOT.RooCBShape("signalModel","The Jpsi Crystall Ball",mass,mean,sigma,alpha,n)

#background

#Background parametrization: just a polynomial

a1 = ROOT.RooRealVar("a1","The a1 of background",-0.7,-2.,2.)

a2 = ROOT.RooRealVar("a2","The a2 of background",0.3,-2.,2.)

a3 = ROOT.RooRealVar("a3","The a3 of background",-0.03,-2.,2.)

backgroundPDF = ROOT.RooChebychev("backgroundPDF","The background PDF",mass,ROOT.RooArgList(a1,a2,a3))

#--- Construct signal+background PDF ---
nsig = ROOT.RooRealVar("nsig","#signal events",200,0.,10000);
nbkg = ROOT.RooRealVar("nbkg","#background events",800,0.,10000);
model = ROOT.RooAddPdf("model","g+a",ROOT.RooArgList(signalModel,backgroundPDF),ROOT.RooArgList(nsig,nbkg));

#RooRealVar massapsi("massapsi","massa Invariante psi",2.,4.,"GeV")
#RooRealVar meanpsi("meanpsi","the mean psi od the crystall ball",3.6,3.0,3.8)

#RooCBShape signalpsi("signalpsi","signal pdf",massapsi,meanpsi,sigma,alpha,n)

#RooAddPdf model("model","j+psi", signalModel, signalpsi)

model.fitTo(dataset)
massframe = mass.frame()
#RooPlot* massframe = mass.frame()
dataset.plotOn(massframe)
model.plotOn(massframe)
c1 = ROOT.TCanvas()
massframe.Draw()

#signalModel.fitTo(dataset)
#xframe = mass.frame()
#dataset.plotOn(xframe)
#signalModel.plotOn(xframe)
#c1 = ROOT.TCanvas()
#xframe.Draw()
c1.SaveAs("jpsibkg.png")


