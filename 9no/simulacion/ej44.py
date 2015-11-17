#!/usr/bin/python
from random import random
observaciones=list()
for i in range(0,300):
	observaciones.append(pow(1-random()**2,3.0/2.0))

print "La aproximacion de la integral es:",sum(observaciones)/len(observaciones)

