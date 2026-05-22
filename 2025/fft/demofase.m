x1 = [ones(64,1); zeros(64,1)];
x2 = [zeros(32,1); ones(64,1); zeros(32,1)];
Dt = 1;
[X1w, w1] = myfft(x1, Dt);
[X2w, w2] = myfft(x2, Dt);
figure(1); plot(w1, abs(X1w),'.');
figure(2); plot(w2, abs(X2w),'.');
c1 = atan(imag(X1w)./real(X1w));
c2 = atan(imag(X2w)./real(X2w));
figure(3); plot(w1, c1,'.'); axis([-pi,pi,-1,1])
figure(4); plot(w2, c2,'.'); axis([-pi,pi,-1,1])

desfaseA = exp(-I * (1:128)' * 2 * pi * 32/ 128);
desfaseB = X1w ./ X2w;