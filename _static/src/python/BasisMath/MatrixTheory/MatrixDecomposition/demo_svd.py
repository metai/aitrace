import numpy as np

A = [[1, 0, 1], [0, 1, 1], [0, 0, 0]]
A = [[0, 2, 2], [2, 1, 2], [0, 2, 1]]
u, s, vh = np.linalg.svd(A)
print('s', s)
print('u', u)
print('vh', vh)
print(s.shape, u.shape, vh.shape)
