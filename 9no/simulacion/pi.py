# -*- coding: utf-8 -*-
from random import random
from math import sqrt

g= lambda n: float([random()**2+random()**2<=1 for i in range(0,n)].count(True))/n*4
h= lambda m,n: [g(n) for i in range(0,m)]
fun_media= lambda arreglo: sum(arreglo)/len(arreglo)
fun_stdev= lambda arreglo,xbar: sqrt(sum([(i - xbar)**2 for i in arreglo])/(len(arreglo)-1))

m=10
n=1000
observaciones=h(m,n)
media=fun_media(observaciones)
stdev=fun_stdev(observaciones,media)

#print "Observaciones de pi:",observaciones
print "Se realizó la aproximación con",m,"simulaciones de pi calculadas con",n,"variables ~U(0,1)"
print "Media observaciones: π ≈",media
print "Desviación Standar observaciones: σ ≈",stdev
