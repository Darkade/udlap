% Un ajuste lineal (linea recta)
m=[5 10 20 50 100]; % datos de masas (g)
d = [15.5 33.07 53.39 140.24 301.03]; % desplazamientos (mm)
g = 9.81; % g = 9.81 m/(s^2) metros por segundo al cuadrado
F=m/1000*g; % la fuerza del resorte (masa en kgs) en newtons (N)
a = polyfit(d,F,1); % ajusta una recta (poli de 1er orden)
d_fit = 0:10:300; % una partición m+as fina de d
F_fit = polyval(a,d_fit); %  evalúa el polinomio en esta partición más fina
plot(d,F,'o',d_fit,F_fit) % grafica datos de desplazamientos y dos ...
% rectas de ajustes
xlabel('Desplazamiento \delta (mm)'),ylabel('Fuerza (N)') % \delta es ...
% comando de latex para esa letra griega
k=a(1)% es la constante del resorte k=mg/delta y es la pendiente de la recta
text(100,.32,['\leftarrow Constante del Resorte K = ',num2str(k),' N/mm']);
% en la posición (100,.32) del plano coloca con comando latex \leftarrow 
% una flecha hacia la izquierda <--- y el texto que sigue. Con num2str(k)
% convierte la constante k en una representación "string" que es útil al
% etiquetear gráficas.