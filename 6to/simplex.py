#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys


####################			<FUNCIONES>			####################################################################

##<Obtener el vector C>###################################################################################################
def GetVectorC(eq):
	C=[]
	j=0
	for i in range(len(eq)):							#Recorre toda la cadena de la restriccion
		if eq[i]=="+" or eq[i]=="-":						#Indicador de que se ha encontrado un signo de adicion,_
											#es decir acontinuacion hay un coeficiente
			j=i
		if eq[i]=="X" or eq[i]=="x":					#Agrega al vector y el coeficiente que se encontro
			C.append(float(eq[j:i]))
			j=i
	return C
##</Obtener el vector C>###################################################################################################

##<Encontrar Zj-Cj>###################################################################################################
def GetZjCj(A,C,Cb):
	ZC=[]									#Inicializa un vector ZC que contendra los Zj - Cj
	for i in range(len(C)):							#para cada valor en el vector C (al que ya se agregaron las A's y las h's)
		ZjCj=0								#inicializa una sumatoria
		for j in range(len(A)):						#Multiplica Cb por Yi y resta el Ci correspondiente
			ZjCj=ZjCj + float(A[j][i]*Cb[j])
		ZjCj=ZjCj-C[i]
	        ZC.append(ZjCj)							#agrega el resultado y obtenemos nuestro Zj-Cj inicial
	return ZC								#regresa el vector Z-C

##</Encontrar Zj-Cj>###################################################################################################

##<Encontrar Vector Cb>###################################################################################################
def GetCB(C,ColBase):
	Cb=[]									#este vector contendra las posiciones
	for NColBase in ColBase :						#en el vector ColBase estan las posiciones de los ei.
		for i in range(len(C)):							#y para cada una de esas posiciones de la columna vamos a
			if i==NColBase :						#recorrer el vector C
				Cb.append(C[i])						#si estamos en la posicion de e1, esa se agrega primero a CB y asi
	return Cb									#sucesivamente
##</Encontrar Vector Cb>###################################################################################################

##<Creación de la matriz A>###################################################################################################
def MatrixA(restricciones,C,M,min_max):
	A=[]
	XB=[]
	D=[]

		##agrega a la matrix A los valores de los coeficientes de las retriscciones
	for rest in restricciones :
		y=[]
		j=0
		for i in range(len(rest)):						#Recorre toda la cadena de la restriccion
			if rest[i]=="+" or rest[i]=="-":				#Indicador de que se ha encontrado un signo de adicion, es decir acontinuacion hay un coeficiente
				j=i
			if rest[i]=="X" or rest[i]=="x":				#Agrega al vector y el coeficiente que se encontro
				y.append(float(rest[j:i]))
				j=i
			if rest[i]=="<" or rest[i]==">" or rest[i]=="=" : 		
				D.append(rest[i:i+2])					#agrega a D la restriccion para agregar las H, A
				XB.append(float(rest[i+2:]))				#Hace arreglo con los valores de las restricciones
				break
		if y != [] : A.append(y)


		##Agrega a A los coeficientes de las  variables de holgura
	for i in range(len(D)):								#Recorre las direcciones de las restricciones
		if D[i] == "<=":							
			for j in range(len(D)):						#Recorre las ecuaciones
				if j ==i :						#Si es la ecuacion correspondiente a la restriccion
					A[j].append(1)						#apendisa 1
					C.append(0)
				else :
					A[j].append(0)						#Otro caso apendiza 0
		elif D[i] == ">=":							#Análogo
			for j in range(len(D)):
				if j == i :
					A[j].append(-1)
					C.append(0)
				else :
					A[j].append(0)


		##Agrega a A los coeficientes de las  variables ARTIFICIALES
	for i in range(len(D)):								#Recorre las direcciones de las restricciones
		if D[i] == "==":							
			for j in range(len(D)):						#Recorre las ecuaciones
				if j ==i :						#Si es la ecuacion correspondiente a la restriccion
					A[j].append(1)						#apendisa 1
					if min_max == "M" :
						C.append( -1 * M )
					else :
						C.append( M )
				else :
					A[j].append(0)						#Otro caso apendiza 0
		elif D[i] == ">=":							#Análogo
			for j in range(len(D)):
				if j == i :
					A[j].append(1)
					if min_max == "M" :
						C.append( -1 * M )
					else :
						C.append( M )
				else :
					A[j].append(0)
	


	return A, XB, C

