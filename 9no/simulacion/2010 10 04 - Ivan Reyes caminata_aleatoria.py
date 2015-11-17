from random import randint

def Caminata_Aleatoria(radio,pasos):
#	posiciones=[]
	p=[0,0,0]

#	posiciones.append(p[:])
	for i in range(pasos):

		x=randint(0,5)
		v=[0,0,0,0,0,0]

		v[x]=1 if x <= 2 else -1
		v=v[:3] if x <= 2 else v[3:]

		p[0]+=v[0]
		p[1]+=v[1]
		p[2]+=v[2]

#		posiciones.append(p[:])
		if sum(x**2 for x in p) > radio**2:
			return 1
	return 0


radio=20
pasos=300
m=10000

salidas=[Caminata_Aleatoria(radio,pasos) for i in range(m)]
probabilidad=sum(salidas)/float(m)

print "\n\nLa probabilidadad de que con",pasos,"pasos se salga de un circulo de radio",radio,"es aproximadamente",probabilidad
