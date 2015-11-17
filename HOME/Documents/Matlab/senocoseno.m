%Seno y coseno imprime las funciones seno y coseno con
% * en los maximos
theta=linspace(0,2*pi,100);
x=cos(theta);y=sin(theta);
plot(theta,x,'r',theta,y,'y',pi/2,1,'*b',0,1,'*b',2*pi,1,'*b');
axis('equal')
xlabel('EJE X'); ylabel('EJE Y');
title('Seno y Coseno')
