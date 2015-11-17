# -*- coding: utf-8 -*-
from random import random

ud=lambda n: int(n*random())+1

#m=100000
#n=3

print "Script que genera m observaciones de una variable uniforme discreta 0,n"
m=int(raw_input("¿Cuantas variables aleatorias se van a generar (m)? "))
n=int(raw_input("¿De 0 a donde se van a generar valores (n)? "))

print "Se van a realizar",m,"observaciones de una variable uniforme discreta (0," + str(n) + ")\n"

observaciones=[ud(n) for i in range(0,m)]
estadistica=[observaciones.count(i) for i in range(1,n+1)]

for i in range(0,n):
	print "De",m,"observaciones realizadas",estadistica[i],"fueron",i+1,"que es el",float(estadistica[i])/m*100,"%"
