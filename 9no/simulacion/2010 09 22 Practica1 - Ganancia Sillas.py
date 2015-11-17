#!/usr/bin/python
# -*- coding: utf-8 -*-

from distribuciones import continuas
from random import random
from math import sqrt
import pylab as P


Costo=175
Total_Sillas=3000

Precio_Maximo=300
Precio_Minimo=200

Ventas_Minimo= 500
Ventas_Maximo=3500
Ventas_Moda=  2000

m=100000

def triangular(a,b,c):
	U=random()
	Fc=float((c-a))/(b-a)
	return a+sqrt(U*(b-a)*(c-a)) if U<=Fc else b-sqrt((1-U)*(b-a)*(b-c))


def ganancia():
	precio_inicial=min(Total_Sillas,Precio_Maximo-(Precio_Maximo-Precio_Minimo)*random())
	precio_final=precio_inicial/2

	ventas_inicial=triangular(Ventas_Minimo,Ventas_Maximo,Ventas_Moda)
	ventas_final=Total_Sillas-ventas_inicial

	return (precio_inicial-Costo)*ventas_inicial+(precio_final-Costo)*ventas_final

promedio=lambda observaciones:sum(observaciones)/len(observaciones)
varianza=lambda observaciones,promedio: sum((i-promedio)**2 for i in observaciones)/(len(observaciones)-1)

observaciones=[ganancia() for i in range(m)]
p=promedio(observaciones)
s=sqrt(varianza(observaciones,p))

print "\n\n\nGanancia esperada de la venta de sillas."
print "Promedio:",p,"Desviación Estandar:",s

P.hist(observaciones,sqrt(m))
P.show()

