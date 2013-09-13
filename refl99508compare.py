datadir='/SNS/REF_L/IPTS-9370/0/99508/'
nxsfile=datadir+'NeXus/REF_L_99508_event.nxs'
prefile=datadir+'preNeXus/REF_L_99508_runinfo.xml'

nxs = LoadEventNexus(nxsfile)
pre = LoadPreNexus(prefile, MappingFilename="/SNS/REF_L/2009_3_4B_CAL/calibrations/REF_L_TS_2010_02_19.dat", LoadMonitors=False)

print "match = %s" % CheckWorkspacesMatch(pre, nxs)
