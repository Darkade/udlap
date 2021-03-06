%Script que encuentra los maximos y minimos de
% f(x)=x^3-3x +1
disp('1. Encuentre los m�ximos y minimos que tenga la funci�n');
disp('      f(x)=x^3-3x+1')
disp('  usando fminbnd de MATLAB.')

ezplot('x^3-3*x+1');                 %Graficando la funci�n
axis([-3 3 -4 4],'square');
grid;
min1=fminbnd(@(x) x^3-3*x+1,-3,3);
min2=fminbnd(@(x) -1*(x^3-3*x+1),-3,3);
disp(strcat('El minimo esta en:',num2str(min1),' con f(',num2str(min1),') = ',num2str(min1^3-3*min1+1)))
disp(strcat('El m�ximo esta en:',num2str(min2),' con f(',num2str(min2),') = ',num2str(min2^3-3*min2+1)))

text(-1,3,'<-M�ximo (-1,3)')
text(-1,-1,'Minimo (1,-3)->')