
clear all
close all

C = 3e8;
PI = pi;
H = 10e3;
V = 150;
Fc = 5.3e9;
Tp = 2.5e-6;
Kr = 20.0e12;
Fsr = 60e6;
% Fsr = 140.68e6;
% Fsr = 2813.714242e6;
Nr = 320;
Fsa = 100;
Na = 256;
Lr = 12.0;
La = 3.0;

ZeroAzimuth = false
% ZeroAzimuth = true
As = 0 * PI / 180.0;
As = 0.5 * PI / 180.0;
% As = 10.5 * PI / 180.0;
% As = 21.9 * PI / 180.0;
Ad = 30.0 * PI / 180.0;
Ab = 1.325 * PI / 180.0;

Rc = H / sin(Ad);


% Earth Bending Geometry (Vg < Vr < Vs)
Vs = V;  % platform
Vg = 1.0 * V;  % ground
% Linear geometry
Vr = sqrt(Vs * Vg);  % Equivalent velocity


targets = [
    % [-100, 60, 0, 1],
    % [-100, 0, 0, 1],
    % [100, -60, 0, 1],
    [0, 0, 0, 1],
    [180, 60, 0, 1],
    [100, 100, 0, 1],
    % [150, 100, 0, 1],
];

axis = 'm'
% axis = 'n'
% -------------------------------------------

Wl = C / Fc;
Br = abs(Kr) * Tp;
R0 = Rc * cos(As);
Xc = sqrt(R0^2 - H^2);
Yc = Rc * sin(As);
Zc = 0;

SC = [Xc, Yc, Zc];
SA = [-462, 462, -200, 200];
SA = [-200, 720, -200, 200];
% SA = [-200, 200, -200, 200];
% SA = [-10, 10, -200, 200];
ES = [0, Na, 0, Nr];

disp([])
fprintf('\nSC: %f, ', SC);
disp([])
fprintf('\nSA: %f, ', SA);

fprintf('\nDR: %f\n', C / (2 * Br));
fprintf('\nR0: %f\n\n', R0);

Xmin = SA(1) + Xc;
Xmax = SA(2) + Xc;
Ymin = SA(3) + Yc;
Ymax = SA(4) + Yc;


SS = [Xmin, Xmax, Ymin, Ymax];
disp('[Xmin, Xmax, Ymin, Ymax]')
disp([Xmin, Xmax, Ymin, Ymax])
Rnear = sqrt(Xmin^2 + Ymin^2 + H^2);
Rfar = sqrt(Xmax^2 + Ymax^2 + H^2);

fprintf('\n\nRnear %f, Rfar %f: ', Rnear, Rfar);



Rnear = H / sin(Ad + Ab / 2.0);
Rfar = H / sin(Ad - Ab / 2.0);
fprintf('\n\nRnear %f, Rfar %f: ', Rnear, Rfar);

Ynear = Rnear * sin(As);
Yfar = Rfar * sin(As);
Xnear = sqrt((Rnear * cos(As))^2 - H^2);
Xfar = sqrt((Rfar * cos(As))^2 - H^2);

% Xnear = (H / tan(Ad + Ab / 2.0))
% Xfar = (H / tan(Ad - Ab / 2.0))
fprintf('\n\nXnear %f, Xfar %f, Ynear %f, Yfar %f ', Xnear, Xfar, Ynear, Yfar);

SA(1) = Xnear - Xc;
SA(2) = Xfar - Xc;

fprintf('\nSC %f ', SC);
fprintf('\nSA %f ', SA);

% -------------------------------------------

etac = -R0 * tan(As) / Vg;
fetac = 2.0 * Vg * sin(As) / Wl;

disp([etac, fetac])

Tsa = Na / Fsa;

ta = linspace(-Tsa/2.0, Tsa/2.0, Na);
fa = linspace(-Fsa / 2.0, Fsa / 2.0, Na) - fetac;
% fa = linspace(-Fsa / 2.0, Fsa / 2.0, Na);
ta = reshape(ta, [Na, 1]);
fa = reshape(fa, [Na, 1]);


Tsr = 2 * (Rfar - Rnear) / C;
tnear = 2 * Rnear / C;
tfar = 2 * Rfar / C;
disp(['Tsr: ' num2str(Tsr)])
disp(['Tsa: ' num2str(Tsa)])
% tr = linspace(tnear, tfar, Nr);
% tr = linspace(-Tsr / 2.0, Tsr / 2.0, Nr) + tnear;
tr = linspace(-Nr / 2.0, Nr / 2.0, Nr) / Fsr + (tnear + tfar) / 2.0;
fr = linspace(-Fsr / 2.0, Fsr / 2.0, Nr);
tr = reshape(tr, [Nr, 1]);
fr = reshape(fr, [Nr, 1]);

fprintf('Nr = %f, Tsr=%f, Fsr=%f, \nFsr*Tsr=%f, Nr/Tsr=%f MHz\n', Nr, Tsr, Fsr, Fsr*Tsr, (Nr/Tsr)/1e6);

