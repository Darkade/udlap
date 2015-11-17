a=[10 2 1;2 20 -2;-2 14 10];    %Definiendo las matrices
b=[- 9 44 22]';                 %Definiendo las matrices

disp('Solución con a\b')
xyz_1=a\b


u=rref([a b]);                  %aplicando rref a la matriz aumentada [a b]
disp('Solución mediante la funcion rref')
xyz_2=u(:,4)


disp('Usando LU para hallar la solucion')

[L,U]=lu(a);