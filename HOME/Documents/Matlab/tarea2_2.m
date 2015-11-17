A=[20 2 1 ;2 20 -2;-2 14 10]; % Definimos la matriz
[V,D]=eig(A); % calculamos sus vectores propios

disp('------------------------Halle los vectores y valores propios de A--------------------------------------')

disp('Vectores propios')
V
disp('Valores propios')
D


disp('------------------------Muestre computacionalmente que los valores propios de A^2')
disp('                        son los cuadrados de los valores propios de A------------------------------------')
disp('Cuadrados de los valores propios de A. D^2')
Dquad=D^2
disp('Valores propios de A^2. eig(A^2)')
[V2 D2]=eig(A^2);
D2
disp('------------------------Calcule los cuadrados de los valores propios de A^2 y')
disp('                        Muestre, computacionalmente, que estos son los valores propios de A^4-------------')
disp('Cuadrados de los valores propios de A^2')
D2quad=D2^2
disp('Valores propios de A^4. eig(A^4)')
[V4 D4]=eig(A^4);
D4