import pytool
import numpy as np
import matplotlib.pyplot as plt

# =====================generate Ellipse=====================
a = 6  # major axis
b = 2  # minor axis
x0 = 10  # center x0
y0 = 10  # center y0
N = 1000  # number of points

# angle for rotating ellipse data
theta = np.pi * 30 / 180

x, y = pytool.ellipse_surface(a, b, x0, y0, N, 'rand')
# x, y = pytool.ellipse_surface(a, b, x0, y0, N, 'order')


x = x - np.mean(x)
y = y - np.mean(y)

xse = [min(x), max(x)]
yse = [min(y), max(y)]


xy = np.array([x, y])
print(xy.shape)

A = xy

# ========================rotate============================
# ------------rotating matrix(Anti-clockwise)---------------
M = [[np.cos(theta), np.sin(theta)],
     [-np.sin(theta), np.cos(theta)]]
M = [[np.cos(theta), -np.sin(theta)],
     [np.sin(theta), np.cos(theta)]]
print("rotating matrix M: ", M)

# -----------------------rotating---------------------------
A = np.dot(M, A)

x = A[0]
y = A[1]

# ========================show data=========================
plt.figure()
plt.scatter(x, y, c='g', marker='o')
plt.grid()

# ==================Eigenvalue decomposition================

AAT = np.dot(A, A.transpose())
ATA = np.dot(A.transpose(), A)

evalues, evectors = np.linalg.eig(AAT)
# evalues, evectors = np.linalg.eig(ATA)
print(A.shape, AAT.shape, evalues.shape, evectors.shape)
print(AAT)
print("evalues: ", evalues, "evectors: ", evectors)
angle1 = np.arctan(evectors[1, 0] / evectors[0, 0]) * 180 / np.pi
angle2 = np.arctan(evectors[1, 1] / evectors[0, 1]) * 180 / np.pi
print(angle1, angle2)


# =====================plot eigen vector=====================
colorlines = ['-r', '-b']
pytool.plot_vectors2d(evectors.transpose(), xse=xse, yse=yse,
                      nPoints=N, title='eigen vectors', colorlines=colorlines)
plt.legend(['eigen vector1', 'eigen vector2'])
plt.show()


plt.figure()
plt.imshow(AAT)
plt.show()
