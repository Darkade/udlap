function tabla = temperaturafn(Ti,Ts);

C=[Ti:Ts];
F=(9/5)*C+32;
tabla=[C;F]';