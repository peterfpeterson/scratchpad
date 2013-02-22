######################################################################
#Python Script Generated by GeneratePythonScript Algorithm
######################################################################
LoadAscii(Filename='NOM_10291-5.dat',OutputWorkspace='NOM_10291_Bank5',Unit='TOF')
CreateSingleValuedWorkspace(OutputWorkspace='Background1262',DataValue='1262')
Minus(LHSWorkspace='NOM_10291_Bank5',RHSWorkspace='Background1262',OutputWorkspace='NOM_10291_Bank5')
CreateLeBailFitInput(ReflectionsFile=r'si_bank5.hkl',FullprofParameterFile=r'nom60b5.irf',Bank='5',
                     LatticeConstant='5.4307100000000004',InstrumentParameterWorkspace='Bank5InstrumentParameterTable1',
                     BraggPeakParameterWorkspace='BraggPeakParameterTable1')
LeBailFit(InputWorkspace='NOM_10291_Bank5',OutputWorkspace='PatternWildGuess',
          InputParameterWorkspace='Bank5InstrumentParameterTable1',OutputParameterWorkspace='TempTable',
          InputHKLWorkspace='BraggPeakParameterTable1',OutputPeaksWorkspace='BraggPeakParameterTable2',
          FitRegion='3720,15288',Function='Calculation',UseInputPeakHeights='0',PeakRadius='8',
          Minimizer='Levenberg-Marquardt',AllowDegeneratedPeaks='1')
ProcessBackground(InputWorkspace='NOM_10291_Bank5',OutputWorkspace='NOM_10291_Bank5_Background',
                  Options='SelectBackgroundPoints',BackgroundPointSelectMode='Input Background Pionts Only',
                  LowerBound='3720',UpperBound='15288',
                  BackgroundPoints='3722,4188,4487,5132,5514,5477,6228,6531,6932,7315,8568,9480,10025,10704,11482,12564,14000,15000,15280',
                  NoiseTolerance='0.10000000000000001')
Fit(Function='name=Polynomial,n=6,A0=0.00773246,A1=8.16986e-05,A2=-2.08771e-08,A3=1.76857e-12,A4=-7.87425e-18,A5=-5.21571e-21,A6=1.70891e-25',
    InputWorkspace='NOM_10291_Bank5_Background',MaxIterations='1000',
    Minimizer='Levenberg-MarquardtMD',CreateOutput='1',Output='NOM_10291_Bank5_Background',StartX='3720',EndX='15288')
LeBailFit(InputWorkspace='NOM_10291_Bank5',OutputWorkspace='CalculatedPattern0',InputParameterWorkspace='Bank5InstrumentParameterTable1',
          OutputParameterWorkspace='Bank5InstrumentParameterTable1_0',
          InputHKLWorkspace='BraggPeakParameterTable1',OutputPeaksWorkspace='BraggPeakParameterTable2_0',
          FitRegion='3720,15288',Function='Calculation',BackgroundParametersWorkspace='NOM_10291_Bank5_Background_Parameters',
          UseInputPeakHeights='0',PeakRadius='8',Minimizer='Levenberg-Marquardt',AllowDegeneratedPeaks='1')
LeBailFit(InputWorkspace='NOM_10291_Bank5',OutputWorkspace='NOM_10291_Bank5_MC_1000',
          InputParameterWorkspace='Bank5InstrumentParameterTable1_0',OutputParameterWorkspace='Bank5InstrumentParameterTable_MC',
          InputHKLWorkspace='BraggPeakParameterTable1',OutputPeaksWorkspace='BraggPeakParameterTable3',
          FitRegion='3720,15288',Function='MonteCarlo',
          BackgroundParametersWorkspace='NOM_10291_Bank5_Background_Parameters',
          UseInputPeakHeights='0',PeakRadius='8',Minimizer='Levenberg-Marquardt',
          Damping='0.90000000000000002',NumberMinimizeSteps='10000',FitGeometryParameter='1',
          RandomSeed='1000',AnnealingTemperature='10',DrunkenWalk='1',AllowDegeneratedPeaks='1')
