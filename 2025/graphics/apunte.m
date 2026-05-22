t = [-pi: 0.5: pi];
xt = cos(2*t);
clf; plot(t,xt); xlabel('t'); ylabel('cos(2*t)'); axis([-pi, pi, -1.2, 1.2]); ;
print('cos2tcoarse.eps', '-deps');

t = [-pi: 0.01: pi];
xt = cos(2*t);
clf; plot(t,xt); xlabel('t'); ylabel('cos(2*t)'); axis([-pi, pi, -1.2, 1.2]); ;
print('cos2t.eps', '-deps');

n = [-10:1:10];
xn = cos(2 * pi * n / 10);
clf; stem(n,xn); axis([-10, 10, -1.2, 1.2]); xlabel('n'); ylabel('cos(2 * pi * n / 10)'); 
print('cosdisc.eps', '-deps');

clf;
subplot(3,1,1); plot(t, exp(t/10)); title('exp(t/10)'); axis([-pi, pi, -0.2, 3]); ;
subplot(3,1,2); plot(t, exp(1/20 * t + 1/3)); title('exp(1/20 * t + 1/3)'); axis([-pi, pi, -0.2, 3]); ;
subplot(3,1,3); plot(t, exp(-1/20 * t + 1/3)); title('exp(-1/20 * t + 1/3)'); axis([-pi, pi, -0.2, 3]); ;
print('contvart.eps', '-deps');

clf;
subplot(3,1,1); plot(t, cos(15*t)); title('cos(15*t)'); axis([-pi, pi, -1.2, 1.2]); ;
subplot(3,1,2); plot(t, cos(15*t+1)); title('cos(15*t+1)'); axis([-pi, pi, -1.2, 1.2]); ;
subplot(3,1,3); plot(t, cos(15*t-1)); title('cos(15*t-1)'); axis([-pi, pi, -1.2, 1.2]); ;
print('contfase.eps', '-deps');

clf;
subplot(3,1,1); plot(t, cos(20*t)); title('cos(20*t)'); axis([-pi, pi, -1.2, 1.2]); ;
subplot(3,1,2); plot(t, cos(15*t)); title('cos(15*t)'); axis([-pi, pi, -1.2, 1.2]); ;
subplot(3,1,3); plot(t, cos(10*t)); title('cos(10*t)'); axis([-pi, pi, -1.2, 1.2]); ;
print('contfrec.eps', '-deps');

n = -10:1:10;
clf;
subplot(3,1,1); stem(n, exp(n/10)); title('exp(n/10)'); axis([-10, 10, -0.2, 3]);
subplot(3,1,2); stem(n, exp(1/20 * n + 1/3)); title('exp(1/20 * n + 1/3'); axis([-10, 10, -0.2, 3]); 
subplot(3,1,3); stem(n, exp(-1/20 * n + 1/3)); title('exp(-1/20 * n + 1/3)'); axis([-10, 10, -0.2, 3]);
print('discvart.eps', '-deps');

clf;
subplot(3,1,1); stem(n, cos(15*n)); title('cos(15*n)'); axis([-10, 10, -1.2, 1.2]); 
subplot(3,1,2); stem(n, cos(15*n+2)); title('cos(15*n+2)'); axis([-10, 10, -1.2, 1.2]);
subplot(3,1,3); stem(n, cos(15*n-2)); title('cos(15*n-2)'); axis([-10, 10, -1.2, 1.2]);
print('discfase.eps', '-deps');

clf;
subplot(3,1,1); stem(n, cos(20*n)); title('cos(20*n)'); axis([-10, 10, -1.2, 1.2]);
subplot(3,1,2); stem(n, cos(15*n)); title('cos(15*n)'); axis([-10, 10, -1.2, 1.2]);
subplot(3,1,3); stem(n, cos(10*n)); title('cos(10*n)'); axis([-10, 10, -1.2, 1.2]);
print('discfrec.eps', '-deps');

clf; plot(t, cos(t)); title('funcion par'); axis([-pi, pi, -1.2, 1.2]); ;
print('contpar.eps', '-deps');

clf; plot(t, sin(t)); title('funcion impar'); axis([-pi, pi, -1.2, 1.2]); ;
print('contimpar.eps', '-deps');

clf; stem(n, n.*n.*n/100); title('n^3/100 funcion impar'); axis([-10, 10, -10, 10]);
print('discimpar.eps', '-deps');

clf; stem(n, n.*n/10); title('n^2/10 funcion par'); axis([-10, 10, -0.2, 10]); 
print('discpar.eps', '-deps');

xpt = cos(5*t) + sin(10*t);
xnt = cos(-5*t) + sin(-10*t);
clf;
subplot(3,1,1); plot(t, xpt); title('cos(5*t)+sin(10*t)'); axis([-pi, pi, -2.4, 2.4]); ;
subplot(3,1,2); plot(t, (xpt+xnt)/2); title('parte par'); axis([-pi, pi, -1.2, 1.2]); ;
subplot(3,1,3); plot(t, (xpt-xnt)/2); title('parte impar'); axis([-pi, pi, -1.2, 1.2]); ;
print('contparimpar.eps', '-deps');

