# -*- coding: utf-8 -*-
from random import random

g= lambda n: float([random()**2+random()**2<=1 for i in range(0,n)].count(True))/n*4
print "π ≈",g(1000000)


#h= lambda m: sum([g(100000) for i in range(0,m)])/m
#print h(100)

