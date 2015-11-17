% La barra de un péndulo en movimiento bidimensional
% correspondiente al péndulo gobernado por la ec. diferencial
% theta dot dot + sin(theta) = 0.
% ---------
clf
data = [0 0;-1.5 0]; % coordenadas de los extremos de la barra
phi = 0; % orientación inicial
R = [cos(phi) -sin(phi); sin(phi) cos(phi)]; % matriz de rotaciones ...
% En algebra lineal esa matriz rota vectores en plano-xy en sentido ...
% contrario al del reloj en un ángulo phi. Las nuevas coordenadas x',y' ...
% para un punto x,y quedan dadas por:
% x' = x cos(phi) - y sin(phi)
% y' = x sin(phi) + y cos(phi)
data = R*data;
axis([-2 2 -2 2]); axis('equal')
%
% ---- definiición de objetos llamados barra, eje y ruta
%
barra = line('xdata',data(1,:),'ydata',data(2,:), ...
    'linewidth',3,'erase','xor');

eje = line('xdata',0,'ydata',0,'marker','o','markersize',10);
ruta = line('xdata',[],'ydata',[],'marker','.','erasemode','none');
pause
%
theta = pi - pi/1000; % ángulo inicial
thetadot = 0; % velocidad angular inicial
t = 0; % instante inicial
dt = .2; % incremento de tiempo
tfinal = 500; % instante final
%
% --- Método de Euler para integración numérica
%
while (t < tfinal)
    t = t + dt; 
    theta = theta + thetadot*dt;
    thetadot = thetadot - sin(theta)*dt;
    R = [cos(theta) -sin(theta);sin(theta) cos(theta)];
    datanew = R*data;
    %
    % --- cambio de valores de propiedades de los objetos ruta y barra
    set(ruta,'xdata',datanew(1,1),'ydata',datanew(2,1));
    set(barra,'xdata',datanew(1,:),'ydata',datanew(2,:));
    pause
    drawnow;
end