%script file para ej3
tlapso=[0 1]; y0=1;
[x,y]=ode45('ej3',tlapso,y0);
y_en_1=y(length(x))

tlapso=[1 1.5]; y0=y_en_1;
[x,y]=ode45('ej3',tlapso,y0);
y_en_1_5=y(length(x))
