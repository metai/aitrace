import pytool
import numpy as np
import matplotlib.pyplot as plt

# gen points
startx = 0
endx = 10
N = 32
x = np.linspace(startx, endx, N)

# y1 = a1*x + b1
a1 = 6.0
b1 = 2.0
x1 = x + np.random.randn(N)
y1 = a1 * x1 + b1 + np.random.randn(N)


# y2 = a2*x + b2
a2 = -6.0
b2 = -2.0
x2 = x + np.random.randn(N)
y2 = a2 * x2 + b2 + np.random.randn(N)

# y3 = a3*x + b3
a3 = 0.0
b3 = 1.0
x3 = x + np.random.randn(N)
y3 = a3 * x3 + b3 + np.random.randn(N)

# show data
plt.figure()
plt.scatter(x1, y1, c='r', marker='+')
plt.scatter(x2, y2, c='b', marker='*')
plt.scatter(x3, y3, c='g', marker='o')


# Eigenvalue decomposition
# x1y1 = np.concatenate((x1, y1), axis=1)
x1y1 = np.array([x1, y1])
x2y2 = np.array([x2, y2])
x3y3 = np.array([x3, y3])
print(x1y1.shape)
A = np.concatenate((x1y1, x2y2, x3y3), axis=1)

AAT = np.dot(A, A.transpose())
ATA = np.dot(A.transpose(), A)

evalues, evectors = np.linalg.eig(AAT)
# evalues, evectors = np.linalg.eig(ATA)
print(A.shape, ATA.shape, evalues.shape, evectors.shape)

print(evalues, evectors)

colorlines = ['-r', '-b']
pytool.plot_vectors(evectors, startx=startx, endx=endx,
                    nPoints=N, title='eigen vectors', colorlines=colorlines)

plt.show()
