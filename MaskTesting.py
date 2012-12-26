LoadEmptyInstrument(Filename="/home/pf9/code/mantid/Code/Mantid/instrument/MAPS_Definition.xml",
                    OutputWorkspace="__empty_MAPS")
LoadRaw(Filename="/home/pf9/code/systemtests/Data/MAP17186.raw",
        OutputWorkspace="MAP17186.raw")
#AddSampleLog(Workspace="MAP17186.raw", 
#             LogName="Filename",
#             LogText="/home/pf9/code/systemtests/Data/MAP17186.raw")
NormaliseToMonitor(InputWorkspace="MAP17186.raw",
                   OutputWorkspace="17186.spe-white",
                   MonitorSpectrum=41473,
                   IntegrationRangeMin=1000,
                   IntegrationRangeMax=2000,
                   IncludePartialBins=True)
AddSampleLog(Workspace="17186.spe-white",
             LogName="DirectInelasticReductionNormalisedBy",
             LogText="monitor-1")
ConvertUnits(InputWorkspace="17186.spe-white",
             OutputWorkspace="17186.spe-white",
             Target="Energy")
Rebin(InputWorkspace="17186.spe-white",
      OutputWorkspace="17186.spe-white",
      Params=(20,560,300))
CreateSingleValuedWorkspace(OutputWorkspace="__tmp_binary_operation_double",
                            DataValue=1000)
Multiply(LHSWorkspace="17186.spe-white",
         RHSWorkspace="__tmp_binary_operation_double",
         OutputWorkspace="17186.spe-white")
LoadRaw(Filename="/home/pf9/code/systemtests/Data/MAP17269.raw",
        OutputWorkspace="MAP17269.raw")
AddSampleLog(Workspace="MAP17269.raw",
             LogName="Filename",
             LogText="/home/pf9/code/systemtests/Data/MAP17269.raw")
NormaliseToMonitor(InputWorkspace="MAP17269.raw",
                   OutputWorkspace="MAP17269.raw",
                   MonitorSpectrum=41473,
                   IntegrationRangeMin=1000,
                   IntegrationRangeMax=2000,
                   IncludePartialBins=True)
AddSampleLog(Workspace="MAP17269.raw",
             LogName="DirectInelasticReductionNormalisedBy",
             LogText="monitor-1")
Integration(InputWorkspace="MAP17269.raw",
            OutputWorkspace="background_int",
            RangeLower=12000,
            RangeUpper=18000,
            IncludePartialBins=True)
Integration(InputWorkspace="MAP17269.raw",
            OutputWorkspace="total_counts",
            IncludePartialBins=True)
ConvertUnits(InputWorkspace="background_int",
             OutputWorkspace="background_int",
             Target="Energy")
CreateSingleValuedWorkspace(OutputWorkspace="__tmp_binary_operation_double",
                            DataValue=170160000)
Multiply(LHSWorkspace="background_int",
         RHSWorkspace="__tmp_binary_operation_double",
         OutputWorkspace="background_int")

Divide(LHSWorkspace="background_int",
       RHSWorkspace="17186.spe-white",
       OutputWorkspace="background_int")
FindDetectorsOutsideLimits(InputWorkspace="17186.spe-white",
                           OutputWorkspace="white_masks",
                           HighThreshold=10000000000,
                           LowThreshold=1e-10,
                           EndWorkspaceIndex=17279)
#FindDetectorsOutsideLimits-[Information] 2496 spectra fell outside the given limits.
#spectra1024-1151,2176-2303,3328-3455,4480-4607,5632-5759,6784-6911,7936-8063,9088-9215,10944-11007,11392-11519,12672-13823,16000-16127
MaskDetectors(Workspace="17186.spe-white",
              MaskedWorkspace="white_masks",
              EndWorkspaceIndex=17279)
ExtractMask(InputWorkspace="white_masks",
            OutputWorkspace="mask")
ExtractMask(InputWorkspace="17186.spe-white",
            OutputWorkspace="mask2")

#DeleteWorkspace(Workspace="white_masks")
#RenameWorkspace(InputWorkspace="white_masks", OutputWorkspace="FindDetectorsOutsideLimits")
#########################################
#MedianDetectorTest(InputWorkspace="17186.spe-white",
#                   OutputWorkspace="white_masks",
#                   SignificanceTest=0,
#                   HighThreshold=2,
#                   EndWorkspaceIndex=17279)
#MedianDetectorTest-[Information] Median value with outliers removed = 0.231968
#MedianDetectorTest-[Information] 493 spectra failed the median tests.
#MedianDetectorTest-[Information] 	Number of failures - -1776
#MaskDetectors(Workspace="17186.spe-white",
#              MaskedWorkspace="white_masks",
#              EndWorkspaceIndex=17279)
#MaskDetectors(Workspace="17186.spe-white",
#              MaskedWorkspace="white_masks",
#              EndWorkspaceIndex=17279)
#########################################
