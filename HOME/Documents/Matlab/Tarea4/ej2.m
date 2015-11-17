%Script que encuentra el minimo de:
%   f(x1,x2)=2x1^2 + x2^2 + 2x1x2 + 2x1 + 2x2;

disp('2. Encuentre un m�nimo o un m�ximo local que tenga la')
disp('   siguiente funci�n aplicando fminsearch y fminunc de')
disp('   MATLAB. Grafique la funci�n y su curva de nivel.')
disp('f(x1,x2)=2x1^2 + x2^2 + 2x1x2 + 2x1 + 2x2')


[X1 X2]=meshgrid(linspace(-20,20,100),linspace(-20,20,100));  %Creando un GRID para la funci�n
Z=2.*X1.^2+X2.^2+2.*X1.*X2+2.*X1+2.*X2;                       %Evaluando la funci�n

surf(X1,X2,Z);hold on;                                        %Graficando la funci�n
ezcontour(inline('2*X1^2+X2^2+2*X1*X2+2*X1+2*X2'),[-20 20 -20 20])  %Graficando la curva de nivel


sol=fminunc(@ej2f,[0;0]);                   %Usando fminunc para encontrar los minimos
disp(strcat('El minimo, con fminunc, se encuentra en (',num2str(sol(1)),',',num2str(sol(2)),')' ))
sol=fminsearch(@ej2f,[0;0]);
disp(strcat('El minimo, con fminsearch, se encuentra en (',num2str(sol(1)),',',num2str(sol(2)),')' ))