##</Creacion de la matrix A>######################################################

##<Imprimir una matrix>###########################################################
def MatrixPrint(Matrix):
	MatrixFormat=""
	for i in range(len(Matrix)) :
		for j in range(len(Matrix[i])) :
			MatrixFormat = MatrixFormat + str(Matrix[i][j]) + '	'
		MatrixFormat = MatrixFormat + "\n"
	return MatrixFormat
##</Imprimir una matrix>###########################################################

##<Imprimir un vector>###########################################################
def VectorPrint(Matrix):
	MatrixFormat="[ "
	for i in range(len(Matrix)) :
		if i == (len(Matrix) - 1) :
			MatrixFormat = MatrixFormat + str(Matrix[i])
		else :
			MatrixFormat = MatrixFormat + str(Matrix[i]) + ',	'
	return MatrixFormat + " ]"
##</Imprimir un vector>###########################################################

##<Identificar la Base>############################################################
def Base(A):
	B=[]								#inicializa la matriz B. esta matriz contiene las ORDENADAS posiciones de la base canonica
	CB=[]								#Contiene las posiciones de la base ordenadas de derecha a izquierda
	for j in range(len(A[1])-1,0,-1) : 				#Recorremos las columnas de la matriz a del final al inicio
		Bt=[]							#Bt contiene la columna i-esima de la matriz A
		for i in range(len(A)) : 				#Asignacion de Bt
			Bt.append(A[i][j])
		if Bt.count(1) == 1 :					#si en Bt solo se encuentra un 1, es decir Bt=ei se agrega suposicion a la lista CB
			CB.append(j)
		if len(CB)>=len(A) :					#Condicion de parada, si de derecha a izquierda hay mas vectores ei que los que
			break						#la base canonica del problema contine sale deja de buscar vectores ei

	for i in range(len(A)):						#Recorre los renglores de A
		for j in CB :						#^solo en las columnas en las que se encontraron vectores ei
			if A[i][j] == 1 :				#y ordena para tener la matriz canonica
				B.append(j)

	return B
##</Identificar la Base>############################################################

##<Identificar variables de entrada y salida>############################################################
def EntradaSalida(A,ZC,XB,min_max) : 
	entrada = 0							#iniciamos la entrada, es decir el valor j en cero
	salida = 0
	if min_max == "M" :
		for i in range(1,len(ZC)) :					#recorre todo ZC empezando por la segunda posicion, variando i
			if ZC[ i ] <= ZC[ entrada ] :				#compara i con la posicion de entrada,para la primera vuelta ZC[1] con ZC[0]
				entrada = i					#si la posicion i es menor a la posicion anterior se reasigna la entrada
	else :
		for i in range(1,len(ZC)) :					#recorre todo ZC empezando por la segunda posicion, variando i
			if ZC[ i ] >= ZC[ entrada ] :				#compara i con la posicion de entrada,para la primera vuelta ZC[1] con ZC[0]
				entrada = i					#si la posicion i es menor a la posicion anterior se reasigna 

	for j in range(len(A)) :					#protege de dividir por cero				
		if A[ j ][ entrada ] > 0 :
			salida = j
		break

	for j in range(1,len(A)) :					#analógo pero con la divicion de XB/Yij, cuando se encuentra el menor se leasigna a 
		if A[ j ][ entrada ] > 0 :				#Protege de dividir por cero
			if XB[ j ]/A[ j ][ entrada ] <= XB[ salida ]/A[ salida ][ entrada ] :
				salida = j
	
	return entrada, salida
##</Identificar variables de entrada y salida>############################################################