assert(abs(Nr - Tsr*Fsr) < 1, '\n------Wrong settings, Nr != Fsr * Tsr ');

% ------------------------------------------------

nTGs = size(targets, 1);

tas = ta * ones([1, Nr]);
trs = ones([Na, 1])* tr';
disp([size(tas), size(trs)])
targets = bsxfun(@plus, targets, [SC 0]);

Sr = 0;
for n =1:nTGs
	target = targets(n, :);
    disp(target)

   x = target(1); y = target(2); z = target(3); G = target(4);

    R = sqrt(H^2 + x^2 + (y - V * tas).^2);

    % P = hstack((zeros((Na, 1)), V * ta, ones((Na, 1)) * H))
    % T = matmul(ones((Na, 1)), reshape(target[0:3], (1, 3)))
    % R = sqrt(sum(square(P - T), 1))

    Wr = abs(trs - 2 * R / C) < (Tp / 2.0);

    Aeta = atan((tas - etac) * Vg / R0);
    BWa = 0.886 * Wl / La;
    Wa = sinc(0.886 * Aeta / BWa);
    Wa = Wa.^2;

    % Wr = 1
    % Wa = 1

    Sr = Sr + G .* Wr .* Wa .* exp(-1j * 4 * PI * Fc * R / C + 1j * PI * Kr * (trs - 2 * R / C).^2);
end
disp('Simulation is done!')


RD = fftshift(fft(fftshift(Sr, 1), [], 1), 1);

% F2D = fft2(Sr)
F2D = fft(RD, 2);

cmap = 'jet';
% cmap = 'gray'

if axis == 'm'
    xx = linspace(SA(1), SA(2), Nr);
    yy = linspace(SA(4), SA(3), Na);
end

if axis == 'n'
    xx = linspace(1, Nr, Nr);
    yy = linspace(1, Na, Na);
end

figure()
subplot(321)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('Time domain (amplitude)')
subplot(322)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('Time domain (phase)')

subplot(323)
imagesc(xx, yy, abs(RD))
xlabel('Range')
ylabel('Azimuth')
title('RD domain (amplitude)')
subplot(324)
imagesc(xx, yy, angle(RD))
xlabel('Range')
ylabel('Azimuth')
title('RD domain (phase)')


subplot(325)
imagesc(xx, yy, abs(F2D))
xlabel('Range')
ylabel('Azimuth')
title('2D frequency domain (amplitude)')
subplot(326)
imagesc(xx, yy, angle(F2D))
xlabel('Range')
ylabel('Azimuth')
title('2D frequency domain (phase)')



% ------------------------------------------------------

if ZeroAzimuth
    hh = exp(1j * 2.0 * pi * fetac * fa);
    Has = repmat(hh, [1, Nr]);
    Sr = Sr .* Has;
end

% ---range compression

frs = ones([Na, 1]) * fr';
Hrs = exp(1j * PI * frs.^2 / Kr);

Sr = fftshift(fft(fftshift(Sr, 2), [], 2), 2);
Sr = Sr .* Hrs;
Sr = ifftshift(ifft(ifftshift(Sr, 2), [], 2), 2);

figure()
subplot(321)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After range compression (amplitude)')
subplot(322)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After range compression (phase)')


% ---azimuth FFT
Sr = fftshift(fft(fftshift(Sr, 1), [], 1), 1);
fas = fa * ones([1, Nr]);


% ---way2 SRC

D = sqrt(1 - (Wl^2) * fas.^2 / (4 * Vr.^2));
Ksrc = 2 * Vr.^2 * Fc.^3 * D.^3 ./ (C * R0 * fas.^2);
Km = Kr ./ (1 - Kr ./ Ksrc);

Hsrc = exp(-1j * PI * fas.^2 ./ Ksrc);
Sr = fftshift(fft(fftshift(Sr, 2), [], 2), 2);  % 2D frequency domain
Sr = Sr .* Hsrc;
Sr = ifftshift(ifft(ifftshift(Sr, 2), [], 2), 2);

subplot(323)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After second RC (amplitude)')
subplot(324)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After second RC (phase)')


% ---RCMC


subplot(323)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After second RC (amplitude)')
subplot(324)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After second RC (phase)')



% ---Azimuth compression

Has = exp(1j * 4 * PI * R0 * D * Fc / C);

Sr = Sr .* Has;

Sr = ifftshift(ifft(ifftshift(Sr, 1), [], 1), 1);

figure()

subplot(221)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After azimuth compression (amplitude)')
subplot(222)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('After azimuth compression (phase)')

Sr = flipud(Sr);

subplot(223)
imagesc(xx, yy, abs(Sr))
xlabel('Range')
ylabel('Azimuth')
title('Reconstructed (amplitude)')
subplot(224)
imagesc(xx, yy, angle(Sr))
xlabel('Range')
ylabel('Azimuth')
title('Reconstructed (phase)')

