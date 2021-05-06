import numpy as np
import iprs

PI = np.pi
C = 299792458.0
EPS = 2.2e-16


def sinc_interp(xin, r=1.0):
    xin = np.array(xin)
    N = xin.size
    M = int(N * r)

    u = np.linspace(0, N, M)
    v = np.linspace(0, N, N)
    xout = []
    for i in u:
        xout.append(np.sum(xin * sinc(v - i)))
    return np.array(xout), np.array(u)


def sinc(x):
    x = np.array(x)
    eps = 1.0e-8
    y = np.where(np.abs(PI * x) < eps, 1.0,
                 np.sin(PI * x + eps) / (PI * x + eps))
    return y


def rect(x):
    """
    Rectangle function:
        rect(x) = {1, if |x|<= 0.5; 0, otherwise}
    """
    return np.where(np.abs(x) >= 0.5, 0.0, 1.0)


def chirp(t, T, K_r):
    """
    Create a chirp signal :
        S_{tx}(t) = rect(t/T) * exp(1j*pi*K_r*t^2)
    """
    return rect(t / T) * np.exp(1j * np.pi * K_r * t**2)


# def compute_wa():
#     etac = (Yc+tg[1]) / Vg
#     etac = (Yc+tg[1]) / Vg
#     theta_eta = np.arctan(Vg * (eta - etac) / R0)


def gentgs(targets, Xc, Yc, R0, H, Vr, Vg, Wl, F0, Lr, Kr, Tp, etas, taus):
    for tg in targets:
        tg[0] = tg[0] + Xc
        tg[1] = tg[1] + Yc

    s = []
    for eta in etas:
        s_eta = 0.0
        for tg in targets:
            if R0 is None:
                R0 = np.sqrt(H**2 + tg[0]**2)
            eta_c = tg[1] / Vg
            R_eta = np.sqrt(tg[0]**2 + H**2 + (tg[1] - Vr * eta)**2)
            # print("R_eta, eta, eta_c: ", R_eta, eta, eta_c)

            wrs = rect((taus - 2 * R_eta / C) / Tp) * \
                np.exp(1j * PI * Kr * (taus - 2 * R_eta / C)**2)
            wa = sinc(Lr * np.arctan(Vg * (eta - eta_c) / R0) / Wl)**2
            # footprinty = 2 * np.tan(0.886 * Wl / (2 * Lr)) * R0
            # wa = np.sinc((Vg * eta - tg[1]) / footprinty)**2
            # tt = rect((taus - 2 * R_eta / C) / Tp)
            # print(taus.min(), taus.max())
            # print("tt ----> min, max", tt.min(), tt.max())
            # print(wrs.max())
            # print("wa: ", wa)
            phase_eta = -1j * 4 * PI * F0 * R_eta / C + \
                1j * PI * Kr * (taus - 2 * R_eta / C)**2
            # print(phase_eta.min(), phase_eta.max())
            s_eta = s_eta + tg[2] * wrs * wa * np.exp(phase_eta)
            # print(np.sum(s_eta), tg[2])
        s.append(s_eta)

    s = np.array(s)

    print("s.shape", s.shape)
    print("s.min, s.max", s.min(), s.max())
    return s


