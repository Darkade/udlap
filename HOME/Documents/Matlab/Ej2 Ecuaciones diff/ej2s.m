%Script file par ej2.m
tlapso =[1 2]; y0=1;
[x,y]=ode23('ej2',tlapso,y0);
xf=length(x); %<<por aquello>> de xfinal
y_en_2=y(xf);
tlapso=[2 5]; y0=y_en_2;
[x,y]=ode23('ej2',tlapso,y0);