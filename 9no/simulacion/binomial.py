from distribuciones import discretas

X=discretas()

average=lambda o:float(sum(o))/len(o)



observaciones=(lambda m,p,n:[X.binomial(p,n) for i in range(0,m)])(10000000,0.5,10)

print average(observaciones)