def range_dopp1(s, Fsr, Fsa, Kr, Tp, Ka):

    Na, Nr = s.shape
    # =================range compression
    # -----------------Step1: FFT in range
    Sr = np.fft.fftshift(np.fft.fft(np.fft.fftshift(s)))

    # -----------------Step2: Filter in range

    # htaus = iprs.rect(taus / Tp) * np.exp(-1j * PI * Kr * taus**2)

    # Hr = iprs.fftshift(iprs.fft(htaus))

    ftaus = np.linspace(-Fsr / 2.0, Fsr / 2.0, Nr)

    Hr = iprs.rect(ftaus / (np.abs(Kr) * Tp)) * np.exp(1j * PI * ftaus**2 / Kr)

    print("Hr.shape: ", Hr.shape)

    Hrs = np.reshape(np.repeat(Hr, Na), (Nr, Na)).transpose()

    print("===>", Hrs[0, 500], Hrs[1, 500], Hrs[3, 500])
    print("===>", Hrs[10, 0], Hrs[10, 1], Hrs[10, 3])

    # plt.figure()
    # plt.imshow(np.abs(Hrs))

    print(Hrs.min(), Hrs.max())

    Srf = Sr * Hrs

    print("Srf.shape; ", Srf.shape)

    # -----------------Step3: IFFT in range
    Src = np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(Srf)))

    # =================azimuth FFT
    # -----------------Step4: FFT in azimuth
    Sa = np.zeros(s.shape, dtype=complex)
    for i in range(Nr):
        Sa[:, i] = iprs.fft(Src[:, i])

    # =================RCMC
    # -----------------Step5: RCMC
    Srcmc = Sa

    # =================azimuth compression
    # -----------------Step6: Filter in azimuth
    fetas = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na)
    Ha = np.exp(-1j * (PI * fetas**2) / Ka)
    print("Ha.shape: ", Ha.shape)
    Has = np.reshape(np.repeat(Ha, Nr), (Na, Nr))

    print("Has.shape: ", Has.shape)
    print("--->", Has[0, 10], Has[1, 10], Has[3, 10])
    print("--->", Has[10, 0], Has[10, 1], Has[10, 3])

    Saf = Srcmc * Has
    print("Saf.shape: ", Saf.shape)
    # -----------------Step7: IFFT in azimuth
    SI = np.zeros(s.shape, dtype=complex)
    for i in range(Nr):
        SI[:, i] = iprs.ifft(Saf[:, i])

    return SI


def range_dopp2(s, Fsr, Fsa, Kr, Tp, Ka):

    Na, Nr = s.shape
    # =================range compression
    # -----------------Step1: FFT in range
    Sr = np.fft.fftshift(np.fft.fft(np.fft.fftshift(s)))

    # -----------------Step2: Filter in range

    # htaus = iprs.rect(taus / Tp) * np.exp(-1j * PI * Kr * taus**2)

    # Hr = iprs.fftshift(iprs.fft(htaus))

    ftaus = np.linspace(-Fsr / 2.0, Fsr / 2.0, Nr)

    Hr = iprs.rect(ftaus / (np.abs(Kr) * Tp)) * np.exp(1j * PI * ftaus**2 / Kr)

    print("Hr.shape: ", Hr.shape)

    Hrs = np.reshape(np.repeat(Hr, Na), (Nr, Na)).transpose()

    print("===>", Hrs[0, 500], Hrs[1, 500], Hrs[3, 500])
    print("===>", Hrs[10, 0], Hrs[10, 1], Hrs[10, 3])

    # plt.figure()
    # plt.imshow(np.abs(Hrs))

    print(Hrs.min(), Hrs.max())

    Srf = Sr * Hrs

    print("Srf.shape; ", Srf.shape)

    # -----------------Step3: IFFT in range
    Src = np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(Srf)))

    # =================azimuth FFT
    # -----------------Step4: FFT in azimuth
    Sa = np.zeros(s.shape, dtype=complex)
    for i in range(Nr):
        Sa[:, i] = iprs.fft(Src[:, i])

    # =================RCMC
    # -----------------Step5: RCMC
    Srcmc = Sa

    # =================azimuth compression
    # -----------------Step6: Filter in azimuth
    fetas = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na)
    Ha = np.exp(-1j * (PI * fetas**2) / Ka)
    print("Ha.shape: ", Ha.shape)
    Has = np.reshape(np.repeat(Ha, Nr), (Na, Nr))

    print("Has.shape: ", Has.shape)
    print("--->", Has[0, 10], Has[1, 10], Has[3, 10])
    print("--->", Has[10, 0], Has[10, 1], Has[10, 3])

    Saf = Srcmc * Has
    print("Saf.shape: ", Saf.shape)
    # -----------------Step7: IFFT in azimuth
    SI = np.zeros(s.shape, dtype=complex)
    for i in range(Nr):
        SI[:, i] = iprs.ifft(Saf[:, i])

    return SI


