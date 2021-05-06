
Ts = 5;
Fs = 400.0;
n = Ts * Fs;

f1 = 10;
f2 = 25;
f3 = 50;
f4 = 100;

t1 = linspace(0, Ts, n);
x1 = cos(2 * pi * f1 * t1);
t2 = linspace(Ts, 2 * Ts, n);
x2 = cos(2 * pi * f2 * t2);
t3 = linspace(2 * Ts, 3 * Ts, n);
x3 = cos(2 * pi * f3 * t3);
t4 = linspace(3 * Ts, 4 * Ts, n);
x4 = cos(2 * pi * f4 * t4);

t = [t1 t2 t3 t4];
x = [x1 x2 x3 x4];

TW = 500e-3
NW = floor(TW * Fs)


figure
subplot(121)
plot(t, x)
subplot(122)
cwt(x, 1:Fs, 'sym4', 'scal');




