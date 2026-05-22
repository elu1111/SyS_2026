function [Xw, w] = myfft(xn, Dt);
# xn muestras en el dominio del tiempo
# Dt tiempo de muestreo
# Xw transformada rapida de Fourier
# w vector frecuencia
N = length(xn);
Xw = fftshift(fft(xn)) / N;
w = 2 * pi * ((1:N) - ceil(N/2)) / N / Dt;

end
