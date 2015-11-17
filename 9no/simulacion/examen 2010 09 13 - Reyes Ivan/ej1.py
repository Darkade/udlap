# -*- coding: utf-8 -*-
#!/usr/bin/python

from math import exp,log,sqrt
from random import random
import numpy as np
import pylab as P

X=lambda: log(random()*(exp(1)-1)+1 )
av=lambda o: float(sum(o))/len(o)
m=10000
	
print "\n\nEjercicio 1 pag 81"
print "Se puede obtener la función de acumulación para esta distribución."
print "Luego mediante el metodo de la transformada inversa obtener la formula"
print "que se debe emplear para generar una observación:"
print "		log(random()*(exp(1)-1)+1 )"

print "\nEstan a punto de generarse",m,"observaciones de la distribución."


observaciones=[X() for i in range(m)]
promedio=av(observaciones)

print "El promedio de las observaciones es:",promedio

P.hist(observaciones,sqrt(m))
P.show()
