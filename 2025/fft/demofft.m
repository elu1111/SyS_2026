Dt = 1/200;
n = 0:1023;
xn = 1/2 + 1/4 * cos(2 * pi * 50 * n * Dt);
[Xw, w] = myfft(xn, Dt);
figure(1); plot(n*Dt,xn,'-'); title('xn = 1/2 + 1/4 * cos(2 * pi * 50 * n * Dt);');
figure(2); plot(w,abs(Xw),':*'); title('frecuencia angular (radianes por segundo)');
figure(3); plot(w / (2 * pi), abs(Xw),':*'); title('frecuencia en ciclos por segundo');


