import numpy as np
from numpy.fft import fft, fftshift, ifftshift, fft2, ifft, ifft2

import iprs

PI = 3.141592653589793238462643383279502884197169399375105820974944592307
EPS = 1.0e-32
C = 299792458.0
Ge = 398603e9  # the constant of earth gravitation
# Re = 6400.137e3  # the radius of earth
Rea = 6367.856e3  # the avarage radius of earth
Ree = 6378.137e3  # the equatorial radius of earth
Rep = 6356.752e3  # the polar radius of earth


def rect(x):
    r"""
    Rectangle function:
        rect(x) = {1, if |x|<= 0.5; 0, otherwise}
    """
    # return hs(x + 0.5) * ihs(x - 0.5)
    return np.where(np.abs(x) >= 0.5, 0.0, 1.0)


def antenna_pattern_azimuth(Wl, La, A):

    Bwa = 0.886 * Wl / La

    Pa = np.sinc(0.886 * A / Bwa)

    return Pa


def chirp_scaling(Sr, ta, tr, fa, fr, tnear, tfar, Tp, Fc, Kr, V, Vr, fadc, R0, Yc, zpadar=False, usesrc=True, rcmc=None, usedpc=True, verbose=False):

    Na, Nr = Sr.shape

    Wl = C / Fc
    Vs = V

    ta = np.reshape(ta, (Na, 1))

    # ==================Align to Zero Doppler Center in azimuth
    print("---Align to zero Doppler Center(azimuth)...")
    Haz = np.exp(-1j * 2.0 * PI * fadc * np.matmul(ta, np.ones((1, Nr))))

    Sr = Sr * Haz
    # printmmv("Sr", Sr)

    print("---Done!")

    if zpadar is None:
        Za = int(np.ceil(Tp * Fsa * 1e4))
        Zr = int(np.ceil(Tp * Fsr))
        zpadar = (Za, Zr)

    if zpadar:
        Za, Zr = zpadar
        Sr, fa, fr, ta, tr = iprs.zeros_padding(
            Sr, fa, fr, ta, tr, Tp, Za, Zr, verbose=verbose)

    Na, Nr = Sr.shape

    fr = np.reshape(fr, (Nr, 1))
    fa = np.reshape(fa, (Na, 1)) + fadc
    print(fadc)

    # =================Step1: FFT in azimuth (In RD domain)
    print("---Do FFT in azimuth...")

    Sr = fftshift(fft(fftshift(Sr, axes=0), axis=0), axes=0)
    print("---Done!")

    # -----------------Step2: Chirp Scaling
    print("---Do Chirp Scaling...")
    Rref = ((tnear + tfar) / 2.0) * C / 2.0
    Vref = Vr
    faref = fadc

    # print("Rref", Rref)
    # print("Vref", Vref)
    # print("faref", faref)

    print(Sr.min(), Sr.max(), "]]]]]]]]]]]]]")
    print(Wl, Vr, V)
    aaa = ((Wl * fa)**2) / (4.0 * (Vr**2))
    print(aaa.min(), aaa.max())
    DfaV = np.sqrt(1 - ((Wl * fa)**2) / (4.0 * (V**2)))
    DfaVref = np.sqrt(1 - ((Wl * fa)**2) / (4.0 * (Vref**2)))
    DfarefV = np.sqrt(1 - ((Wl * faref)**2) / (4.0 * (V**2)))
    DfarefVref = np.sqrt(1 - ((Wl * faref)**2) / (4.0 * (Vref**2)))
    # printmmv("DfaV", DfaV)
    # printmmv("DfaVref", DfaVref)

    FENMU = (C * R0 * (fa ** 2))
    FENMU = np.where(np.abs(FENMU) < EPS, EPS, FENMU)
    Ksrc = (2.0 * (Vr ** 2) * (Fc ** 3) * (DfaV ** 3)) / FENMU
    Km = Kr / (1.0 - Kr / Ksrc)
    RCMbulk = Rref / DfaVref - Rref / DfarefVref
    # printmmv("Ksrc", Ksrc)
    # printmmv("Km", Km)
    # printmmv("RCMbulk", RCMbulk)

    tau = (2 / C) * (R0 / DfarefV + RCMbulk)
    taudiff = tau - (2 * Rref) / (C * DfaVref)
    alpha = DfarefVref / DfaVref - 1.0

    Hsrc = np.exp(1j * PI * Km * alpha * (taudiff**2))
    # printmmv("tau", tau)
    # printmmv("alpha", alpha)
    # printmmv("Hsrc", Hsrc)

    Sr = Sr * (np.matmul(Hsrc, np.ones((1, Nr))))
    Hsrc = None
    print('---Done!')

    # -----------------Step3: FFT in range
    print("---Do FFT in range...")
    Sr = fftshift(fft(fftshift(Sr, axes=1), axis=1), axes=1)
    print("---Done!")

    # -----------------Step4: RC, SRC, RCMC
    print("---Do RC, SRC...")
    Hm = np.exp(1j * PI * np.matmul(np.ones((Na, 1)), fr.transpose())**2 /
                (np.matmul(Km, np.ones((1, Nr))) *
                    (1 + np.matmul(alpha, np.ones((1, Nr))))))

    Hrcmc = np.exp(1j * 4 * PI * (np.matmul(RCMbulk, np.ones((1, Nr)))) *
                   (np.matmul(np.ones((Na, 1)), fr.transpose())) / C)

    Sr = Sr * Hm
    Hm = None

    print("---Done!")

    Title = 'After RC, SRC'
    if rcmc:
        print("---Do RCMC...")
        Sr = Sr * Hrcmc
        Hrcmc = None
        print("---Done!")
        Title = 'After RC, SRC and RCMC'

    # -----------------Step5: IFFT in range
    print("---Do IFFT in range...")

    Sr = ifftshift(ifft(ifftshift(Sr, axes=1), axis=1), axes=1)

    print("---Done!")
    if verbose:
        iprs.show_amplitude_phase(Sr, Title=Title)

    if usedpc:
        print("---Do dopplor phase compensation (DPC)...")
        Hdp = np.exp(1j * 2 * PI * fa * Yc / Vs)
        Sr = Sr * np.matmul(Hdp, np.ones((1, Nr)))
        print("---Done!")

    if verbose:
        iprs.show_amplitude_phase(Sr, Title='After DPC')

    # -----------------Step6: azimuth compression
    print("---Do azimuth compression...")

    Hac = np.exp(1j * 4 * PI * R0 * Fc * DfaV / C)
    Hpc = np.exp(-1j * 4 * PI * (Km / (C**2)) *
                 (1.0 - DfaVref / DfarefVref) * (R0 / DfaV - Rref / DfaV)**2)

    Sr = Sr * np.matmul(Hac, np.ones((1, Nr)))
    Sr = Sr * np.matmul(Hpc, np.ones((1, Nr)))

    print("---Done!")

    # -----------------Step7: IFFT in azimuth
    print("---Do IFFT in azimuth...")

    SI = ifftshift(ifft(ifftshift(Sr, axes=0), axis=0), axes=0)
    Sr = None

    print("---Done!")

    if verbose:
        iprs.show_amplitude_phase(SI, Title='After azimuth compression')

    if zpadar:
        print("---Abort Invalid Data...")
        SI = SI[Za:Na - Za, Zr:Nr - Zr]
        print("---Done!")

    print("===Out csa_adv!")

    return SI
