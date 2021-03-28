 
function  f=xdotht(x,t)

global a h e

f=a*x.*(1-x)-h*(1+e*sin(t));
%f=sin(pi*x);
