import pytool
import numpy as np
import matplotlib.pyplot as plt

# =====================generate Ellipse=====================

# angle for rotating
theta = np.pi * 30 / 180

# ========================rotate============================
# ------------rotating matrix(Anti-clockwise)---------------
M = [[np.cos(theta), -np.sin(theta)],
     [np.cos(theta), np.cos(theta)]]
# -----------------------rotating---------------------------

# A = np.array(M)
A = [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
# A = [[1, 0], [0, 1]]
# A = [[1, 1], [0, 1]]
# A = [[2, 0], [0, 1]]
print(A)
# ==================Eigenvalue decomposition================

evalues, evectors = np.linalg.eig(A)

print("A: ", A)
print("evalues: ", evalues)
print("evectors: ", evectors)


# =====================plot eigen vector=====================


colorlines = ['-r', '-b']
pytool.plot_vectors2d(evalues*evectors, title='eigen vectors', colorlines=colorlines)
# pytool.plot_vectors2d(evectors, title='eigen vectors', colorlines=colorlines)
plt.legend(['eigen vector1', 'eigen vector2'])
plt.show()
