from random import normalvariate as normal
from math import sqrt,exp

import pylab as P
import mpl_toolkits.mplot3d.axes3d as P3




P0=150
mu=.15
s=0.04
t=1

m=7

X=[]
Y=[]

Pt=P0


for t in [0,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5]:
	tendencia	=	(mu-s**2/2)*t
	ruido		=	s*sqrt(t)*normal(0,1)
	Pt			=	P0*exp(tendencia+ruido)

	X.append(t)
	Y.append(Pt)

P.plot(X,Y)
P.show()
