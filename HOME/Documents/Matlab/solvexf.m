function [det_A x]=solvexf(r);
%Esta es una funcíon que calula el determinante y solución para el
%   sistema de ecuaciones
%   [5 2r r;3 6 2r-1;2 r-1 3r][x1 x2 x3]=[2;3;5]
%   Pero para distintos valores de r
%   Esta función solvexf se llama de la siguiente manera:
%   [det_A,x]solvexf(r)
%   donde r es input
%   det_A, x output

A=[5 2*r r;3 6 2*r-1;2 r-1 3*r];
b=[2;3;5];
det_A=det(A);
x=A\b;
