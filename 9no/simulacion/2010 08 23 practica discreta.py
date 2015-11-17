##El arreglo mas y val contienen respectivamente la masa y los valores a asignar
## en cada caso en el caso particular:
##
##		-3,	1/3
##		2,	1/6
##		5,	1/2

from random import random

def ud(mas,val):
	pro=[sum(mas[:i]) for i in range(1,len(mas))]+[1]
	r=random()
	return val[[r<i for i in pro].index(True)]


mas=[1.0/3,1.0/6,1.0/2]
val=[-3,2,5]

#print ud(mas,val)

print "Masa:", mas
print "Valores:", val

m=600000
observaciones=[ud(mas,val) for i in range(0,m)]

for i in range(0,len(val)):
	k=observaciones.count(val[i])
	print "De las",m,"observaciones realizadas",k,"fueron",val[i],"que son el",float(k)/m,"%"
	
	
