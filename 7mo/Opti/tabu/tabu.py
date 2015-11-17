#!/usr/bin/python
# coding=UTF-8

from libtabu import *

def imprimir(buff,mensaje):
	if buff != None:
		buff.insert(buff.get_end_iter(), mensaje+"\n")
	else:
		print mensaje



def resolver_modelo(fobjetivo=[],restricciones=[],v_inicial=[],tipoinicial=str,iteraciones=int,tabu=int,buff=None,progreso=None):
	model = Modelo()
	vecinos = Generar_Vecinos()
	ListaTabu = Lista()
	ListaTabu.zize=tabu
	inicial = SolucionInicial()
	

	model.fobjetivo=fobjetivo
	model.restricciones=restricciones
	
	nvariables=len(model.fobjetivo)
	
	########################<solución inicial>#####################
	if tipoinicial=="r" or tipoinicial=="random":
		actual=inicial.Aleatorio(nvariables)
		while not model.Factible(actual):
			actual = inicial.Aleatorio(nvariables)
		imprimir(buff,"La solución Aleatoria generada es " +str(actual))
	
	elif tipoinicial=="u" or tipoinicial=="usuario":
		if model.Factible(v_inicial) == False:
			imprimir(buff, "La solución no es factible\n\n")
			quit()
		else:
			actual=v_inicial
			imprimir(buff, "La solución del usuario es" + str(actual))

	elif tipoinicial=="up" or tipoinicial=="unidadpeso":
		tentativo1=[float(model.fobjetivo[i]) / float(model.restricciones[0][i]) for i in range(nvariables)]
		tentativo2=sorted(tentativo1[:],reverse=True)

		actual= [0 for i in range(nvariables)]
		for i in  [tentativo1.index(valor) for valor in tentativo2]:
			actual[i]=1
			if not model.Factible(actual): 
				actual[i]=0
				break
		imprimir(buff, "La solución U/P generada es " +str( actual ))
	else:
		imprimir(buff,"no es una opcion valida\n\n")

########################</solución inicial>#####################
	
	
	###########<ALGORITMO>############################
	
	mejor=actual		#asignar que al inicio la mejor solución es la solucion inicial
	continuar=True
	
	while continuar:
		for i in range(iteraciones):
#			progreso.set_pulse_step(float(i+1)/float(iteraciones))
			progreso.set_fraction(float(i+1)/float(iteraciones))
			
			imprimir(buff,"ITERACION #" + str(i) + " ----- Solución actual: " + str(actual))
			mejorv=[]
			V=vecinos.Standar(actual)[:]
		
			ListaTabu.AddTabu(actual)
		
			for vecino in V[:]:
				if model.Factible(vecino):
					mejorv=vecino
					break
		
			for vecino in V[:]:
				imprimir(buff, str(vecino) + " Valor objetivo: " + str(model.Z(vecino)) + "; Factible? " + str(model.Factible(vecino)))
				if model.Factible(vecino) and not ListaTabu.IsTabu(vecino):
					if model.Z(vecino) >= model.Z(mejorv):
						mejorv=vecino
	
			actual=mejorv
			if model.Z(mejorv) >= model.Z(mejor):
				mejor=mejorv
			
		
			imprimir(buff, "Mejor Vecino:		"  +str(mejorv))
			imprimir(buff, "Nueva Solución actual:	" +str(actual))
			imprimir(buff, "BEST EVER:		" +str(mejor) + "\n")
			imprimir(buff, "Valor Objetivo:		" +str(model.Z(mejor)))
			imprimir(buff, "valor restricciones:	" +str(model.ValorR(mejor)) + "\n\n")
		C=""
#		C = raw_input("Continuar con la ultima mejor solución? (S/n)")
		if  C == "S" or C == "s":
			continuar=True
		else:
			continuar=False
	###########</ALGORITMO>############################
#resolver_modelo([40,80,50,70,75,40,40,65],[[20,30,15,40,25,16,18,30,"<",100]],"up",100)
