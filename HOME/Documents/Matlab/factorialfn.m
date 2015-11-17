function [r]=factorialfn(n);
%Funcion que calcula el factorial de un numero natural
r=1;                % se inicia r con valor uno porque es el producto neutro
for k=(1:n)         % el contador K va a recorrer una matriz de la forma [1 2 ... n]
    r=r*k;          % r tiene el resultado de hacer el producto de todos los numeros de la matriz
                    %   por ejemplo 5!
                    %       iteracion 1)   r=1*1
                    %       iteracion 2)   r=1*2
                    %       iteracion 3)   r=2*3
                    %       iteracion 3)   r=6*4
                    %       iteracion 3)   r=24*5
end
                    % Termina el for y r tiene el valor 120, se regresa
