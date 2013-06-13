# Load each file
NOM_group = CreateGroupingWorkspace(InstrumentName="NOMAD", GroupDetectorsBy="All")
names = ["NOM14526", "NOM14527", "NOM14528", "NOM14529"]
for name in names:
  preserveEvents = (not name in ["NOM14528", "NOM14529"])
  Load(name, OutputWorkspace=name)

  # Reduce each dataset to a single spectrum
  nom = AlignAndFocusPowder(name, CalFileName="/SNS/NOM/IPTS-8607/shared/NOM_calibrate_d14526_2013_05_18.cal", ResampleX=-3000,
                            RemovePromptPulseWidth=50, PreserveEvents=preserveEvents,
                            DMin=.13, Dmax=31.42, Tmin=300, Tmax=16666.67,
                            PrimaryFlightPath=19.5, SpectrumIDs=1, L2=2, Polar=90, Azimuthal=0,
			    OutputWorkspace=name)
  if preserveEvents:
    CompressEvents(name, OutputWorkspace=name, Tolerance=.01)
  NormaliseByCurrent(name, OutputWorkspace=name)

#Special work for the vanadium
NOM14528 = mtd["NOM14528"] - mtd["NOM14529"]
NOM14528 = ConvertUnits(NOM14528, Target="dSpacing", EMode="Elastic")
NOM14528 = StripVanadiumPeaks(NOM14528, FWHM=7, PeakPositionTolerance=.05,
                                          BackgroundType="Quadratic", HighBackground=True)
NOM14528 = ConvertUnits(NOM14528, Target="TOF")
NOM14528 = FFTSmooth(NOM14528, Filter="Butterworth",
                            Params="20,2",IgnoreXBins=True,AllSpectra=True)
NOM14528 = MultipleScatteringCylinderAbsorption(NOM14528, # numbers for vanadium
                                                       AttenuationXSection=2.8, ScatteringXSection=5.1,
                                                       SampleNumberDensity=0.0721, CylinderSampleRadius=.3175)
NOM14528 = SetUncertainties(NOM14528)
NOM14528 = ConvertUnits(NOM14528, Target="TOF")

for name in names:
  ConvertUnits(name, OutputWorkspace=name, Target="MomentumTransfer", EMode="Elastic")
  Rebin(name, OutputWorkspace=name, Params=.02, PreserveEvents=True)
soq = (mtd["NOM14526"] - mtd["NOM14527"])/mtd["NOM14528"]

# Get the high-Q function to asymptote to 1
Fit(InputWorkspace="soq", Function="name=FlatBackground,A0=1", 
StartX=35, EndX=48, CreateOutput=True)
print "high-Q asymptote:", mtd["soq_Parameters"].row(0)['Value']

single = CreateSingleValuedWorkspace(DataValue=mtd["soq_Parameters"].row(0)['Value'], ErrorValue=0)
Divide(LHSWorkspace="soq", RHSWorkspace= "single", OutputWorkspace="soq")

gr = PDFFourierTransform("soq", Qmin=.5, Qmax=48, PDFType="G(r)=4pi*r[rho(r)-rho_0]", DeltaR=.02, RMax=20)
