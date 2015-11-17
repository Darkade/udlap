tlapso = [0 20];
z0=[1;0]; % condicion inicial para el vector cero
[t,z]=ode23('pend',tlapso,z0); % se obtiene una matriz z de dos columnas
x=z(:,1);y=z(:,2) % x es la columna uno y y la columna dos
plot(t,x,t,y)
xlabel('t');ylabel('x e y');
figure(2) %abre una nueva ventana figura
plot(x,y) % grafica el "retrato de fase"
xlabel('desplazamiento');ylabel('velocidad');
title('grafica del retrato de fase');