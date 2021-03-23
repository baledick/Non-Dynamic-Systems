
clear all

global a b
%my first integration  xdot = x(1-x)
% x(i+1)=x(i)+ delta *x(i)*(1-x(i));
a=1;b=1;

dt=0.1;
Nt=100;
x=zeros(Nt,1);t=x;

x(1)=0.5;
t(1)=0;
for ia=2:Nt;
    t(ia)=(ia-1)*dt;
    y=x(ia-1);
    x(ia)=x(ia-1)+dt*xdot(y);
end;

    figure(31)
    plot(t(1:Nt),x(1:Nt),'r',t(1:Nt),2-x(1:Nt),'--b','Linewidth',2)
    xlabel('t','Fontsize',24)
    ylabel('x(t)','Fontsize',24)
    title('Logistic')
    hold on
    %plot(t,0.5*exp(0*t),'--k')
    



