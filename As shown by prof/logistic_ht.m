
clear all

global a h e

%my first integration  xdot = x(1-x)
% x(i+1)=x(i)+ delta *x(i)*(1-x(i));
a=1;
h=1/8;

e=0.2;

Nt=400;
x=zeros(Nt,1);
T=linspace(0,2*pi,Nt);
dt=T(2)-T(1);

X=linspace(0.01,2,101);
for ix=1:length(X);
x0=X(ix);
x(1)=x0;
    
for ia=2:Nt;
    y=x(ia-1);t=T(ia-1);
    x(ia)=x(ia-1)+dt*xdotht(y,t);
    if x(ia)<0;x(ia)=0;end;
end;


    figure(37)
    plot(T,x,'b','Linewidth',2)
    xlabel('t','Fontsize',24)
    ylabel('x(t)','Fontsize',24)
    xlim([0 2*pi])
    title('Logistic')
    hold on
    
    P(ix)=x(Nt);
end
figure(38)
    plot(X,P,'b',X,X,'r','Linewidth',2)
    xlabel('X','Fontsize',24)
    ylabel('P(X)','Fontsize',24)
    title('Poincare Map')
    hold on
    
   
   
    



