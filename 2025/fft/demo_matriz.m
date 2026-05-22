# demo_matriz.m
# Como generar la matriz M de la transformada rapida de Fourier

# Elegimos el periodo
N = 4;

# vector de tiempo discreto
n = (0:(N-1))';

# Constante W
W = exp(-j * 2 * pi / N);

# Matriz M

M = W.^(n*n');

disp('$Matriz M_{4}$')
M

disp('$M_{4}^{t} \cdot M_{4} / N$')
M'*M/N

disp('$M_{4} \cdot M_{4}^{t} / N$')
M*M'/N
