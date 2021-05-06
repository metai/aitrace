.. _Chapter-MatrixAnalysisSummary:

总结
=================


概念对比
---------------


- 函数矩阵: 矩阵 :math:`{\bm A}^{(k)}` 的元素是关于变量 :math:`k` 的函数;
- 矩阵函数: 以矩阵 :math:`{\bm A}` 为自变量的函数;
- 矩阵序列: :math:`{{\bm A}^{(k)} = (a_{ij}^{(k)})_{m\times n}\in {\mathbb C}^{m\times n}}` , 其中 :math:`a_{ij}^{(k)}` 为关于 :math:`k` 的函数;
- 矩阵级数: :math:`\sum_{k=0}^{+\infty} {\bm A}^{(k)} = {\bm A}^{(0)} + {\bm A}^{(1)} + \cdots`
- 矩阵序列收敛: :math:`{\bm A}^{(k)} \rightarrow {\bm A} (k\rightarrow +\infty)` , 其中 :math:`{\bm A}^{(k)}` 为关于 :math:`k` 的函数矩阵, :math:`{\bm A} = (a_{ij})_{m\times s}` 为常数矩阵;
- 收敛矩阵: :math:`{\bm A}^k \rightarrow {\bm O} (k\rightarrow +\infty)` , 其中 :math:`{\bm A}^k = {\bm A}{\bm A}\cdots {\bm A}` 表示 :math:`{\bm A}` 的 :math:`k` 次幂, :math:`{\bm O}` 为零矩阵;


收敛定理
----------------

- 矩阵序列收敛: :math:`{\bm A}^{(k)} \rightarrow {\bm O}` 的充要条件是 :math:`\|{\bm A}^{(k)}\| \rightarrow 0` , 其中, :math:`\|\cdot\|` 为 :math:`\mathbb{C}^{m\times n}` 上的任意范数.
- 矩阵序列收敛: :math:`{\bm A}^{(k)} \rightarrow {\bm A}` 的充要条件是 :math:`\|{\bm A}^{(k)} - {\bm A}\| \rightarrow 0` , 其中, :math:`\|\cdot\|` 为 :math:`\mathbb{C}^{m\times n}` 上的任意范数.
- 矩阵收敛: :math:`{\bm A}^k \rightarrow {\bm O}` 的充要条件是 :math:`\rho({\bm A}) < 1` , 其中, :math:`\rho({\bm A})` 为 :math:`{\bm A}` 的谱半径.
- 矩阵级数收敛: :math:`\sum_{k=0}^{+\infty} {\bm A}^{(k)} = {\bm A}^{(0)} + {\bm A}^{(1)} + {\bm A}^{(2)} + \cdots` 绝对收敛的充要条件是正项级数 :math:`\sum_{k=0}^{\infty}\|{\bm A}^{(k)}\|` 收敛.
- 矩阵幂级数收敛: :math:`\sum_{k=0}^{+\infty} {\bm A}^k = {\bm I} + {\bm A}^1 + {\bm A}^2 + \cdots` 收敛的充要条件是 :math:`{\bm A}` 收敛, 且幂级数收敛于 :math:`({\bm I} - {\bm A})^{-1}`   .