xpn = n.*n.*n/100 + n.*n/10;
xnn = (-n).*(-n).*(-n)/100 + (-n).*(-n)/10;
clf;
subplot(3,1,1); stem(n, xpn); title('n^3/100+n^2/10'); axis([-10, 10, -20, 20]);
subplot(3,1,2); stem(n, (xpn+xnn)/2); title('parte par'); axis([-10, 10, -10, 10]);
subplot(3,1,3); stem(n, (xpn-xnn)/2); title('parte impar'); axis([-10, 10, -10, 10]);
print('discparimpar.eps', '-deps');

xn = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0];
yn = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1];
clf; stem(n,xn); title('Impulso unitario'); axis([-10, 10, -0.2, 1.2]);
print('impunidisc.eps', '-deps');
clf; stem(n,yn); title('Escalon unitario'); axis([-10, 10, -0.2, 1.2]);
print('escunidisc.eps', '-deps');
clf; stem(n+2,xn); title('Impulso unitario desplazado'); axis([-10, 10, -0.2, 1.2]); 
print('impunidiscdesp.eps', '-deps');
clf; stem(n+2,yn); title('Escalon unitario desplazado'); axis([-10, 10, -0.2, 1.2]); 
print('escunidiscdesp.eps', '-deps');
clf; stem(n+2,- xn); title('Impulso unitario desplazado y multiplicado por una constante'); axis([-10, 10, -1.2, 1.2]); 
print('impunidiscdespmult.eps', '-deps');
clf; stem(n+2,yn); title('Escalon unitario desplazado y multiplicado por una constante'); axis([-10, 10, -1.2, 1.2]); 
print('escunidiscdespmult.eps', '-deps');

load 'diversa.mat'
clf; 
t = 0:1:15;
z = zeros(size(t));
subplot(2,1,1); plot(logica(:,1), logica(:,2), t, z) ; title('Representacion logica'); axis([0,15,-0.4, 1.4]);
subplot(2,1,2); plot(continua(:,1), continua(:,2), t, z) ; title('Representacion continua'); axis([0,15,-0.4, 1.4]);
print('diversa.eps', '-deps');

t = [0:0.01:50];
xt = cos(2 * pi/10 * t);
clf; 
plot(t, xt); ; axis([0, 50, -1.2, 1.2]); 
xlabel('t'); ylabel('cos(2 * pi * t / 10)');
title('Funcion periodica x(t) = cos(2 * pi * t / 10)');
print('percont.eps', '-deps');

n = [0:1:50];
xn = cos(2 * pi/10 * n);
clf; 
stem(n, xn); axis([0, 50, -1.2, 1.2]); 
xlabel('n'); ylabel('cos(2 * pi * n / 10)');
title('Funcion periodica x[n] = cos[2 * pi * n / 10]');
print('perdisc.eps', '-deps');

xdn = cos(7/11 * n);
xcn = cos(7/11 * t);
z = zeros(size(t));
clf; 
stem(n, xdn); axis([0, 50, -1.2, 1.2]); hold on;
plot(t(1:20:5000), xcn(1:20:5000),'r-', t, z);
xlabel('n'); ylabel('cos(7 * n / 10)');
title('Funcion discreta no periodica con envolvente continua periodica');
print('noperdisc.eps', '-deps');

t11 = [-3:0.1:0];
x11 = zeros(size(t11));
xe112 = [0:0.1:1]; 
te112 = 0 * ones(size(xe112));
t12 = [0:0.1:1];
x12 = ones(size(t12));
xe123 = [0:0.1:1]; 
te123 = 1 * ones(size(xe123));
t13 = [1:0.1:3];
x13 = zeros(size(t13));
t21 = [-3:0.1:0];
x21 = zeros(size(t21));
xe212 = [0:0.1:1]*2; 
te212 = 0 * ones(size(xe212));
t22 = [0:0.1:1]/2;
x22 = 2 * ones(size(t22));
xe223 = [0:0.1:1]*2; 
te223 = 1/2 * ones(size(xe223));
t23 = [1/2:0.1:3];
x23 = zeros(size(t23));
t31 = [-3:0.1:0];
x31 = zeros(size(t31));
xe312 = [0:0.1:1]*4; 
te312 = 0 * ones(size(xe312));
t32 = [0:0.1:1]/4;
x32 = 4 * ones(size(t32));
xe323 = [0:0.1:1]*4; 
te323 = 1/4 * ones(size(xe323));
t33 = [1/4:0.1:3];
x33 = zeros(size(t33));
clf;
plot(t11,x11,'k',te112,xe112,'k',t12,x12,'k',te123,xe123,'k',t13,x13,'k'); hold on; 
plot(t21,x21,'b',te212,xe212,'b',t22,x22,'b',te223,xe223,'b',t23,x23,'b'); 
plot(t31,x31,'r',te312,xe312,'r',t32,x32,'r',te323,xe323,'r',t33,x33,'r'); 
axis([-3, 3, -0.5, 4.5]);
print('sucimpcont.eps', '-deps');