##<Calcular las ecuaciones de transformacion>############################################################
def Ecuaciones_Trans(A,XB,ZC,entrada,salida) :
	
	if wo == False :
		print "Entra: " + str(entrada) + " Sale: " +str(salida) +"\nYij:"
	else :
		output.write("\n\nEntra: " + str(entrada) + " Sale: " +str(salida) +"\nYij:\n")

	Yij=[]
	##Calcular Y######
	for i in range(len(A)) :					#recorre TODA la matriz A, es decir todos los vectores Yij
		SYij=[]
		if i != salida :					#cuando estamos en un renglon k != de r (de la salida) usamos la formula adecuada
			for k in range(len(A[i])) :
				SYij.append(A[i][k]-(A[salida][k]/A[salida][entrada])*A[i][entrada])	#se guarda el renglon entero en un vector
				ygorro = "^y" + str(i) + str(k) + " = y" + str(i) + str(k) + " - y" + str(salida) + str(k) + "/y"+ str(salida) + str(entrada) + "*Y"+ str(i) + str(entrada) +" = "+ str(A[i][k]-(A[salida][k]/A[salida][entrada])*A[i][entrada])
				if wo ==False :
					print ygorro
				else :
					output.write(ygorro + "\n")
			Yij.append(SYij)				#todos los renglones se guardan en una matriz que luego será la nueva A
		else :
			for k in range(len(A[i])) :			#analogamanete cuando k=r
				varsyij = A[salida][k]/A[salida][entrada]
				SYij.append(varsyij)
				ygorro = "^y" + str(i) + str(k) + " = y" + str(salida) + str(k) + "/y"+ str(salida) + str(entrada) + " = " + str(varsyij)
				if wo ==False :
					print ygorro
				else :
					output.write(ygorro + "\n")
			Yij.append(SYij)				#todos los renglones se guardan en una matriz que luego será la nueva A


	##Calcular Zj-Cj######
	if wo == False : 
		print "\nZj-Cj:"
	else : 

		output.write("\nZj-Cj:\n")
	SZC=[]
	for k in range(len(ZC)) :					#calcula todas las Zj-Cj de acuerdo a la formula de cambio y lo guarda en SZC
		varszc = ZC[k]-(A[salida][k]/A[salida][entrada])*ZC[entrada]
		SZC.append(varszc)		# que se convertira en el nuevo ZC, es decir Zj-Cj
		zcgorro= "^Z" + str(k) + " - C" + str(k) + " = (Z" + str(k) + " - C" + str(k) + ") - ( y" + str(salida) + str(k) + " / y"+str(salida) + str(entrada)+" ) * (Z" + str(entrada) + " - C" + str(entrada) + ") = " + str(varszc)
		if wo == False :
			print zcgorro
		else :
			output.write (zcgorro + "\n")
	
	##Calcular las XB#####
	if wo == False : 
		print "\nXB's:"
	else:
		output.write("\nXB's:")
	SXB=[]
	for i in range(len(XB)) :					#Procedimiento adecuado para las XB. Estas son almacenadas en un vector SXV
		if i != salida :						#que será el nuevo XB
			varsxb=XB[i]-(XB[salida]/A[salida][entrada])*A[i][entrada]
			SXB.append(varsxb)
			xbgorro = "^XB" + str (i) +" = XB" +str(i)+ " - (XB"+str(salida)+" / y"+str(salida)+str(entrada)+" ) * y"+str(i)+str(entrada) +" = " + str(varsxb)
			if wo == False :
				print xbgorro
			else :
				output.write(xbgorro + "\n")
		else :
			varsxb=XB[salida]/A[salida][entrada]
			SXB.append(varsxb)
			xbgorro = "^XB" + str (i) +" = XB"+str(salida)+" / y"+str(salida)+str(entrada) +" = " + str(varsxb)
			if wo == False :
				print xbgorro
			else :
				output.write(xbgorro + "\n")
	
	##Reasignar los resultados de las ecuaciones de transformacion ###########
	return Yij, SZC, SXB						#se regresan Yij, SZC y SXB para su reasignacion
##</Calcular las ecuaciones de transformacion>############################################################

#########################################################  </FUNCIONES> #######################################################






#####################################################      <MAIN>      ################################################
print "\nResolución de PPL, por el metodo Simplex"

#Inicializar variables######
rest=""
restricciones=[]
datos=False
wo=False
############################


##Pidiendo los datos desde un archivo

