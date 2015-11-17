# -*- coding: utf-8 -*-
#!/usr/bin/python

from distribuciones import discretas
from math import sqrt
import numpy as np
import pylab as P

X=discretas()
Y=discretas()


def suma_dados():
	observaciones=[]
	i=0
	while len(observaciones) < 11:
		i+=1
		observacion=X.uniforme_d(6)+Y.uniforme_d(6)
		if not (observacion in observaciones):
			observaciones.append(observacion)
	return i

observar=lambda m:[suma_dados() for i in range(m)]
av=lambda o: float(sum(o))/len(o)

m=10000

observaciones=observar(10000)
promedio=av(observaciones)

print "\n\nEjercicio 7 pagina 58"
print "Se van a realizar m=",m,"observaciones del problema requerido"
print "El promedio de tiradas necesarias para obtener todas las posibles sumas 2,3,...,12 es",promedio
print "A continuación el histograma de los datos\n\n"
P.hist(observaciones,sqrt(m))
P.show()
