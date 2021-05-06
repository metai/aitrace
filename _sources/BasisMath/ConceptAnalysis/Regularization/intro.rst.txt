.. _Section-RegularizationIntro:

正则化简介
=====================


在数学, 统计学和计算机科学中, 特别是在机器学习和逆问题的求解中, 正则化通常通过增加额外的信息解决不适定问题或防止过度拟合. 在不同领域有着不同的正则化技术, 大多是基于范数的正则, 主要有如下几类:

- 基于范数的正则: :math:`\ell_{1/2}, \ell_0, \ell_1, \ell_2` , 核范数(Nuclear Norm), 拉普拉斯范数 (Laplacian Norm), 谱范数(Spectral Norm)正则, 以及Tikhonov 正则 (:term:`Tikhonov Regularization` , 在统计学中称为岭回归) 等等.
- 基于噪声的正则: 如在神经网络中的加噪声, dropout等技术. 
- 稀疏正则 (:term:`Sparse Regularization`): :math:`\ell_{1/2}, \ell_0, \ell_1` , 列稀疏正则等等
- 流形正则 (:term:`Manifold Regularization`): 通常为拉普拉斯范数正则.
- 其它正则: 及早停止 (Early stopping) 也是一种正则化技术.
