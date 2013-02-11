calfile = '/home/pf9/NOM_calibrate_d9334_2012_10_30.cal'
vanfile = '/SNS/NOM/IPTS-7065/0/9335/NeXus/NOM_9335_event.nxs'
bakfile = '/SNS/NOM/IPTS-7065/0/9333/NeXus/NOM_9333_event.nxs'

focus_args={'CalFileName':calfile, #'CropWavelengthMin':0.1,'RemovePromptPulseWidth':50,
'Params':'-0.0004','ResampleX':-3000,#'CompressTolerance':0.,
'PrimaryFlightPath':19.5,'SpectrumIDs':'1,2,3,4,5,6','L2':'2,2,2,2,2,2','Polar':'15,31,67,122,154,7','Azimuthal':'0,0,0,0,0,0'}

Load(Filename=bakfile,OutputWorkspace='NOM_9333',Precount=True)
AlignAndFocusPowder(InputWorkspace='NOM_9333',OutputWorkspace='NOM_9333',**focus_args)
#CompressEvents(InputWorkspace='NOM_9333',OutputWorkspace='NOM_9333',Tolerance='0.01')
NormaliseByCurrent(InputWorkspace='NOM_9333',OutputWorkspace='NOM_9333')

Load(Filename=vanfile,OutputWorkspace='NOM_9335',Precount='1')
AlignAndFocusPowder(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',PreserveEvents=True,**focus_args)
#CompressEvents(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Tolerance='0.01')
NormaliseByCurrent(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335')

Minus(LHSWorkspace='NOM_9335',RHSWorkspace='NOM_9333',OutputWorkspace='minus')
SortEvents(InputWorkspace="minus")

#Minus(LHSWorkspace='NOM_9335',RHSWorkspace='NOM_9333',OutputWorkspace='NOM_9335')
#ConvertUnits(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Target='TOF')
#CompressEvents(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Tolerance='0.01')

ConvertUnits(InputWorkspace='NOM_9333',OutputWorkspace='NOM_9333',Target='dSpacing')
ConvertUnits(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Target='dSpacing')
ConvertUnits(InputWorkspace='minus',     OutputWorkspace='minus',     Target='dSpacing')
#StripVanadiumPeaks(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',BackgroundType='Quadratic',PeakPositionTolerance='0.050000000000000003')
#ConvertUnits(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Target='TOF')
#FFTSmooth(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Filter='Butterworth',Params='20,2',IgnoreXBins='1',AllSpectra='1')
#MultipleScatteringCylinderAbsorption(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335')
#SetUncertainties(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335')
#ConvertUnits(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Target='TOF')
ConvertUnits(InputWorkspace='NOM_9335',OutputWorkspace='NOM_9335',Target='dSpacing')

CreateSingleValuedWorkspace(OutputWorkspace="factor", DataValue=3600., ErrorValue=0.) # should be 3600000000
for i in range(6):
    filename = "/SNS/NOM/IPTS-4480/shared/norm_Bank00%d.dat&end" % i
    wksp = "norm_%d" % (i+1)
    LoadAscii(Filename=filename, OutputWorkspace=wksp, Unit="dSpacing")
    Multiply(LHSWorkspace=wksp, RHSWorkspace="factor", OutputWorkspace=wksp)
    plotSpectrum(["NOM_9335", "NOM_9333", "minus"], i)
