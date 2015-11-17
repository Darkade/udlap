% Script que calcula la transformada de laplace para la función
%   f(t)= 4t^2 + 7e^(5t) + 2sin(4t)

disp('3. Escriba un script file para calcular la transformada de Laplace para:')
disp('      f(t)= 4t^2 + 7e^(5t) + 2sin(4t)')

syms t;
f=4*t^2+7*exp(5*t)+2*sin(4*t);
lf=laplace(f);
disp(' ')
disp('La transformada es:')
disp(lf);