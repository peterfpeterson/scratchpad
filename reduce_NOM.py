import os
import sys
import shutil 
sys.path.append("/home/pf9/builds/mantid-debug/bin")
from MantidFramework import mtd
mtd.initialize()
from mantidsimple import *

cal_dir = "/SNS/NOM/IPTS-6491/shared/"
cal_file  = os.path.join(cal_dir, "NOM_calibrate_d9748_2012_12_07.cal")
char_file = "/SNS/users/pf9/NOM_characterizations.txt" #os.path.join(cal_dir, "NOM_characterizations.txt")
binning = (300,-0.0004,16667)
sam_back =     9749
van      =     9750
van_back =     9751

#from mantidsimple import *

eventFileAbs=sys.argv[1]
outputDir=sys.argv[2]

eventFile = os.path.split(eventFileAbs)[-1]
nexusDir = eventFileAbs.replace(eventFile, '')
runNumber = eventFile.split('_')[1]
configService = mtd.getSettings()
dataSearchPath = configService.getDataSearchDirs()
dataSearchPath.append(nexusDir)
configService.setDataSearchDirs(dataSearchPath)

SNSPowderReduction(Instrument="NOM", RunNumber=runNumber, Extension="_event.nxs",
                   PreserveEvents=False,PushDataPositive='AddMinimum',
                   CalibrationFile=cal_file, CharacterizationRunsFile=char_file,
                   BackgroundNumber=sam_back, VanadiumNumber=van,
                   VanadiumBackgroundNumber=van_back, RemovePromptPulseWidth=50,
                   Binning=binning, BinInDspace=False, FilterBadPulses=True,
                   SaveAs="gsas and fullprof and pdfgetn", OutputDirectory=outputDir,
                   StripVanadiumPeaks=True,
                   NormalizeByCurrent=True, FinalDataUnits="MomentumTransfer")
