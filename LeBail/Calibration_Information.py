######################################################################
# User specified information for instrument calibration
######################################################################

BANKID = 1

# Calibration information dictionary
calibDict = {}

# Directories
calibDict["DataFileDir"] = "/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/FERNS-LaB6/"
calibDict["HKLFileDir"]  = "/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/Reflections/"
calibDict["IrfFileDir"]  = "/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/PeakProfiles/"
calibDict["WorkingDir"]  = ""

# Background
calibDict["BackgroundType"]  = "Polynomial"
calibDict["BackgroundOrder"] = 6

# Bank 1 Information
calibDict[1] = {
        "DataFileName"      : "PG3_10808-1.dat",
        "HKLFileName"       : "LB4844b1.hkl",
        "IrfFileName"       : "2011B_HR60b1.irf",
        "DataWorkspace"     : "PG3_10808",
        "LeBailFitMinTOF"   : 5053.,
        "LeBailFitMaxTOF"   : 49387.,
        "SinglePeakFitMin"  : 15000.,
        "SinglePeakFitMax"  : 49387.,
        "LatticeSize"       : 4.1568899999999998,
        "UserSpecifiedBkgdPts": "5243,8910,11165,12153,13731,15060,16511,17767,19650,21874,23167,24519,36000,44282,49000"
        }
	
calibDict[2] = {
        "DataFileName"      : "PG3_10809-2.dat",
        "HKLFileName"       : "LB4853b2.hkl",
        "IrfFileName"       : "2011B_HR60b2.irf",
        "DataWorkspace"     : "PG3_10809",
        "LeBailFitMinTOF"   : 7000.,
        "LeBailFitMaxTOF"   : 71260.,
        "SinglePeakFitMin"  : 17322.,
        "SinglePeakFitMax"  : 71260.,
        "LatticeSize"       : 4.1568899999999998,
        "UserSpecifiedBkgdPts": "5243,8910,11165,12153,13731,15060,16511,17767,19650,21874,23167,24519,36000,44282,49000, 60000., 71240."
        }
	
calibDict[3] = {
        "DataFileName"      : "PG3_10810-3.dat",
        "HKLFileName"       : "LB4854b3.hkl",
        "IrfFileName"       : "2011B_HR60b3.irf",
        "DataWorkspace"     : "PG3_10810",
        "LeBailFitMinTOF"   : 10000.,
        "LeBailFitMaxTOF"   : 70000.,
        "SinglePeakFitMin"  : 16866.,
        "SinglePeakFitMax"  : 70000.,
        "LatticeSize"       : 4.1568899999999998,
        "UserSpecifiedBkgdPts": "5243,8910,11165,12153,13731,15060,16511,17767,19650,21874,23167,24519,36000,44282,49000, 60000., 71240."
        }
	

#def setupGlobals(usrbankid):
#    """ Set up globals values
#    """
#    global datafilename, hklfilename, irffilename  
#    global datawsname, instrparamwsname, braggpeakparamwsname
#    global outdataws1name , montecarlofilename
#    global bkgdtablewsname, bkgdwsname, bkgdfilename
#    global expirffilename
#    global tofmin_singlepeaks, tofmax_singlepeaks, startx, endx
#    global bankid, latticesize
#    global usrbkgdpoints
#
#    bankid = usrbankid
#
#    
#    elif bankid == 3:
#	# Bank2
#	datafilename = '/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/FERNS-LaB6/PG3_10810-3.dat'
#	hklfilename = "/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/Reflections/LB4854b3.hkl"
#	irffilename = r'/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August/PeakProfiles/2011B_HR60b3.irf'
#
#	expirffilename = "/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August_Bank2/Bank3.irf"
#
#	montecarlofilename = '/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August_Bank3/Bank3InstrumentMC.dat'
#
#	datawsname = "PG3_10810"
#    
#	outdataws1name = "PG3_10810_FittedSinglePeaks"
#
#        startx = 10000.0
#        endx =   70000.0
#
#        tofmin_singlepeaks = 16866.
#        tofmax_singlepeaks = 70000.
#
#
#        bkgdtablewsname = "PG3_10809_Background_Parameters"
#        bkgdwsname = "PG3_10808_Background"
#        bkgdfilename = '/home/wzz/Projects/MantidTests/LeBailFit/PG3_2012August_Bani2/PG3_10808_Background_Parameters.bak'
#
#        latticesize = 4.1568899999999998
#
#        usrbkgdpoints = '5243,8910,11165,12153,13731,15060,16511,17767,19650,21874,23167,24519,36000,44282,49000'   
#
#    else:
#	# Bank ?
#	raise NotImplementedError("To be implemented ASAP for Bank %d!" % (bankid))
#
#
#    instrparamwsname = "Bank%sInstrumentParameterTable" % (bankid)
#    braggpeakparamwsname = 'BraggPeakParameterTable'
#
#
#    return
