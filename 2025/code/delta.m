% series de Fourier tiempo continuo 

% numero de armonicas a calcular
N = 32;

% Periodo
T = 4.0;    
% Parte del periodo que la signal es 1
T1 = 1.0;
% Desplazamiento
Td = 2.0;

a0 = T1 / T;

k = (1:N)';
ak = T1/ T * ...
(1 - exp(-j * k * 2 * pi * T1 / T)) ./ ...
(j * k * 2 * pi * T1/ T);

bk = ak .* (1 - exp(-j * k * 2 * pi * Td/T));

% Dominio de la frecuencia
% preparando la grafica
K = (-N:1:N)';
akn = conj(ak(end:-1:1));
AK = [akn;a0; ak];
magAK = sqrt(conj(AK).*AK);

bkn = conj(bk(end:-1:1));
BK = [bkn;0; bk];
magBK = sqrt(conj(BK).*BK);

h1 = figure(1); clf
subplot(3, 1, 1);
stem(K, real(BK));
xlabel('k');
ylabel('real bk')
subplot(3, 1, 2);
stem(K, imag(BK));
xlabel('k');
ylabel('imag bk')
subplot(3, 1, 3);
stem(K, magBK);
xlabel('k');
ylabel('norm bk')
print('dominio_frecuencia_delta.png')

% Dominio del tiempo
% Preparando la grafica
puntos=1000;
t = linspace(0, 4*T,puntos);
xt = zeros(size(t));
for n=1:puntos,
        expo = exp(j * K' * 2 * pi * t(n) / T);
        xt(n) = expo * BK;
end;
 
 h2 = figure(2); clf
 plot(t, xt)
 xlabel('t')
 ylabel('x(t)')
 print('dominio_tiempo_delta.png')