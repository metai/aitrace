import pytool
import numpy as np
import matplotlib.pyplot as plt

# gen Ellipse
a = 4
b = 2
x0 = 10
y0 = 10
N = 100
x, y = pytool.ellipse_surface(a, b, x0, y0, N, 'order')
# x, y = pytool.ellipse_surface(a, b, x0, y0, N, 'rand')
print(len(x), len(y), x[0], y[0])

xse = [min(x), max(x)]
yse = [min(y), max(y)]

# show data
plt.figure()
plt.scatter(x, y, c='g', marker='o')


# SVD decomposition
x = np.array(x)
y = np.array(y)
xy = np.array([x, y])

print(xy.shape)

A = xy

AAT = np.dot(A, A.transpose())
ATA = np.dot(A.transpose(), A)


u, s, vh = np.linalg.svd(AAT)
print(A.shape, ATA.shape, u.shape, s.shape, vh.shape)
print(u, s, vh)

colorlines = ['-r', '-b']
pytool.plot_vectors2d(u, xse=xse, yse=yse,
                    nPoints=N, title='u vectors', colorlines=colorlines)

plt.show()
