#!/usr/bin/env python
from math import pi
qrange=[[.46,20],[.92,25],[1.6,50],[3.0,50],[4.0,50],[.2,15]]
dmins = []
dmaxs = []
for (qmin, qmax) in qrange:
    dmaxs.append(2.*pi/qmin)
    dmins.append(2.*pi/qmax)
print dmins
print dmaxs
