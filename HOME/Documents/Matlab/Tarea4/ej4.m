%Animación de una pelota de tenis

disp('4. Genere un script file una animacion grafica bidimensional ya sea')
disp('   usando movie o con handle graphics')
disp('   Cuando vea la grafica presione cualquier tecla para continuar')

clf
%sol=solve('(-.05)*x^2+.5')
sol=[-3.1622776601683793319988935444327  3.1622776601683793319988935444327];    %Usando Solve hayamos las raices de una parabola

x1=linspace(-6,sol(1),50);          %El dominio de la primera parabola, 
x2=linspace(sol(1),sol(2),75);      %Una raiz de cada una de las parabolas laterales coinciden
x3=linspace(sol(2),6,50);           %con alguna de la parabola del centro

funcion1=(-.025)*(x1+2*sol(2)).^2+.25;      %Evaluando funciones
funcion2=(-.05)*x2.^2+.5;
funcion3=(-.025)*(x3-2*sol(2)).^2+.25;

x=[x1 x2 x3];                               %Añadiendo todos los dominios a un solo vector
y=[funcion1 funcion2 funcion3];             %añadiendo las imagenes a un solo vector

%Ploteando una "cancha" de tenis
plot([0 0],[0 .3],'g','LineWidth',3); hold on
fill([6 6 10 10],[0 1 1 0],'r')
fill([-6 -6 -10 -10],[0 1 1 0],'b')
title('Pelota de Tenis','FontSize',20)

%Creando el Handle

punto=line(x(1),y(1),'marker','o','markersize',12,'erasemode','xor');
axis([-10 10 0 3])

for k = 2:length(x)
    set(punto,'xdata',x(k),'ydata',y(k));
    pause
    drawnow 
end
for k = length(x):-1:2
    set(punto,'xdata',x(k),'ydata',y(k));
    pause
    drawnow
end

