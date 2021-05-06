import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10, 20, 30], [40, 50, 60]])

print("---element-wise: ")
c = a * b
print(c)

print("---matmul: ")
c = np.matmul(a, b.transpose())
print(c)

c = np.dot(a, b.transpose())

print("---dot: ")
print(c)

c = np.kron(a, b)

print("---kron: ")
print(c)
