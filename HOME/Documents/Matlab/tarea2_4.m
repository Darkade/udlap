x=[0 2 4 6 8 10 12];
y=[2.4 1.2 0.8 -.4 0 -1.2 -.8];
fit_3=polyfit(x,y,3);
rango=[3 5 7 9 11];
val_3=polyval(fit_3,rango);
plot(x,y,'o',rango,val_3,'xr')