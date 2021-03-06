LoadCalFile(InstrumentName="NOMAD", CalFilename="/tmp/NOM_calibrate_d9334_2012_10_30.cal", WorkspaceName="NOM")
NOM_9334 = Load("NOM_9334_event.nxs")
NOM_9334 = CompressEvents(NOM_9334, Tolerance=.01)
NOM_9334 = AlignDetectors(InputWorkspace=NOM_9334, OutputWorkspace=NOM_9334, OffsetsWorkspace="NOM_offsets")
NOM_9334 = DiffractionFocussing(NOM_9334, GroupingWorkspace="NOM_group", PreserveEvents=True)
NOM_9334 = ConvertUnits(NOM_9334, Target="MomentumTransfer")
#NOM_9334 = CompressEvents(NOM_9334, Tolerance=.01)
NOM_9334 = Rebin(NOM_9334, Params=(.01, .02, 50.01), PreserveEvents=True)
EditInstrumentGeometry(NOM_9334, SpectrumIDs=(1,2,3,4,5,6), PrimaryFlightPath=19.5, L2=(2,2,2,2,2,2), Polar=(15,31,67,122,154,7), Azimuthal=(0,0,0,0,0,0))

Joerg1 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank000.dat", Unit="MomentumTransfer")
Joerg2 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank001.dat", Unit="MomentumTransfer")
Joerg3 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank002.dat", Unit="MomentumTransfer")
Joerg4 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank003.dat", Unit="MomentumTransfer")
Joerg5 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank004.dat", Unit="MomentumTransfer")
Joerg6 = LoadAscii("/SNS/NOM/IPTS-4480/shared/Scan9334_Bank005.dat", Unit="MomentumTransfer")
