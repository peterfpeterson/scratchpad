root = "/home/pf9/code/systemtests/"
LoadGSS(Filename=root+"InstallerTesting/PG3_4866.gsa", OutputWorkspace="current")
LoadGSS(Filename=root+"SystemTests/AnalysisTests/ReferenceResults/PG3_4866_reference.gsa",
        OutputWorkspace="unstable")
LoadGSS(Filename=root+"SystemTests/AnalysisTests/ReferenceResults/PG3_4866_Stable.gsa",
        OutputWorkspace="stable")
workspaces = ("current", "unstable", "stable")
for wksp in workspaces:
    ConvertUnits(InputWorkspace=wksp, OutputWorkspace=wksp, Target="dSpacing")
#mantid.plotSpectrum(workspaces, [0,0,0], True)