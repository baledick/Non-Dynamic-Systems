
clear all

global a h

%my first integration  xdot = x(1-x)
% x(i+1)=x(i)+ delta *x(i)*(1-x(i));
a=1;

dt=0.1;
Nt=1000;
x=zeros(Nt,1);t=x;


H=[linspace(0,1/4,31),linspace(1/4+1.e-05,1/3,41)];


for ib=1:length(H);
    h=H(ib);
    
    x(1)=1.1;
    t(1)=0;
    
for ia=2:Nt;
    t(ia)=(ia-1)*dt;
    y=x(ia-1);
    x(ia)=x(ia-1)+dt*xdoth(y);
    if x(ia)<0;x(ia)=0;end;
end;

xt(ib)=x(Nt);
if H(ib)>1/4;
    figure(35)
    plot(H(1:ib),xt(1:ib),'r',H(1:31),(1+sqrt(1-4*H(1:31)))/2,'--b','Linewidth',2)
    hold on
    plot(H(31:ib),0*H(31:ib),'--b','Linewidth',2)
    hold off
    xlabel('t','Fontsize',24)
    ylabel('x(t)','Fontsize',24)
    drawnow
else;
    figure(35)
    plot(H(1:ib),xt(1:ib),'r',H(1:ib),(1+sqrt(1-4*H(1:ib)))/2,'--b','Linewidth',2)
    xlabel('t','Fontsize',24)
    ylabel('x(t)','Fontsize',24)
    title('Logistic')
    drawnow
end;

    figure(36)
    plot(t(1:Nt),x(1:Nt),'r','Linewidth',1)
    xlabel('t','Fontsize',24)
    ylabel('x(t)','Fontsize',24)
    title('Logistic')
    hold on

end;

   
    



