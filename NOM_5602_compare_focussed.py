#single = LoadEventPreNexus(EventFilename="/SNS/NOM/IPTS-6034/0/5602/preNeXus/NOM_5602_neutron_event.dat", SpectrumList=[59327])
#EditInstrumentGeometry(single, PrimaryFlightPath=19.5, SpectrumIDs=[59328], L2=[1.095], Polar=[123.2], Azimuthal=[0], NewInstrument=True)
#single = ConvertUnits(single, Target="MomentumTransfer")
#single = CompressEvents(single, Tolerance=.01)
#single = Rebin(single, Params=(0., .02, 49.98), PreserveEvents=True)
#Joerg = LoadAscii("/home/pf9/Downloads/e57t0p63.dat", Unit="MomentumTransfer")
#print blah

LoadCalFile(InstrumentName="NOMAD", CalFilename="/tmp/NOM_calibrate_d9334_2012_10_24.cal", WorkspaceName="NOM")
print blah
NOM_5602 = Load(Filename="NOM_9334_event.nxs")#/home/pf9/NOM_5602_event.nxs")#, ChunkNumber=3, TotalChunks=3)
#LoadInstrument(NOM_5602, Filename="/home/pf9/code/mantidgeometry/NOMAD_Definition.xml")
#NOM_5602 = CompressEvents(NOM_5602, Tolerance=.01)
#print blah
#NOM_5602 = Load(Filename="/SNS/NOM/IPTS-6034/0/5602/preNeXus/NOM_5602_neutron_event.dat", ChunkNumber=1, TotalChunks=3)
NOM_5602 = CompressEvents(NOM_5602, Tolerance=.01)
#LoadInstrument(NOM_5602, Filename="/home/pf9/code/mantidgeometry/NOMAD_Definition.xml")
#NOM_5602 = ConvertUnits(NOM_5602, Target="dSpacing")
NOM_5602 = AlignDetectors(InputWorkspace=NOM_5602, OutputWorkspace=NOM_5602, OffsetsWorkspace="NOM_offsets")
NOM_group = CreateGroupingWorkspace(InputWorkspace=NOM_5602, GroupDetectorsBy="Group")
NOM_5602 = DiffractionFocussing(NOM_5602, GroupingWorkspace=NOM_group, PreserveEvents=True)
NOM_5602 = ConvertUnits(NOM_5602, Target="MomentumTransfer")
NOM_5602 = CompressEvents(NOM_5602, Tolerance=.01)
NOM_5602 = Rebin(NOM_5602, Params=(.51, .02, 50.01), PreserveEvents=True)
NOM_5602 = NormaliseByCurrent(NOM_5602)
NOM_5602 /= 3600.
#print NOM_5602.getNumberEvents()
#NOM_5602 = CropWorkspace(NOM_5602, .5, 50)
#print NOM_5602.getNumberEvents()
Joerg1 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank0.dat", Unit="MomentumTransfer")
Joerg2 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank1.dat", Unit="MomentumTransfer")
Joerg3 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank2.dat", Unit="MomentumTransfer")
Joerg4 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank3.dat", Unit="MomentumTransfer")
Joerg5 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank4.dat", Unit="MomentumTransfer")
Joerg6 = LoadAscii("/home/pf9/Downloads/NOM_5602_focussed/Scan5602_bank5.dat", Unit="MomentumTransfer")
