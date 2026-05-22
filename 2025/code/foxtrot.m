% series de Fourier tiempo continuo 
% ejemplo 9.7.3

% numero de armonicas a calcular
N = 32;

% Periodo
T = 8.0;    
T1 = 0.5;

a0 = 0;

k = (1:N)';
ak =  ...
(1- cos(k * pi * T1/T) ) ./ ...
(j*k * pi);

% Dominio de la frecuencia
% preparando la grafica
K = (-N:1:N)';
akn = ak(end:-1:1);
AK = [conj(akn);a0; ak];
magAK = sqrt(conj(AK).*AK);


h1 = figure(1); clf
subplot(3, 1, 1);
stem(K, real(AK));
xlabel('k');
ylabel('real ak')
subplot(3, 1, 2);
stem(K, imag(AK));
xlabel('k');
ylabel('imag ak')
subplot(3, 1, 3);
stem(K, magAK);
xlabel('k');
ylabel('norm ak')
print('dominio_frecuencia_foxtrot.png')
% Dominio del tiempo
% Preparando la grafica
puntos=5000;
t = linspace(-2*T, 2*T,puntos);
xt = zeros(size(t));
for n=1:puntos,
        expo = exp(j * K' * 2 * pi * t(n) / T);
        xt(n) = expo * AK;
end;
 h2 = figure(2); clf
 plot(t, xt)
 xlabel('t')
 ylabel('x(t)')
 print('dominio_tiempo_foxtrot.png')