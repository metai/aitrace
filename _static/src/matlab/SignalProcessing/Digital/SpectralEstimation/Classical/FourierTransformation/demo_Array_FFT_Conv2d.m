clear all

% ---data
X = [1 2 3 4 5 6; 5 6 7 8 9 10; 9 10 11 12 13 14; 9 10 11 12 13 14; 9 10 11 12 13 14; 9 10 11 12 13 14];
[Xh, Xw, Xc] = size(X);

% ---convolution kernel
K = [0 1 1;-1 0 1;-1 -1 0];


[Kh, Kw] = size(K);

% ---pad (zeros) kernel to the same size of data X
KK = zeros(Xh, Xw);
KK(1:Kh, 1:Kw) = K;

% ---FFT
Y = fft2(X);
H = fft2(KK);
Z  = Y .* H;
O1 = ifft2(Z);

% ---Conv2d valid
O2 = conv2(X, K, 'valid');

% ---Conv2d same
O3 = conv2(X, K, 'same');

disp('---By FFT')
disp(O1)

disp('---By Conv(valid)')
disp(O2)

disp('---By Conv(same)')
disp(O3)

