import numpy as np
import pytool

A = [[20, 3, 1], [2, 10, 2], [8, 1, 0]]

A = np.array(A)
D = np.diag((1, 1, 1 / 2))
B = np.dot(D, A)
B = np.dot(B, np.linalg.inv(D))

Cis = []
Ris = []
Cis1, Ris1 = pytool.gerschgorin(A)
Cis2, Ris2 = pytool.gerschgorin(A.transpose())
Cis3, Ris3 = pytool.gerschgorin(B.transpose())

Cis = Cis + Cis1
Ris = Ris + Ris1

Cis = Cis + Cis2
Ris = Ris + Ris2

Cis = Cis + Cis3
Ris = Ris + Ris3

colorlines = ['-r', '-g', '-b', '.r', '.g', '.b', '-.r', '-.g', '-.b']

evalues, evectors = np.linalg.eig(A)

Title = "gerschgorin of A with eigens: " + str(evalues)
Legend = ['A: G1', 'A: G2', 'A: G3', 'A^T: G1',
          'A^T: G2', 'A^T: G3', 'B^T: G1', 'B^T: G2', 'B^T: G3']

pytool.plot_circles(
    Cis=Cis, Ris=Ris, colorlines=colorlines, dTheta=0.01, title=Title, legend=Legend)
