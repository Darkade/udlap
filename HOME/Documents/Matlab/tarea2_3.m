x=[2.2 4.2 6.2 8.2 10.2 12.2 14.2];
y=[10 15 14 16 17 19 20];

%fit_1=polyfit(x,y,1);val_1=polyval(fit_1,x); %Hallando ajuste lineal
%fit_6=polyfit(x,y,6);rango=0:.01:15;val_6=polyval(fit_6,rango); %Hallando ajuste de grado 6
%plot(x,y,'o',x,val_1);
%figure(2)
%plot(x,y,'o',rango,val_6);

plot(x,y,'o')
