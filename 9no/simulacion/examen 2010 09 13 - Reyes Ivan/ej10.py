# -*- coding: utf-8 -*-
#!/usr/bin/python
from distribuciones import discretas
from math import sqrt
import numpy as np
import pylab as P

X=discretas()
av=lambda o: float(sum(o))/len(o)



p=.7
r=10
m=100000

print "\n\nEjercicio 10 Pagina 59"
print "\nEstan por realizarse",m,"observaciones de una distribución binomial negativa"
print "con p=",p,"y r=",r

observaciones=[X.binomial_neg(p,r) for i in range(m)]
promedio=av(observaciones)

print "El promedio de las observaciones es:",promedio

P.hist(observaciones)
P.show()
