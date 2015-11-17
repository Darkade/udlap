%Script file que resuelve el sistema de ecuaciones no lineales
%   x^3 + ysin(y) - x + 2=0
%         xy + e^(xy) - 5=0
disp('3. Resolver el sistema de ecuaciones no lineales');
disp('     x^3 + ysin(y) - x + 2=0');
disp('           xy + e^(xy) - 5=0');

sol=solve('x^3+y*sin(y)-x+2=0','x*y+exp(x*y)-5=0');     %Resolviendo el sistema de ecuaciones con el comando solve
x=sol.x;y=sol.y;                                    %Obteniendo los valores de x e y a partir de la matriz sol

disp('Los valores de x e y son:');
x
y
