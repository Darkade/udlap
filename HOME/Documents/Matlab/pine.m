function [t]=pine(n)
%Funcion que devuelve si un número es par, impar, o no entero
    if floor(n)~=n              % Primero comprueba si el número es o no es entero,
                                %    comparando la parte entera del número
                                %    con el mismo
        t='No Entero';          
    else                        % Si el número fuera entero se procede a decir si es par o impar
        if mod(n,2)==0          % Si el modulo de numero entero entre 2 es cero entonces es par
            t='Par';
        else                    % En otro caso el número entero debe ser impar
            t='Impar';          
        end 
    end
    
    
        