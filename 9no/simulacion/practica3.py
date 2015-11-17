from random import random
from math import exp
class integral:
	a=float()
	b=float()
	def tl(self,y):
		return (self.b-self.a)*y + self.a
	def g(self,x):
		return exp(x)
	def h(self,y):
		return self.g(self.tl(y))*(self.b-self.a)

integral=integral()
integral.a=-2
integral.b=2

observaciones=list()
for i in range(0,200000):
	observaciones.append(integral.h(random()))

print "La aproximacion es:",sum(observaciones)/len(observaciones)

print integral.a
