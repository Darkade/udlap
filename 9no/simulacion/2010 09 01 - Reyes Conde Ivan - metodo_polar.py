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
	x=continuas()

	while True:
		try:
			m=long(raw_input("\n\nNumero de observaciones (el metodo polar devolverá el doble): "))
			break
		except ValueError:
			print "El dato no es un número."

	observaciones=[]
	for i in range(0,m):
		observaciones+=x.polar()

	P.hist(observaciones,sqrt(m))
	P.show()

