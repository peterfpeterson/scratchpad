datadir='/SNS/REF_L/IPTS-9370/0/99508/'
nxsfile=datadir+'NeXus/REF_L_99508_event.nxs'
prefile=datadir+'preNeXus/REF_L_99508_runinfo.xml'

nxs = LoadEventNexus(nxsfile)
pre = LoadPreNexus(prefile)
