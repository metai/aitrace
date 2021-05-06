
f = 100;
Fs = 1000;

T = 0.1;

Ns = Fs*T;

t = linspace(0, T, Ns);

x = cos(2*pi*f*t);

y = fft(x);

f = 0:length(x);
f = f*(Fs/Ns);

figure
subplot(121)
plot(x)
subplot(122)
plot( f, abs(y) )
