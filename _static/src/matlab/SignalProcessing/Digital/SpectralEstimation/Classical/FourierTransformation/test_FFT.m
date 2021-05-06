
f0 = 10;
Tss = -1.0;
Tse = 1.0;
T = Tse-Tss;

Fs = 100;
Ns = Fs*T;

t = linspace(Tss, Tse, Ns);
x = sin(2*pi*f0*t);

y = fft(x);
yshift = fftshift(fft(x));

f = linspace(0, Fs, Ns);
fshift = linspace(-Fs/2, Fs/2, Ns);

figure
subplot(311)
plot(t, x, '-r')
grid on
xlabel('Time/s')
ylabel('Amplitude')
title(['Original Signal(', num2str(f0), 'Hz)'])

subplot(312)
plot(f, abs(y))
grid on
xlabel('Frequency/Hz')
ylabel('Amplitude')
title('FFT of Signal')

subplot(313)
plot(fshift, abs(yshift))
grid on
xlabel('Frequency/Hz')
ylabel('Amplitude')
title('FFT of Signal (shifted)')

