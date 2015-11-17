from random import random
from math import sqrt, exp, log, sin, cos,pi,factorial

class continuas:
	"""Clase para simular variables aleatorias Continuas. Incluye las distribuciones: normal (metodo polar y muller), exponencial, gamma."""
	def polar(self):
		S=2
		while S > 1:
			v1=2*random()-1
			v2=2*random()-1
			S=v1**2+v2**2
		fact=sqrt(-2*log(S)/S)

		return [fact*v1,fact*v2]

	def muller(self):
		f1=sqrt(-2*log(random()))
		f2=2*pi*random()
		return [f1*cos(f2),f1*sin(f2)]

	def exponencial(self,l):
		return -1.0/l*log(random())

	def gamma(self,k,l):
		return sum([self.exponencial(l) for i in range(0,k)])

	def beta(self,a,b):
		x=self.gamma(a,1)
		y=self.gamma(b,1)
		return x/(x+y)
	def triangular(a,b,c):
		U=random()
		Fc=float((c-a))/(b-a)
		if U<=Fc:
			return a+sqrt(U*(b-a)*(c-a)) 
		else:
			return b-sqrt((1-U)*(b-a)*(b-c))


class discretas:
	"""Clase para simular variables aleatorias discretas. Incluye: Uniforme discreta, bernoulli, binomial, poisson, geometrica, binomial negativa"""
	def uniforme_d(self,n):
		return int(n*random())+1

	def bernoulli(self,p):
		return int(random()>p)

	def binomial(self,p,n):
		u=random()
		q=1-p
		pr=q**n
		F=pr
		
		x=0
		while u>F:
			x+=1
			pr=pr*(n-x+1)*p/(x*q)
			F+=pr
		return x

	def hipergeometrica(self,M,K,n):
		print "Aun no implementado"
		#f(x)=f(x-1)\frac{(K-x+1)(n-x+1)}{x(M-K-n+x)}
		pass


	def poisson(self,l):
		u=random()
		pr=exp(-1*l)
		F=pr

		x=0
		while u>F:
		     pr=pr*l/(x+1)
		     F+=pr
		     x+=1
		return x

	def geometrica(self,p):
		return int(log(random())/log(1-p)) + 1

	def binomial_neg(self,p,r):
		u=random()
		q=1-p
		pr=p**r
		F=pr

		x=r
		while u>F:
			x+=1
		    #pr=pr*(r+x-1)/x*q
			print pr
			pr=(x*q)/(x+1-r)*pr
			F+=pr
		return x
