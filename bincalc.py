#!/usr/bin/env python
import math

numpoints = 3000
qrange=[[.46,20],
[.92,25],
[1.6,50],
[3.0,50],
[4.0,50],
[.2,15]]
drange = [(2.*math.pi/x[1],2.*math.pi/x[0]) for x in qrange]

def calcScale(dmin, dmax, deltad):
     d = [dmin]
     temp = dmin
     while temp < dmax:
          temp = temp * (deltad + 1.)
          d.append(temp)
     return d

for i, (dmin, dmax) in zip(range(len(drange)), drange):
     #dmin = 1.
     #dmax = 1.
     print "%d:%f -> %f" % ((i+1), dmin, dmax)
     deltad = (math.log(dmax) - math.log(dmin))/float(numpoints)
     shift = .1
     sign = 0
     first = True
     for j in range(100):
          d = calcScale(dmin, dmax, deltad)
          if first:
               print ' %d %f %f' % (len(d), deltad, shift)#, d[0:3]
               first = False
          if len(d) > numpoints:
               deltad *= (1. + shift)
               if sign == 0:
                    sign = 1
               elif sign == -1:
                    sign = 1
                    shift *= .9
          elif len(d) < numpoints:
               deltad *= (1. - shift)
               if sign == 0:
                    sign = -1
               elif sign == 1:
                    sign = -1
                    shift *= .9
          else:
               print ' SUCCESS!!!!!!!!!!!!', deltad
               deltad = round(deltad, 6)
               d = calcScale(dmin, dmax, deltad)
               print ' %d ' % len(d), deltad#, d[0:3]
               break
