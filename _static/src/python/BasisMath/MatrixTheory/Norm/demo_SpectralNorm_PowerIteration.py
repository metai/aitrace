import numpy as np

EPS = 2.2e-32

H = 3
W = 5

X = np.random.randn(H, W)

S, U, V = np.linalg.svd(np.matmul(np.conjugate(X).transpose(), X))

maxSigma = S.max()

SpectralNorm_SVD = np.sqrt(maxSigma)


def power_iteration_spectral_norm(X, nIters):
    Sigma = 0.0
    M, N = X.shape
    XH = np.conj(X).transpose()
    v = np.random.rand(N, 1)
    print(v)
    # v = np.ones((N, 1))
    for i in range(nIters):
        u = np.matmul(X, v)
        u = u / (np.linalg.norm(u, ord=1) + EPS)
        v = np.matmul(XH, u)
        v = v / (np.linalg.norm(v, ord=1) + EPS)
        Sigma = np.matmul(np.transpose(u), X)
        Sigma = np.matmul(Sigma, v)
        print(Sigma)
    return Sigma


nIters = 1000
SpectralNorm_PowerIteration = power_iteration_spectral_norm(X=X, nIters=nIters)

print(SpectralNorm_PowerIteration)
print("SpectralNorm_SVD:", SpectralNorm_SVD)
print("SpectralNorm_PowerIteration: ", SpectralNorm_PowerIteration)
