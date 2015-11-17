# -*- coding: utf-8 -*-
from random import random
from math import log

geo=lambda p: int(log(rand())/log(1-p))+1

print "Script que genera m observaciones de una variable ~geo(p)"
m=int(raw_input("¿Cuantas variables aleatorias se van a generar (m)? "))
n=int(raw_input("¿Cual es el parametro de la distribución geometrica (p)? "))

print "Se van a realizar",m,"observaciones de una variable geometrica (," + str(p) + ")\n"

observaciones=[geo(n) for i in range(0,m)]
print observaciones
#estadistica=[observaciones.count(i) for i in range(1,n+1)]

#for i in range(0,n):
#	print "De",m,"observaciones realizadas",estadistica[i],"fueron",i+1,"que es el",float(estadistica[i])/m*100,"%"
