import sys
sys.path.append("/home/pf9/builds/mantid-debug/bin")
#sys.path.append("/opt/mantidnightly/bin")
#sys.path.append("/opt/Mantid/bin")

import mantid
#from MantidFramework import mtd
#mtd.initialise()
from mantid.simpleapi import *

file_name = "/SNS/TOPAZ/IPTS-4822/0/3857/NeXus/TOPAZ_3857_event.nxs"

LoadEventNexus( Filename=file_name, OutputWorkspace='TOPAZ_events', 
                FilterByTofMin='500', FilterByTofMax='16000' )

#ConvertToDiffractionMDWorkspace( InputWorkspace='TOPAZ_events', OutputWorkspace='TOPAZ_MDEW',
#                                 LorentzCorrection='1', OutputDimensions='Q (lab frame)',
#                                 SplitInto='2,2,2', SplitThreshold='50',MaxRecursionDepth='12')
ConvertToMD( InputWorkspace='TOPAZ_events', OutputWorkspace='TOPAZ_MDEW',
             LorentzCorrection=True, QDimensions='Q3D',
             dEAnalysisMode='Elastic', QConversionScales='Q in A^-1',
             SplitInto='2,2,2', SplitThreshold='50',MaxRecursionDepth='12',
             MinValues='-15,-15,-15', MaxValues='15,15,15')
sys.exit()