t11 = [-3:0.1:0];
x11 = zeros(size(t11));
t12 = [0:0.1:1];
x12 = t12 .* ones(size(t12));
t13 = [1:0.1:3];
x13 = ones(size(t13));
t21 = [-3:0.1:0];
x21 = zeros(size(t21));
t22 = [0:0.1:1]/2;
x22 = t22 .* (2 * ones(size(t22)));
t23 = [1/2:0.1:3];
x23 = ones(size(t23));
t31 = [-3:0.1:0];
x31 = zeros(size(t31));
t32 = [0:0.1:1]/4;
x32 = t32 .* (4 * ones(size(t32)));
t33 = [1/4:0.1:3];
x33 = ones(size(t33));
clf;
subplot(3,1,1); plot(t11,x11,t12,x12,t13,x13); axis([-3, 3, -0.5, 1.5]);
subplot(3,1,2); plot(t21,x21,t22,x22,t23,x23); axis([-3, 3, -0.5, 1.5]);
subplot(3,1,3); plot(t31,x31,t32,x32,t33,x33); axis([-3, 3, -0.5, 1.5]);
print('sucesccont.eps', '-deps');

t11 = [-3:0.1:0];
x11 = zeros(size(t11));
x12 = [0:0.1:1];
t12 = zeros(size(x12));
t22 = [0:0.1:3];
x22 = ones(size(t22));
clf;
plot(t11,x11,'k',t12,x12,'k',t22,x22,'k'); axis([-3, 3, -0.5, 1.5]); title('u(t)');
print('limesccont.eps', '-deps');

t = -2:0.001:4;
y = (t >= 0) & (t <= 2);
z = zeros(size(t));
clf;
plot(t, z, '-', t, y); axis([-2, 4, -0.5, 1.5]); title('u(t) - u(t-2)'); 
print('compesccont.eps', '-deps');

n = [-2:1:4];
x = ((n >= 0) & (n < 2)) * 1.0;
clf;
stem(n,x); 
axis([-2, 4, -0.5, 1.5]); 
title('u[n] - u[n-2]');
print('compescdisc.eps', '-deps');

t = [-2:0.1:8];
x = t .* ((t >= 0) & (t <= 2)) + (6 - t) .* ((t >= 4) & (t <= 6));
z = zeros(size(t));
clf;
plot(t,x,t,z); axis([-2,8,-0.5,2.5]);
print('compcontuno.eps', '-deps');

n = [-2:1:8];
x = (n .* n) .* ((n >= 0) & (n < 2)) - (n/4) .* ((n >= 4) & (n < 6));
clf;
stem(n,x); axis([-2,8,-1.5,1.5]);
print('compcontdos.eps', '-deps');

t = [-2:0.01:10];
x1 = ((t >= 0) & (t < 2)) * 1.0;
x2 = (-((t >= 2) & (t < 4))) * 1.0;
x3 = ((t >= 4) & (t < 6)) * 1.0;
x4 = (-((t >= 6) & (t < 8))) * 1.0;
x = x1 + x2 + x3 + x4;
y = t .* x1 + (t - 4) .* x2 + (t - 4) .* x3 + (t - 8) .* x4;
clf; 
subplot(1,2,1); plot(t, x); axis([-2,10,-1.5,1.5]); 
subplot(1,2,2); plot(t, y); axis([-2,10,-0.5,2.5]); 
print('comppreguno.eps', '-deps');

n = [-2:1:10];
x1 = ((n >= 0) & (n < 2)) * 1.0;
x2 = (-((n >= 2) & (n < 4))) * 1.0;
x3 = ((n >= 4) & (n < 6)) * 1.0;
x4 = (-((n >= 6) & (n < 8))) * 1.0;
x = x1 + x2 + x3 + x4;
y = n .* x1 + (n - 4) .* x2 + (n - 4) .* x3 + (n - 8) .* x4;
clf; 
subplot(1,2,1); stem(n, x); axis([-2,10,-1.5,1.5]); 
subplot(1,2,2); stem(n, y); axis([-2,10,-0.5,2.5]); 
print('comppregdos.eps', '-deps');


x1 = zeros(size(n));
x2 = x1;
x1(3) = 1;
x2(5) = 2;
subplot(2,1,1); stem(n, x2); title('Impulso desplazado y multiplicado'); 
subplot(2,1,2); stem(n, x1); title('Impulso unitario');
print('lecture2.eps', '-deps');

