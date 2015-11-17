#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import random
from math import sqrt
import pylab as P

def triangular(a,b,c):
	U=random()
	Fc=float((c-a))/(b-a)
	print Fc
	if U<=Fc:
		return a+sqrt(U*(b-a)*(c-a))
	else:
		return b-sqrt((1-U)*(b-a)*(b-c))


h=[triangular(500,3500,2000)for i in range(1000)]
P.hist(h,100)
P.show()
