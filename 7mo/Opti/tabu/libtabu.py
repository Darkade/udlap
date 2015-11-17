#!/usr/bin/python
# coding=UTF-8

import re
import math
import random

class Modelo:
	fobjetivo = []
	restricciones = []
	
	#ValorObjetivo
	def Z(self,decision):
		Z=0
		for i in range(len(self.fobjetivo)):
			Z+=self.fobjetivo[i]*decision[i]
		return Z
	
	#Factibilidad
	def Factible(self,decision):
		nr=len(self.restricciones) #Numero de restricciones		

		for i in range(nr):
			nc=len(self.restricciones[i])-2 # numero de componentes, en -2 esta la restriccion, en -1 la comparacion
			r=0				#valor de la ecuacion
			R=0				#cota de la restriccion

			for j in range(nc):
				r+=self.restricciones[i][j]*decision[j]	#valor de la ecuacion

			R=self.restricciones[i][nc+1]				#cota
			C=self.restricciones[i][nc]				#Comparacion
			resultado = {						#resultado de comparar el valor y la cota
			">" or ">=":	lambda r, R: r >= R,
			"<" or "<=":	lambda r, R: r <= R,
			"=":		lambda r, R: r == R
			}[C](r,R)
			if resultado == False : return False			#si a acada ciclo una restriccion no se comple devuelve false y sale
		return True							# si la funcion llega al final devuelve true, si es factible

	#Valor de las restrcciones
	def ValorR(self,decision):
		valores=[]
		for i in range(len(self.restricciones)):
			r=0				#valor de la ecuacion

			for j in range(len(self.restricciones[i])-2):
				r+=self.restricciones[i][j]*decision[j]	#valor de la ecuacion		
			valores.append(r)
		return valores

class SolucionInicial:


	def Aleatorio(self,t):
		solucion=[]							#limpia el arreglo para no ciclarse
		random.seed()							#genera un semilla a partir de la hora actual
		for i in range(t):
			solucion.append(random.randint(0,1))			#agrega un aleatorio 0 o 1 a cada posicion
		return solucion

	def Usuario(self,t):
		solucion=[]
		for i in range (t):
			solucion.append(int(raw_input("x"+str(i+1) + " = ")))
		return solucion

class Generar_Vecinos:
	def Standar(self,s_actual):
		vecinos=[]							#iniciar vecinos[] que es un arreglo vacio
		for i in range(len(s_actual)):					#comparar si la diagonal es cero o uno y cambiar
			vecinos.append(s_actual[:])
			if vecinos[i][i] == 0:
				vecinos[i][i] = 1
			elif vecinos[i][i] == 1:
				vecinos[i][i] = 0
		return vecinos


class Lista:
	tabus = []
	size = 7
	def AddTabu(self,elemento):
		self.tabus.append(elemento[:])
		while len(self.tabus) > self.size:
			del self.tabus[0]
	def IsTabu(self,elemento):
		if elemento in self.tabus: # considera la posicion cero como falso y la 1 como verdadero, aprender a manejar error
			return True
		else:
			return False
	def Clear(self):
		self.tabus=[]


