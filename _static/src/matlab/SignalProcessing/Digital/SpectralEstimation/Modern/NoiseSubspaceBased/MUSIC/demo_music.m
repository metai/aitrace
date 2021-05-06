
N = 64; % size of data autocorrelation matrix
Nx = 64; % size of data
t = 0:Nx-1;

f = [0.2, 0.3, 0.8, 1.2]; % frequency of sig
A = [1, 1, 1, 1]; % Amplitude of sig
phy = pi/3; % intial phase of sig

noise = 0.5*randn(1, Nx); % White noise with unit variance

M = length(f);

%% gen sig data

x = sum(exp(1j*pi*f'*t + phy)) + noise;

%% compute  Autocorrelation matrix
rx = xcorr(x, 'coeff');

Rx = toeplitz(rx(Nx:Nx+N-1)); % Autocorrelation matrix

%%  compute eigenvectors
[v, d] = eig(Rx);

V = v(:, M+1:N:N); % Noise eigenvectors

%% compute MUSIC

[y, i] = sort(diag(d));
Px = 0;
K = 1024;
k = 0:K-1;
omega = k*2*pi/(K-1); % Eigenspectrum

for j=1:N-M
    Px = Px + abs(fft(v(:, i(j)), K));
end

Px = flipud(Px);
PEF = 1./Px;
Sx = -20*log10(Px);
sigma = sum(y(1:N-M)) / (N-M);


figure
subplot(121)
plot(abs(fft(x)))
subplot(122)
plot(1./Px)


figure
subplot(121)
pmusic(rx, 4, 'whole')
subplot(122)
plot(Px)
grid on
