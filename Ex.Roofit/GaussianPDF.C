#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif

#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooAddPdf.h"
#include "RooGaussian.h"
#include "RooChebychev.h"
#include "RooCBShape.h"
#include "RooPlot.h"
#include "RooMCStudy.h"
#include "RooFitResult.h"
#include "RooThresholdCategory.h"
#include "RooBinningCategory.h"
#include "RooWorkspace.h"
#include "RooArgList.h"

#include "TROOT.h"
#include "TStyle.h"
#include "TDirectory.h"
#include "TCanvas.h"
#include "TFile.h"
#include "TAxis.h"
#include "TGraphAsymmErrors.h"
#include "TPaveLabel.h"
#include "TFolder.h"

//#include "tdrstyle.C"

using namespace RooFit;

void GaussianPDF(){

  //setTDRStyle();

  //Declare variables x, mean, sigma, 
  RooRealVar x("x","x",-10,10);
  RooRealVar mean("mean","mean of gaussian", 1,-10,10);
  RooRealVar sigma("sigma","width of gaussian",1,0.1,10);
  //Buil gaussian p.d.f. in term of x, mean and sigma
  RooGaussian gauss("gauss", "gaussian PDF", x,mean,sigma);
  //create an empty plot frame in x
  RooPlot* xframe = x.frame("Gaussian p.d.f");
  
  // Plot Model on frame
  gauss.plotOn(xframe);

  //Draw frame on canvas
  xframe->Draw();

}


