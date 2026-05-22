YB = -0.5;
YT = 1.5;
TL = -10;
TR = 10;
dt = 0.01;
dy = 0.01;
t = TL:dt:TR;
y = YB:dy:YT;
yp1 = 0:dy:1;
tp1 = -ones(size(yp1)) * T1;
tp2 = -T1:dt:T1;
yp2 = ones(size(tp2));
yp3 = 0:dy:1;
tp3 = ones(size(yp3)) * T1;
tp = [tp1, tp2, tp3];
yp = [yp1, yp2, yp3];
figure(1); plot(tp, yp, 'b.', t, zeros(size(t)), 'k.', zeros(size(y)), y, 'k.')
legend('pulse')
xlabel('t');
ylabel('p(t)');
axis([TL, TR, YB, YT])
print('tfone.eps', '-deps')

WL = -100;
dW = 0.01;
WR = -WL;
w = (WL:dW:WR) / pi * T1 / 2;
yw = sinc(w);
y = (min(yw) * 1.5:0.01:max(yw) * 1.2);
figure(2); plot(w, yw, 'b.', w, zeros(size(w)), 'k.', zeros(size(y)), y, 'k.');
axis([min(w), max(w), min(yw) * 1.5, max(yw) * 1.2]);
print('tftwo.eps', '-deps')

ypa = 0:dy:1;
tpa = -ones(size(ypa)) * 13.0;
tqa = -13.0:dt:-11.0;
yqa = ones(size(tqa));
yra = 0:dy:1;
tra = -ones(size(yra)) * 11.0;
tsa = -11.0:dt:-7.0;
ysa = zeros(size(tsa));

ypb = 0:dy:1;
tpb = -ones(size(ypb)) * 7.0;
tqb = -7.0:dt:-5.0;
yqb = ones(size(tqb));
yrb = 0:dy:1;
trb = -ones(size(yrb)) * 5.0;
tsb = -5.0:dt:-1.0;
ysb = zeros(size(tsb));

ypc = 0:dy:1;
tpc = -ones(size(ypc)) * 1.0;
tqc = -1.0:dt:1.0;
yqc = ones(size(tqc));
yrc = 0:dy:1;
trc = ones(size(yrc)) * 1.0;
tsc = 1.0:dt:5.0;
ysc = zeros(size(tsc));

ypd = 0:dy:1;
tpd = ones(size(ypd)) * 5.0;
tqd = 5.0:dt:7.0;
yqd = ones(size(tqd));
yrd = 0:dy:1;
trd = ones(size(yrd)) * 7.0;
tsd = 7.0:dt:11.0;
ysd = zeros(size(tsd));

ype = 0:dy:1;
tpe = ones(size(ype)) * 11.0;
tqe = 11.0:dt:13.0;
yqe = ones(size(tqe));
yre = 0:dy:1;
tre = ones(size(yre)) * 13.0;
tse = 13.0:dt:17.0;
yse = zeros(size(tse));


y = [ypa, yqa, yra, ysa, ypb, yqb, yrb, ysb, ypc, yqc, yrc, ysc, ypd, yqd, yrd, ysd, ype, yqe, yre, yse];
Y = (min(y) - 0.1):dy:max(y) + 0.1;
t = [tpa, tqa, tra, tsa, tpb, tqb, trb, tsb, tpc, tqc, trc, tsc, tpd, tqd, trd, tsd, tpe, tqe, tre, tse];
figure(3); plot(t, zeros(size(t)), 'k.', zeros(size(Y)), Y, 'k.', t, y, 'b.');
axis([min(t), max(t), min(y) - 0.1, max(y) + 0.1]);