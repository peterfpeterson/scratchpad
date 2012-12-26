from MantidFramework import *
from mantidsimple import *
from mantid.api import AlgorithmFactory

class Broken(PythonAlgorithm):
    def PyInit(self):
        self.declareFileProperty("left", "", FileAction.Load)
        self.declareFileProperty("right", "", FileAction.Load)
        self.declareWorkspaceProperty("OutputWorkspace", "", Direction=Direction.Output)
    def PyExec(self):
        Load(Filename=self.getPropertyValue("left"), OutputWorkspace="left")
        right = Load(self.getPropertyValue("right"), OutputWorkspace="right")
        left = mtd['left']
        right = mtd['right']
        left += right
        self.setProperty("OutputWorkspace", left)

mtd.registerPyAlgorithm(Broken())
