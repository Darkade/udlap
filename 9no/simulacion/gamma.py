#!/usr/bin/python
# -*- coding: utf-8 -*-

from distribuciones import continuas
from math import sqrt

try:
	import numpy as np
	import pylab as P
except ImportError:
	print	"""Se necesitan las librerias numpy y matplotlib instaladas
	numpy ->		http://www.scipy.org/Installing_SciPy
	matplotlib ->	http://matplotlib.sourceforge.net/users/installing.html

	También es necesario que el archivo distribuciones y distros.py se encuentren en el mismo directorio"""
	
else:
	X=continuas()

	l=raw_input("lambda, el parametro de la distribución: ")
	k=raw_input("k, el número de grados de libertad: ")
	m=raw_input("m, número de observaciones a realizar: ")

	observaciones=[X.gamma(k,l) for i in range(0,m)]

	P.hist(observaciones,sqrt(m))
	P.show()

