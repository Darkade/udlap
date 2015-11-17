% Script que resuelve la ecuacion diferencial
%  y=3*y/x+y^2/x^2

disp('2. Resolver la ecuacion diferencial')
disp('     y=1 + 3*y/x + y^2/x^2')
disp('   con y(1)=0')
disp('   obtener y(2)')

[x y]=ode23(@(x,y) 1 + 3*y/x + y^2/x^2,[1 2],0);        %resolviendo la ecuacion con ode23. La función es definida ahi mismo con @

disp(' ');
disp(strcat('Valor de y(2)=',num2str(y(length(x)))));

plot(x,y,x,y,'go');
title('Solución de la ecuación diferencial')
text(1.3,1,'Solución ->')
text(1.87,4.5,'y(2) ->')