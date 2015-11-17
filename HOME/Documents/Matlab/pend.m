function zdot= pend(t,z)
%calcula derivadas del sistema del pendulo
% inputs t= tiempo;z=[z(1;z(2))] =[theta;thetadot]
% output: zdot = [z(2); -w^2 sin(z(1))]
wcuad =1.56; %especifica %un valor para w^2
zdot=[z(2);-wcuad*sin(z(1))];
