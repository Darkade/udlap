% trayectoria circular de un punto en movimiento dejando su "cola"
% -------------------
clf
xlabel('trayectoria circular de un punto en movimiento y su cola')
theta = linspace(0,2*pi,1000); % creando un vector de ángulos
x = cos(theta); y = sin(theta); % generando coordenadas x-y del punto ...
% a lo largo de la ruta
% Si a y b son escalares, line (a,b) crea un punto de coordenadas (a,b)
% Si x1 x2 y1 y2 son escalares, line([x1 x2],[y1 y2]) crea un segmento
% que une (x1,y1) con (x2,y2)
hpunto=line(x(1),y(1),'marker','o','markersize',8,'erasemode','xor'); 
% (dibuja un punto en la posición inicial y le asigna un "handle". Con ...
% erasemode = xor borra el viejo punto cuando se dibuja el nuevo)
hcola = line(x(1),y(1),'marker','.','color','r','erasemode','none');
% (dibuja la cola) (Con erase = none no borra los puntos anteriores)
axis([-1 1 -1 1]); axis('square');
for k = 2:length(theta)
    set(hpunto,'xdata',x(k),'ydata',y(k));
    set(hcola,'xdata',x(k),'ydata',y(k));
    drawnow  % dibuja el punto en la nueva posición
end