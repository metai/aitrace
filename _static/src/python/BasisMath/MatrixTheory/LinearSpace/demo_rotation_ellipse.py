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

x = x - np.mean(x)
y = y - np.mean(y)

xy = np.array([x, y])
print(xy.shape)

A = xy

# ========================rotate============================
# ------------rotating matrix(Anti-clockwise)------------
M1 = [[np.cos(theta), -np.sin(theta)],
      [np.sin(theta), np.cos(theta)]]
print("M1", M1)

# -----------------------rotating--------
A1 = np.dot(M1, A)

x1 = A1[0]
y1 = A1[1]

# ------------rotating matrix(clockwise)-----------------
M2 = [[np.cos(theta), np.sin(theta)],
      [-np.sin(theta), np.cos(theta)]]
print("M2", M2)

# -----------------------rotating--------
A2 = np.dot(M2, A)

x2 = A2[0]
y2 = A2[1]

# ========================show data=========================
xmin = np.min([x, x1, x2])
xmax = np.max([x, x1, x2])
ymin = np.min([y, y1, y2])
ymax = np.max([y, y1, y2])
plt.figure()
plt.subplot(131)
plt.scatter(x, y, c='g', marker='o')
plt.grid()
plt.axis([xmin, xmax, ymin, ymax])
# plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('orignal ellipse')
plt.subplot(132)
plt.scatter(x1, y1, c='g', marker='o')
plt.grid()
plt.axis([xmin, xmax, ymin, ymax])
# plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('anti-clockwise rotated ellipse')
plt.subplot(133)
plt.scatter(x2, y2, c='g', marker='o')
plt.grid()
plt.axis([xmin, xmax, ymin, ymax])
# plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('clockwise rotated ellipse')
plt.show()
