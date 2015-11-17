% ejemplo de interpolacion con Basic Fitting
x=[0 0.785 1.570 2.356 3.141 3.927 4.712 5.497 6.283]; % 9 puntos ...
% entre o y 2*pi
y=[0 0.707 1.000 0.707 0.000 -0.707 -1.000 -0.707 -0.000]; % observaciones
xi = linspace(0,2*pi,50); % 50 puntos igualmente espaciados
yi = interp1(x,y,xi,'cubic'); % genera valores yi = f(xi) donde f es la
% función obtenida por interpolación cúbica de los datos x e y.
subplot(2,2,1), plot(x,y,'o'); hold on; plot(xi,yi) % subplot(m,n,p) parte ...
% la ventana de la figura en una matriz m x n y selecciona la p-ésima
% "entrada" para graficar los plots actuales
title('cubic')
yi =interp1(x,y,xi,'nearest');
subplot(2,2,2), plot(x,y,'o'); hold on; plot(xi,yi)
title('nearest')
yi =interp1(x,y,xi,'linear');
subplot(2,2,3), plot(x,y,'o'); hold on; plot(xi,yi)
title('linear')
yi =interp1(x,y,xi,'spline');
subplot(2,2,4), plot(x,y,'o'); hold on; plot(xi,yi)
title('spline')