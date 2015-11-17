# -*- coding: utf-8 -*-
from math import exp

class metodo_binomial:
	u=1.1
	d=1/u
	x=105
	spot=100
	r=.10

	def st(self,ups, downs):
		return self.spot*(pow(self.u,ups)*pow(self.d,downs))

	def f(self,ups,downs,tipo):
		if tipo == 'call':
			return max(self.st(ups,downs)-self.x,0)
		elif tipo == 'put':
			return max(self.x-self.st(ups,downs),0)

	def p(self,tiempo):
		return (exp(self.r*tiempo) -self.d)/(self.u-self.d)

	def q(self,tiempo):
		return 1 - (exp(self.r*tiempo) -self.d)/(self.u-self.d)

	def presente(self,tiempo):
		return exp(-1*self.r*tiempo)

	def pascal(self,niveles):
		uno=[1,1]
		
		for i in range(1,niveles):
			dos=[1]
			for j in range(0,i):
				dos.append(uno[j]+uno[j+1])
			dos.append(1)
			uno=dos[:]
		return uno

	def evaluar(self,nivel,tiempo,tipo):
		r=0
		pascal=self.pascal(nivel)
		for k in range(0,nivel+1):
			r+=pascal[k] * self.f(nivel-k,k,tipo) * pow(self.p(tiempo/nivel),nivel-k) * pow(self.q(tiempo/nivel),k)
		return r*self.presente(tiempo)



	def __init__(self):
		print """
Abril 2010
Librería diseñada por:
	Langarica, Lourdes
	Ramirez, Indira @indieveryday
	Reyes, Ivan @Darkade

Este trabajo se distribuye bajo la licencia GPL. Puedes obtener una
copia de la licencia en http://www.gnu.org/licenses/gpl.html
"""

	def help(self):
		print """
Funciones y variables incluidas en la libreria:
	Funciones:
		st(ups,downs): el precio spot del activo si hubo 'ups' subidas
			del precio y 'downs' bajadas
 		f(ups,downs,tipo): el valor de la opcion si el activo tuvo
			'ups' subidas y 'downs' bajadas. tipo={'call'|'put'}
		p(self.tiempo): devuelve el valor de la probabilidad implicita 'p'
			dados r,d,u. self.tiempo es el self.tiempo que ocurre en cada
			nivel, es decir: si son 3 meses y hay 3 niveles p nos
			devuelve la p para un més (e^(r*self.tiempo)-d)/(u-d)
		q(self.tiempo): devuelve 1-p(self.tiempo)
		presente(self.tiempo): devuelve el factor de descuento con la tasa
			continua r para un año y el self.tiempo dado del arbol. Si
			tienes 1 nivel necesitas el 2do renglon del triangulo

	Variables:
		u: la tasa de crecimiento del bien. Por default 1.1
		d: la tasa de decrecimiento del bien. Por default 1/u; es
			necesario redefinirla si se cambia la u
		x: precio de ejercicio de la opción
		spot: precio spot del bien en cero
		r: tasa libre de riesgo continua a un año"""
