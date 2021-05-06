import numpy as np

H = 3
W = 4

X = np.random.randn(H, W)

print(X)
print(np.conj(X).transpose())

L2Norm = np.sqrt(np.sum(X ** 2))

S, U, V = np.linalg.svd(np.conjugate(X).transpose())

print(S)

maxSigma = S.max()

SpectralNorm = np.sqrt(maxSigma)

print(np.sqrt(np.sum(np.abs(S))))

print("L2Norm, SpectralNorm: ", L2Norm, SpectralNorm)
