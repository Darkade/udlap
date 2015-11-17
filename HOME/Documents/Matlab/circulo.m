%Circulo; creando un circulo de radio 1
%01/20/09
theta = linspace (0,2*pi,100); % creando el vector theta
x=cos(theta); y=sin(theta); % que son los vectores de coordenadas
plot (x,y,'-.r',0,0,'+y',.5,.5,'o')
hold on
plot(1,0,'o')
axis('equal')
title('Circulo de radio unitario')

