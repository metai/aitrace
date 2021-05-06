import numpy as np


A = [[1, 0, 0], [0, 1, 0], [0, 2, 1]]
A = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
A = [[1, 0, 0], [0, 1, 0], [0, -1, 1]]

A = np.array(A)
print(A)

detA = np.linalg.det(A)

invA = np.linalg.inv(A)

print(detA)
print(invA)
print(np.dot(A, invA))


A = [[1, 2, 2], [2, 1, 2], [2, 0, 1]]

A = np.array(A)
print(A)

detA = np.linalg.det(A)

invA = np.linalg.inv(A)

print(detA)
print(invA)
print(np.dot(A, invA))
