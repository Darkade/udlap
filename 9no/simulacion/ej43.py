#!/usr/bin/python
from random import random
from math import exp
observaciones=list()
e=exp(1)
for i in range(0,1000):
	observaciones.append(e**e**random())

print "La aproximacion de la integral es:",sum(observaciones)/len(observaciones)

