#import mantid
#from mantid.api import simpleapi
abs_info = {'AttenuationXSection':2.8,
            'ScatteringXSection':5.1,
            'SampleNumberDensity':0.0721,
            'CylinderSampleRadius':.3175}
foc_info = {'CalFileName':"/SNS/PG3/2013_1_11A_CAL/PG3_PAC_d11475_2012_11_29.cal",
            'Params':[-0.0004]}

# wavelength = 0.533A
PG3_11476_raw = LoadEventNexus(Filename="PG3_11476_event.nxs")
PG3_11476_raw = AlignAndFocusPowder(InputWorkspace=PG3_11476_raw, **foc_info)
PG3_11476_raw = ConvertUnits(InputWorkspace=PG3_11476_raw, Target="dSpacing", EMode="Elastic")

PG3_11476 = LoadEventNexus(Filename="PG3_11476_event.nxs")
PG3_11476 = Rebin(InputWorkspace=PG3_11476, Params=[10.])
PG3_11476 = ConvertUnits(InputWorkspace=PG3_11476, target="Wavelength", EMode="Elastic")
PG3_11476_abs = CylinderAbsorption(InputWorkspace=PG3_11476,
                                   ExpMethod="Normal", EMode="Elastic",
                                   CylinderSampleHeight=5,
                                   NumberOfWavelengthPoints = 200,
                                   NumberOfSlices=20, NumberOfAnnuli=3,
                                   **abs_info)
PG3_11476_isaw = MultipleScatteringCylinderAbsorption(InputWorkspace=PG3_11476,
                                                      **abs_info)
PG3_11476 /= PG3_11476_abs
PG3_11476 = ConvertUnits(InputWorkspace=PG3_11476, target="TOF", EMode="Elastic")
PG3_11476 = AlignAndFocusPowder(InputWorkspace=PG3_11476, **foc_info)
PG3_11476 = ConvertUnits(InputWorkspace=PG3_11476, Target="dSpacing", EMode="Elastic")

PG3_11476_isaw = ConvertUnits(InputWorkspace=PG3_11476_isaw, target="TOF", EMode="Elastic")
PG3_11476_isaw = AlignAndFocusPowder(InputWorkspace=PG3_11476_isaw, **foc_info)
PG3_11476_isaw = ConvertUnits(InputWorkspace=PG3_11476_isaw, Target="dSpacing", EMode="Elastic")


# wavelength = 4.797A
PG3_11483_raw = LoadEventNexus(Filename="PG3_11483_event.nxs")
PG3_11483_raw = AlignAndFocusPowder(InputWorkspace=PG3_11483_raw, **foc_info)
PG3_11483_raw = ConvertUnits(InputWorkspace=PG3_11483_raw, Target="dSpacing", EMode="Elastic")

PG3_11483 = LoadEventNexus(Filename="PG3_11483_event.nxs")
PG3_11483 = Rebin(InputWorkspace=PG3_11483, Params=[10.])
PG3_11483 = ConvertUnits(InputWorkspace=PG3_11483, target="Wavelength", EMode="Elastic")
PG3_11483_abs = CylinderAbsorption(InputWorkspace=PG3_11483,
                                   ExpMethod="Normal", EMode="Elastic",
                                   CylinderSampleHeight=5,
                                   NumberOfWavelengthPoints = 200,
                                   NumberOfSlices=20, NumberOfAnnuli=3,
                                   **abs_info)
PG3_11483_isaw = MultipleScatteringCylinderAbsorption(InputWorkspace=PG3_11483,
                                                      **abs_info)
PG3_11483 /= PG3_11483_abs
PG3_11483 = ConvertUnits(InputWorkspace=PG3_11483, target="TOF", EMode="Elastic")
PG3_11483 = AlignAndFocusPowder(InputWorkspace=PG3_11483, **foc_info)
PG3_11483 = ConvertUnits(InputWorkspace=PG3_11483, Target="dSpacing", EMode="Elastic")

PG3_11483_isaw = ConvertUnits(InputWorkspace=PG3_11483_isaw, target="TOF", EMode="Elastic")
PG3_11483_isaw = AlignAndFocusPowder(InputWorkspace=PG3_11483_isaw, **foc_info)
PG3_11483_isaw = ConvertUnits(InputWorkspace=PG3_11483_isaw, Target="dSpacing", EMode="Elastic")

# important line from SNSPowderReduction
#vanRun = MultipleScatteringCylinderAbsorption(InputWorkspace=vanRun, OutputWorkspace=vanRun, # numbers for vanadium
#                                              AttenuationXSection=2.8, ScatteringXSection=5.1,
#                                              SampleNumberDensity=0.0721, CylinderSampleRadius=.3175)
