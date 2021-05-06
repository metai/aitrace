%% generates signal data
t = 0:99;
noise = randn(1, length(t));
x1 = sin(pi/3*t) + 2*sin(pi/4*t) + noise;
x2 = exp(1i*pi/2*t) + 2*exp(1i*pi/4*t) + exp(1i*pi/3*t) + noise;

figure
subplot(131)
%% FFT
periodogram(x1)

%% MUSIC
subplot(132)
R = corrmtx(x1, 12, 'mod');   % Estimate the correlation matrix using
                        % the modified covariance method.
pmusic(R, 3, 'whole')      % Uses the default NFFT of 256.

subplot(133)
pmusic(R, 4, 'whole')      % Use twice the signal space dimension
                        