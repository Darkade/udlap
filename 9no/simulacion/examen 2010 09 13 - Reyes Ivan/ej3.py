# -*- coding: utf-8 -*-
#!/usr/bin/python


from random import random
import numpy as np
import pylab as P

F=[.3,.3+.2,.3+.2+.35,.3+.2+.35+.15]

def discreta():
	u=random()
	for i in range(1,5):
		if u<F[i-1]:
			return i

observar=lambda m:[discreta() for i in range(m)]

av=lambda o: float(sum(o))/len(o)


observaciones=observar(1000)
promedio=av(observaciones)

print "\n\n"
print "Ejercicio 3 pagina 53"
print "El promedio de las observaciones es:",promedio

P.hist(observaciones)
P.show()
	