def range_dopp(s, Fsr, Fsa, Kr, Tp, V, F0, R0, fetac):

    Na, Nr = s.shape
    Wl = C / F0

    detaa = 1.0 / Fsa
    etas = np.linspace(-Na / 2.0, Na / 2.0, Na) * detaa
    hh = np.exp(-1j * 2 * np.pi * fetac * etas)
    Has = np.reshape(np.repeat(hh, Nr), (Na, Nr))
    s = s * Has

    Za = int(np.ceil(Tp * Fsa))
    Zr = int(np.ceil(Tp * Fsr))
    print(Za, Zr, "============")

    s = np.concatenate((s, np.zeros((Za, Nr))), axis=0)
    s = np.concatenate((s, np.zeros((Na + Za, Zr))), axis=1)
    print(s.shape)

    Na, Nr = s.shape

    # =================range compression
    # -----------------Step1: FFT in range
    Sr = np.fft.fftshift(np.fft.fft(
        np.fft.fftshift(s, axes=1), axis=1), axes=1)

    # -----------------Step2: Filter in range

    ftaus = np.linspace(-Fsr / 2.0, Fsr / 2.0, Nr)
    fetas = np.linspace(-Fsa / 2.0, Fsa / 2.0, Na) - fetac

    Hr = iprs.rect(ftaus / (np.abs(Kr) * Tp)) * np.exp(1j * PI * ftaus**2 / Kr)

    print("Hr.shape: ", Hr.shape)

    Hrs = np.reshape(np.repeat(Hr, Na), (Nr, Na)).transpose()

    print("===>", Hrs[0, 500], Hrs[1, 500], Hrs[3, 500])
    print("===>", Hrs[10, 0], Hrs[10, 1], Hrs[10, 3])

    # plt.figure()
    # plt.imshow(np.abs(Hrs))

    print(Hrs.min(), Hrs.max())

    Srf = Sr * Hrs

    print("Srf.shape; ", Srf.shape)

    # -----------------Step3: IFFT in range
    Src = np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(Srf)))

    # =================Second range compression
    Ssrc = np.fft.fftshift(np.fft.fft2(np.fft.fftshift(Src)))
    Src = None
    # Window
    # Ssrc = Ssrc*Window

    D = np.sqrt(1.0 - Wl**2 * fetas**2 / (4.0 * V**2))
    fetamat = np.reshape(np.repeat(fetas, Nr), (Na, Nr))
    ftaumat = np.reshape(np.repeat(ftaus, Na), (Nr, Na)).transpose()
    Dmat = np.reshape(np.repeat(D, Nr), (Na, Nr))

    FENMU = (C * R0 * (fetamat**2))
    FENMU = np.where(np.abs(FENMU) < EPS, EPS, FENMU)

    Ksrc = (2.0 * V**2 * F0**3 * (Dmat**3)) / FENMU
    Hsrc = np.exp(-1j * PI * ftaumat**2 / Ksrc)

    Ssrc = Ssrc * Hsrc
    # field of range doppler
    Ssrc = np.fft.ifftshift(np.fft.ifft(
        np.fft.ifftshift(Ssrc, axes=1), axis=1), axes=1)

    # =================RCMC
    # -----------------Step5: RCMC

    t0 = 2.0 * R0 / C
    Ref = (t0 + (Nr / 2.0) * (1.0 / Fsr)) * C / 2.0
    deltaR = (1.0 / Fsr) * C / 2.0
    deltaRCM = Ref * (1.0 / D - 1.0)
    deltaRCM = deltaRCM / deltaR  # Quantification
    print(deltaRCM.shape, "=-===============-----------------")

    integer = np.ceil(deltaRCM)
    fraction = integer - deltaRCM

    Srcmc = np.zeros((Na, Nr), dtype='complex')
    for i in range(Na):
        SincVal = np.sinc(np.arange(fraction[i] - 4, fraction[i] + 3))
        # print(SincVal)
        for j in range(Nr):
            k = j + integer[i]
            if k >= 4 and k <= Nr - 3:
                Srcmc[i, j] = np.matmul(
                    Ssrc[i, int(k - 4):int(k + 3)], SincVal)

    Ssrc = None

    # =================azimuth compression
    # -----------------Step6: Filter in azimuth

    Has = np.exp(1j * 4 * PI * R0 * Dmat * F0 / C)
    # print("Ha.shape: ", Ha.shape)
    # Has = np.reshape(np.repeat(Ha, Nr), (Na, Nr))

    print("Has.shape: ", Has.shape)
    print("--->", Has[0, 10], Has[1, 10], Has[3, 10])
    print("--->", Has[10, 0], Has[10, 1], Has[10, 3])

    Saf = Srcmc * Has
    print("Saf.shape: ", Saf.shape)
    # -----------------Step7: IFFT in azimuth
    SI = np.fft.ifftshift(np.fft.ifft(
        np.fft.ifftshift(Saf, axes=0), axis=0), axes=0)

    SI = SI[0:Na - Za, 0:Nr - Zr]

    return SI
