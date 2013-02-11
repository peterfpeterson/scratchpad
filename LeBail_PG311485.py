# Load data
LoadAscii(Filename=r'PG3_11485-1.dat',OutputWorkspace='PG3_11485',Unit='TOF')  
 
# Create input workspaces for Le Bail fit
CreateLeBailFitInput(ReflectionsFile=r'LB4844b1.hkl',
        FullprofParameterFile=r'2011B_HR60b1.irf',
        LatticeConstant='4.1568899999999998',
        InstrumentParameterWorkspace='Bank1InstrumentParameterTable1',
        BraggPeakParameterWorkspace='BraggPeakParameterTable1')
 
# Initial Le Bail fit in calculation mode to see how far the starting parameters are off
LeBailFit(InputWorkspace='PG3_11485',
        OutputWorkspace='PG3_11485_Calculated_0',
        InputParameterWorkspace='Bank1InstrumentParameterTable1',
        OutputParameterWorkspace='TempTable',
        InputHKLWorkspace='BraggPeakParameterTable1',
        OutputPeaksWorkspace='BraggPeakParameterTable2',
        Function='Calculation',
        BackgroundType='Chebyshev',
        BackgroundParameters='0,0,0',   # No background at first 
        UseInputPeakHeights='0',
        PeakRadius='8',
        Minimizer='Levenberg-Marquardt')
 
# Fit the instrumental geometry-related parameters.  Dtt1, Dtt1t, Dtt2, Zero, Zerot, 
# Step 1: Fit single diffraction peaks
FitPowderDiffPeaks(InputWorkspace='PG3_11485',
        OutputWorkspace='Bank1FittedPeaks',
        BraggPeakParameterWorkspace='BraggPeakParameterTable2',
        InstrumentParameterWorkspace='Bank1InstrumentParameterTable1',
        OutputBraggPeakParameterWorkspace='BraggPeakParameterTable2_0',
        OutputBraggPeakParameterDataWorkspace='BraggPeakParameterTable2_P',
        OutputZscoreWorkspace='BraggPeakParameterTable2_Zscore',
        MinTOF='15000',MaxTOF='49387',UseGivenPeakCentreTOF='0',
        MinimumPeakHeight='0.29999999999999999',
        PeaksCorrelated='1',
        MinimumHKL='12,12,12',
        RightMostPeakHKL='2,0,0',
        RightMostPeakLeftBound='46000',
        RightMostPeakRightBound='48000')
 
# Step 2: Refine geometry-related parameters.  Dtt1, Dtt1t, Dtt2, Zero, Zerot, 
RefinePowderInstrumentParameters(InputPeakPositionWorkspace='BraggPeakParameterTable2_P',
        OutputPeakPositionWorkspace='PG3_11485_PeakPositions',
        InputInstrumentParameterWorkspace='Bank1InstrumentParameterTable1',
        OutputInstrumentParameterWorkspace='Bank1InstrumentParameterTable1_01',
        RefinementAlgorithm='OneStepFit')
 
# Create a workspace containing background of diffraction data to fit background polynomial
ProcessBackground(InputWorkspace='PG3_11485',
        OutputWorkspace='PG3_11485_Background',
        Options='SelectBackgroundPoints',
        LowerBound='5053',
        UpperBound='49387',
        BackgroundPoints='5243,8910,11165,12153,13731,15060,16511,17767,19650,21874,23167,24519,36000,44282,49000',
        NoiseTolerance='0.10000000000000001')
 
# Fit background function
Fit(Function='name=Polynomial,n=6,A0=0.558765,A1=-3.36699e-05,A2=-9.89997e-10,A3=2.29598e-13,A4=-1.07727e-17,A5=2.10058e-22,A6=-1.49446e-27',
        InputWorkspace='PG3_11485_Background',
        MaxIterations='1000',
        Minimizer='Levenberg-MarquardtMD',
        CreateOutput='1',
        Output='PG3_11485_Background',
        StartX='5053',EndX='49387')
 
# Use LeBailFit to calculate the diffraction pattern to see whether the refined geometry-related parameters are good as starting value
LeBailFit(InputWorkspace='PG3_11485',
        OutputWorkspace='CalculatedPattern0',
        InputParameterWorkspace='Bank1InstrumentParameterTable1_01',
        OutputParameterWorkspace='Bank1InstrumentParameterTable1_0',
        InputHKLWorkspace='BraggPeakParameterTable1',
        OutputPeaksWorkspace='BraggPeakParameterTable2_0',
        Function='Calculation',
        BackgroundParametersWorkspace='PG3_11485_Background_Parameters',
        UseInputPeakHeights='0',PeakRadius='8',Minimizer='Levenberg-Marquardt')
 
# Use LeBailFit to refine POWGEN's instrument profile parameters by Monte Carlo algorithm
LeBailFit(InputWorkspace='PG3_11485',
        OutputWorkspace='PG3_11485_MC_1000',
        InputParameterWorkspace='Bank1InstrumentParameterTable1_0',
        OutputParameterWorkspace='Bank1InstrumentParameterTable_MC',
        InputHKLWorkspace='BraggPeakParameterTable1',
        OutputPeaksWorkspace='BraggPeakParameterTable3',
        FitRegion='5053,49387',
        Function='MonteCarlo',
        BackgroundParametersWorkspace='PG3_11485_Background_Parameters',
        UseInputPeakHeights='0',
        PeakRadius='8',
        Minimizer='Levenberg-Marquardt',
        Damping='0.90000000000000002',
        NumberMinimizeSteps='1000',
        FitGeometryParameter='1',
        RandomSeed='1000',
        AnnealingTemperature='10',
        DrunkenWalk='1')
