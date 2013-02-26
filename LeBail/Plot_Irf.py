######################################################################
#
# This script is migrated from Calibration_Step1 in order to plot 
# how good an irf file is.  
# Besides the naming of workspaces, there is no difference from Calibration_Step1
#
# Python Script as Step 1 of Le Bail Fitting to
# 1. Load file
# 2. Create LeBailFitInput
# 3. Fit background
# 4. Fit Peaks
#
# Step 1:   Load data, model (HKL list) and starting instrument parameters values,
#           and do an initial LeBailFit/calculation to see how much the starting
#           values are off;
#
######################################################################
from Calibration_ImportInformation import *

#--------------  Definition of Global Variables ---------------------
bankid = 0

datafilename = "" 
hklfilename = ""
irffilename = ""

# montecarlofilename = ""
# expirffilename = ""

datawsname = ""
instrparamwsname = ""
braggpeakparamwsname = ""

# outdataws1name = ""

minpeakheight = 0.001

# Range for Le Bail Fit of all peaks 
startx = -1
endx =  -1
# Range for fitting single peaks for step 1~3 
tofmin_singlepeaks = -1
tofmax_singlepeaks = -1

backgroundtype = "Polynomial"
backgroundorder = 6
bkgdtablewsname = ""
bkgdwsname = ""
bkgdfilename = ""
usrbkgdpoints = ''

latticesize = 4.1568899999999998
#--------------------------------------------------------------------


def setupGlobals(infofilename):
    """ Set up globals values
    """
    global datafilename, hklfilename, irffilename  
    global datawsname, instrparamwsname, braggpeakparamwsname
    global bkgdtablewsname, bkgdwsname, bkgdfilename
    global tofmin_singlepeaks, tofmax_singlepeaks, startx, endx
    global bankid, latticesize
    global usrbkgdpoints

    bankid, calibDict = importCalibrationInformation(infofilename)
    bankid = int(bankid)

    datafilename = calibDict["DataFileDir"] + calibDict[bankid]["DataFileName"] 
    hklfilename  = calibDict["HKLFileDir"]  + calibDict[bankid]["HKLFileName"]
    irffilename  = calibDict["IrfFileDir2"]  + calibDict[bankid]["IrfFileName2"]
    
    datawsname = calibDict[bankid]["DataWorkspace"]
    
    startx = float(calibDict[bankid]["LeBailFitMinTOF"])
    endx   = float(calibDict[bankid]["LeBailFitMaxTOF"])

    # Background related
    usrbkgdpoints   = calibDict[bankid]["UserSpecifiedBkgdPts"]
    bkgdwsname      = datawsname+"_Background"
    backgroundtype  = calibDict["BackgroundType"]
    backgroundorder = int(calibDict["BackgroundOrder"])
    bkgdfilename    = calibDict["WorkingDir"] + datawsname + "_Parameters.bak'"
    bkgdwsname      = datawsname + "_Background"
    bkgdtablewsname = datawsname + "_Background_Parameters"
    
    latticesize   = calibDict[bankid]["LatticeSize"]
    usrbkgdpoints = calibDict[bankid]["UserSpecifiedBkgdPts"]

    instrparamwsname     = "Bank%sInstrumentParameterTable" % (bankid)
    braggpeakparamwsname = 'BraggPeakParameterTable'

    return

def doStep1(): 
    """ Step 1: Load data, parameters and do an initial/test Le Bail Fit/calculation 
    """
    global datafilename, hklfilename, irffilename
    global datawsname, instrparamwsname, braggpeakparamwsname
    global outdataws1name
    global bkgdtablewsname, bkgdwsname, backgroundtype, backgroundorder
    global tofmin_singlepeaks, tofmax_singlepeaks
    global bankid
    global latticesize
    
    # 1. Load File 
    print datawsname, irffilename
    LoadAscii(Filename=datafilename, OutputWorkspace=datawsname, Unit='TOF')

    # 2. Create Input Tables
    instrparamwsname = "%s_%s" % (instrparamwsname, irffilename.split(".")[0])

    CreateLeBailFitInput(ReflectionsFile=hklfilename, 
        FullprofParameterFile=irffilename, 
        LatticeConstant=float(latticesize), 
        InstrumentParameterWorkspace=instrparamwsname+"1", 
        BraggPeakParameterWorkspace=braggpeakparamwsname+"1",
        Bank=bankid)

    # 3. Process background 
    bkgdwsname = datawsname+"_Background"
    ProcessBackground(InputWorkspace=datawsname, 
            OutputWorkspace=bkgdwsname, 
            Options='SelectBackgroundPoints',
            LowerBound=startx, 
            UpperBound=endx, 
            BackgroundType=backgroundtype,
            BackgroundPoints=usrbkgdpoints,
            NoiseTolerance='0.10000000000000001')

    functionstr = "name=%s,n=%d" % (backgroundtype, backgroundorder)
    for iborder in xrange(backgroundorder+1):
        functionstr = "%s,A%d=%.5f" % (functionstr, iborder, 0.0)
    print "Background function: %s" % (functionstr)

    Fit(Function='name=Polynomial,n=6,A0=0.657699,A1=3.68433e-05,A2=-1.29638e-08,A3=1.16778e-12,A4=-4.71439e-17,A5=8.8499e-22,A6=-6.26573e-27',
            InputWorkspace=bkgdwsname,
            MaxIterations='1000',
            Minimizer='Levenberg-MarquardtMD',
            CreateOutput='1',
            Output=bkgdwsname,
            StartX=startx,
            EndX=endx)
        
    # 3. Use Le Bail Fit 's calculation feature to generate the starting peak parameters (for fitting) values (can be off)
    print "Background workspace name = ", bkgdtablewsname
    LeBailFit(InputWorkspace=datawsname,
            OutputWorkspace=datawsname+"_ashfia",
            InputParameterWorkspace=instrparamwsname+"1",
            OutputParameterWorkspace='TempTable',
            InputHKLWorkspace=braggpeakparamwsname+"1",
            OutputPeaksWorkspace=braggpeakparamwsname+"2",
            Function='Calculation',
            BackgroundType='Polynomial',
            BackgroundParametersWorkspace=bkgdtablewsname, 
            UseInputPeakHeights='0',
            PeakRadius='8',
            Minimizer='Levenberg-Marquardt')
    
    return


def main(argv):
    """ Main
    """
    setupGlobals("/home/wzz/Projects/MantidTests/LeBailFit/Test2013A/Bank1/Calibration_Information.config")
    
    print "Le Bail Fit Calibration Instrument... Step 1"
    doStep1()

    return


if __name__=="__main__":
    """ starter
    """
    main(["LeBailFitScript"])
