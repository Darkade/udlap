a=-2
b=2
observaciones=list()
for i in range(0,200000):
	r=random()
	f=exp((b-a)*r+a)*(b-a)
	observaciones.append(f)
print "La aproximacion es:",sum(observaciones)/len(observaciones)
