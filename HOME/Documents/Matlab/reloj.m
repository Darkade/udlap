%Programa que saluda, presenta la fecha, la hora
%con disp, fix, clock, data
disp('Cant let you do that starfox')
disp('Hoy es'), disp(date)
fechayhora = fix(clock);
hora=int2str(fechayhora(4));
minutos=int2str(fechayhora(5));
if minutos < 10
    minutos=['0',int2str(minutos)];
end
horaex=[hora,':',minutos];
disp(horaex)