for argumento in sys.argv :
	if argumento == "-V" or argumento == "--about":
		print	"""Resolución del Metodo Simplex Version 1.2 RC

Desarrollado por:

>	Ramirez Vasquez Indira 131162
>	Rivas Espinoza Arturo
>	Reyes Conde Ivan 131621

Oct 2008
			"""
		sys.exit()

	if argumento[:2] == "-S" :
		f = open(argumento[3:],'r')			##Abre el archivo indicado por el argumento -S
		fuente=f.readlines()				##Crea un arreglo con las lineas del archivo
		f.close()					##Cierra el archivo

		min_max=fuente[0][0]				##Asigna el minmax
		eq=fuente[1][:-1]				##Asigna la funcion objetivo
		for i in range(2,len(fuente)-1) :
			restricciones.append(fuente[i][:-1])	##Asigna las restricciones
		datos=True					##Levanta una bandera para decir que ya se tienen todos los datos


##Pidiendo los datos por linea de comando
if datos == False :
	##Pedir funcion a optimizar
	min_max = raw_input("Es un problema de Maximización/minimización? (M/m) ")

	while (min_max.upper() != "M") :
		min_max = raw_input("Opción no valida, Maximización o minimizacion? (M/m)")

	if min_max == "M":
		print "\nProblema de Maximizacion"
	elif min_max =="m":
		print "\nProblema de minimizacion"

	eq= raw_input("\nIntroduzca la ecuación Z a optimizar\nZ=")

	##Pedir restricciones

	print "\n\nIntroduzca las restricciones\n"
	while rest != "." :							#mientras no se le alimente con un '.' sigue agregando restricciones
		rest=raw_input()
		if rest !="." :
			restricciones.append(rest)


for argumento in sys.argv :
	if argumento[:2] == "-O" :
		output=open(argumento[3:],'w')
		wo=True


#####REALIZANDO LAS OPERACIONES


##Busqueda de vectores necesarios
C=GetVectorC(eq)							#Encontrando C, agregando h's y A's
A, XB, C = MatrixA(restricciones,C,10000,min_max)			#Buscando la primera matriz A, con M=10,000. TODO pedir M
ColBase = Base(A)							#Buscando y ordenando las columnas con ei's es decir donde esta la base canonica
Cb = GetCB(C,ColBase)							#a partir de las posiciones de ei encuentra Cb
ZC = GetZjCj(A,C,Cb)							#calcula la primera Zj-Cj

PTabla= "\n\nPrimera tabla:\n" + (MatrixPrint (A)) + "\nZj-Cj inicial:	" + (VectorPrint(ZC)) + "\nXB inicial:	" + (VectorPrint(XB))
if wo == False :
	print PTabla
	raw_input ("\nPresione Enter para continuar\n\n")
else :
	output.write(min_max + " Z = " + eq + "\n")
	output.write("s.a.\n")
	for rest in restricciones :
		output.write(rest + "\n")
	output.write(PTabla)


#criterio de parada del ciclo de iteraciones
if min_max == "M" :
	while [val for val in ZC if val < 0] :					#sihay un valor en ZC que sea menor que CERO 
		entrada,salida = EntradaSalida(A,ZC,XB,"M")					#realiza una nueva iteracion
		A, ZC, XB=Ecuaciones_Trans(A,XB,ZC,entrada,salida)
		if wo == False : raw_input("\nPresione Enter para continuar\n\n")
else :
	while [val for val in ZC if val > 0] :					#sihay un valor en ZC que sea MAYOR que CERO 
		entrada,salida = EntradaSalida(A,ZC,XB,"m")					#realiza una nueva iteracion
		A, ZC, XB=Ecuaciones_Trans(A,XB,ZC,entrada,salida)
		if wo == False : raw_input("\nPresione Enter para continuar\n\n")

UTabla = "\n\nSe ha encontrado el Óptimo.\nUltima tabla:\n" + (MatrixPrint (A)) + "\nZj-Cj final:	" + (VectorPrint(ZC)) + "\nXB final:	" + (VectorPrint(XB))
if wo==False :
	print UTabla
else :
	output.write(UTabla)
	output.close()
	print "\nSe ha encontrado una solucion optima y se escribio en " + output.name + "Gracias por usar nuestro Software"
