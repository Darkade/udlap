%Circulo; creando un circulo de radio 1
%creacion de un circulo de radio arbitrario r, y centro 0,0
%01/20/09
r=input('Radio del circulo: ')
theta = linspace (0,2*pi,100); % creando el vector theta
x=cos(theta); y=sin(theta); % que son los vectores de coordenadas
plot (r*x,r*y,'-.r',0,0,'+y',.5,.5,'o',x,y)
hold on
plot(1,0,'o')
axis('equal')
title('Circulo de radio unitario')

