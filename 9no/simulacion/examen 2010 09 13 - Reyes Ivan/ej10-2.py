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


print "\n\nEjercicio 10 pagina 59, simulación mediante 2do metodo"
print "\nEstan por realizarse",m,"observaciones de una distribución binomial negativa"
print "con p=",p,"y r=",r
print "El metodo de generación es el siguiente:\n"
print """def binomial_neg2(self,p,r):
    suma=0
        for i in range(10):
            suma+=self.geometrica(p)
    return  suma"""
print "\nDonde self.geometrica llama a la simulación de una variable geometrica de la clase distribuciones.py"
observaciones=[X.binomial_neg2(p,r) for i in range(m)]

print "\nEl promedio de las observaciones es:",av(observaciones)

P.hist(observaciones)
P.show()

