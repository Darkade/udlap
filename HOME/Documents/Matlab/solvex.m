
% Este Script file solvex.m resuelve la ecuación
%   [5 2r r;3 6 2r-1;2 r-1 3r][x1 x2 x3]=[2;3;5]
%   Y calcula el determinante de la matriz
A=[5 2*r r;3 6 2*r-1;2 r-1 3*r];
b=[2;3;5];
det_A=det(A)
x=A\b %recordemos que x\y =INV(x)*y
%   det_A, A, B y z son variables que se quedarán en el workspace