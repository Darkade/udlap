%Script que calcula el area en la region acotada por
%y=x
%y=x^3
disp('1. Graficar la región acotada por las curvas dadas y hallar el area de la región.');
disp('      y = x; y = x^3');


area = quad(@(x) x-x.^3,0,1);                                   %obtenemos el area delimitada por las funciones

syms x;                                                         %Definimos x como simbolica
ezplot(x);hold on;ezplot(x^3);axis([0 5 0 5]);                  %Usando ezplot para graficarlas funciones

x2=[linspace(0,1,10) linspace(0,1,10)];                         %creando los vectores que usaremos con fill
y2=[linspace(0,1,10)  linspace(0,1,10).^3];
fill(x2,y2,'r');                                                %usamos fill para rellenar el area delimitada por los vectores

title('Region acotada por x, x^3');xlabel('x');ylabel('y');
text(1,.9,'<- Region acotada por y = x; y = x^3')
text(1.5,.5,strcat('El area de la region es:  ',num2str(area)))

hold off;

disp(strcat('El area de la región es:  ',num2str(area)));

