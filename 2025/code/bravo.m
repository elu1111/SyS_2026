% series de Fourier tiempo continuo 

% numero de armonicas a calcular
N = 32;

% Periodo
T = 2.0;    
% Parte del periodo donde x(t) == 1
T1 = 0.7 * T;
% Demora
Td = 0.4 * T;

a0 = T1 / T;

k = (1:N)';
ak =  T1/ T  * exp(-j * k * 2 * pi * Td/T) .* ...
(1 - exp(-j * k * 2 * pi * T1 / T)) ./ ...
(j * k * 2 * pi * T1/ T);

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
print('dominio_frecuencia_bravo.png')
% Dominio del tiempo
% Preparando la grafica
puntos=500;
t = linspace(0, 4*T,puntos);
xt = zeros(size(t));
for n=1:puntos,
        expo = exp(j * K' * 2 * pi * t(n) / T);
        xt(n) = expo * AK;
end;
 h2 = figure(2); clf
 plot(t, xt)
 xlabel('t')
 ylabel('x(t)')
 print('dominio_tiempo_bravo.png')