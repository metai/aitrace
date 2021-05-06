.. _Section-DFTDICTsRepresentationDictionarySparseSignalProcessing:

离散傅里叶变换类字典
=====================

什么是离散傅里叶变换
----------------

**离散傅里叶变换** (:term:`Discrete Cosine Transform`, DCT) 将有限长序列信号表示成不同频率的余弦函数之和, 被广泛用于音频与图像的压缩. 目前共有 DCT-I, DCT-II, DCT-III, DCT-IV, DCT-V-VIII 五种变种 [#DCTs]_. DCT在图像压缩上的应用内容参见 [#DCT_larry]_. 最长见的是 DCT-II 型, 下面进行介绍.


一维离散余弦变换
----------------

`link text <https://blog.csdn.net/wyw921027/article/details/52102264>`_

`link text <http://fourier.eng.hmc.edu/e161/lectures/dct/node1.html>`_

**离散余弦变换** (:term:`Discrete Cosine Transform`, DCT)最早由 Ahmed等人 :cite:`Ahmed.1974` 于1974年提出, 他们发现DCT的基提供了对Toeplitz矩阵特征向量的良好近似. 序列信号 :math:`x[k], k=0,\cdots,N-1` 的 DCT-II 的离散余弦变换定义如下

.. math::
   y[k] = {\sum}_{n=0}^{N-1}x[n]{\rm cos}\frac{(2n+1)k\pi}{2N},
   :label: equ-1DDCTII

其中, :math:`y[k]` 为变换后的系数序列. 对 :eq:`equ-DCTII-1D` 中的结果分别乘以 :math:`1/\sqrt{2}` (:math:`k=0`) 和 :math:`\sqrt{2/N}` (:math:`k=0,1,\cdots,N-1`) 可以得到正交版本的DCT变换.

.. _defDCTII_Orth:

.. proof:definition:: 离散余弦变换 (Discreate Cosine Transformation)

   离散序列 :math:`x[n], n=0, 1,\cdots, N-1` 的DCT变换定义为

   .. math::
      y[k] = {\rm DCT}(x[n]) = \left\{ {\begin{array}{lll}
            {\sqrt{\frac{2}{N}}\sum_{n=0}^{N-1}x[n]\frac{1}{\sqrt 2}, \quad k=0}\\
            {\sqrt{\frac{2}{N}}\sum_{n=0}^{N-1}x[n]{\rm cos}\frac{(2n + 1)k\pi}{2N}, \quad k=1, \cdots, N-1}
            \end{array}} \right.
      :label: equ-DCTII_Orth

   用矩阵表示为

   .. math::
      {\bm y} = {\bm D}{\bm x}
      :label: equ-DCTII_Orth_MatrixRep

   其中, :math:`{\bm x} = (x_n)_{N\times 1}, x_n = x[n]`, :math:`{\bm D} = (d_{ij})_{N\times N}` 表示为

   .. math::
      {\bm D} = \sqrt{\frac{2}{N}}\left[\begin{array}{ccccc}{1/\sqrt{2}} & {1/\sqrt{2}} & {1/\sqrt{2}} & {\cdots} & {1/\sqrt{2}} \\ {\cos \frac{\pi}{2 N}} & {\cos \frac{3 \pi}{2 N}} & {\cos \frac{5 \pi}{2 N}} & {\cdots} & {\cos \frac{(2 N-1) \pi}{2 N}} \\ {\vdots} & {\vdots} & {\vdots} & {\vdots} \\ {\cos \frac{(N-1) \pi}{2 N}} & {\cos \frac{3(N-1) \pi}{2 N}} & {\cos \frac{5(N-1) \pi}{2 N}} & {\cdots} & {\cos \frac{(2 N-1)(N-1) \pi}{2 N}}\end{array}\right]
      :label: equ-DCTII_Orth_Matrix

   向量 :math:`{\bm x}` 为信号 :math:`{\bm y} = (y_k)_{N\times 1}, y_k = y[k]` 在基 :math:`\{1/{\sqrt 2}, {\rm cos}\frac{(2n + 1)k\pi}{2N}\}` 下的坐标, 亦即离散余弦变换系数, 代表频率成分(与傅立叶变换一致). 变换前后的数据维度不变.



易知, 一维离散余弦变换矩阵 :math:`\bm D` 为正交矩阵 (:math:`{\bm D}{\bm D}^T = {\bm D}^T {\bm D} = {\bm I}`), 故逆一维离散余弦变换可以通过下式计算

.. math::
   {\bm x} = {\bm D}^{-1}{\bm y} = {\bm D}^T{\bm y}
   :label: equ-IDCT_MatrixRep



多维离散余弦变换
-----------------

根据一维离散余弦变换的定义, 很容易将其扩展成多维形式, 记一个 :math:`L` 维序列信号为 :math:`x_{k_1,k_2,\cdots,k_L}`, 其中 :math:`k_l = 0,1,\cdots,N_l-1`, :math:`l=1,2,\cdots,L`, :math:`N_l` 为信号在第 :math:`l` 为的样点数. 则扩展后的多维DCT-II变换可表示为

.. math::
   \begin{aligned}
   y_{k_1,k_2,\cdots,k_L} = {\sum}_{n_1=0}^{N_1-1}\cdots \left({\sum}_{n_L=0}^{N_L-1} x_{n_1,\cdots,n_L}{\rm cos}\frac{(2n_L+1)k_L\pi}{2N_L}\right)\cdots{\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}\\
   = {\sum}_{n_1=0}^{N_1-1}\cdots {\sum}_{n_L=0}^{N_L-1} x_{n_1,\cdots,n_L} {\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}\cdots {\rm cos}\frac{(2n_L+1)k_L\pi}{2N_L}.
   \end{aligned}
   :label: equ-MDDCTII

如二维的DCT变换可表示为

.. math::
   \begin{aligned}
   y_{k_1,k_2} &= {\sum}_{n_1=0}^{N_1-1}\left({\sum}_{n_2=0}^{N_2-1}x_{n_1,n_2}{\rm cos}\frac{(2n_2+1)k_2\pi}{2N_2}\right){\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}\\
   &= {\sum}_{n_1=0}^{N_1-1}{\sum}_{n_2=0}^{N_2-1}{\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}{\rm cos}\frac{(2n_2+1)k_2\pi}{2N_2}\\
   &= {\sum}_{n_2=0}^{N_2-1}\left({\sum}_{n_1=0}^{N_1-1}x_{n_1,n_2}{\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}\right){\rm cos}\frac{(2n_2+1)k_2\pi}{2N_2}\\
   &= {\sum}_{n_2=0}^{N_2-1}{\sum}_{n_1=0}^{N_1-1}{\rm cos}\frac{(2n_2+1)k_2\pi}{2N_2}{\rm cos}\frac{(2n_1+1)k_1\pi}{2N_1}\\
   \end{aligned}
   :label: equ-2DDCTII

记 :math:`{\bm X}\in{\mathbb R}^{N_1\times N_2}`, :math:`{\bm D}_1\in{\mathbb R}^{N_1\times N_1}` 为第一维上的DCT变换, :math:`{\bm D}_2\in{\mathbb R}^{N_2\times N_2}` 为第二维上的DCT变换, :math:`{\bm D}_1,{\bm D}_2` 均由 :eq:`equ-DCTII_Orth_Matrix` 生成, :math:`{\bm Y}\in{\mathbb R}^{N_1\times N_2}` 为二维DCT变换后的系数矩阵, 则

.. math::
   {\bm Y} = {\bm D}_1{\bm X}{\bm D}_2^T
   :label: equ-2DDCTII_Matrix

设 :math:`{\bm X}` 为一二维矩阵, 记 :math:`{\rm DCT}({\bm X}, 1)` 表示对 :math:`{\bm X}` 的第一维(列)进行DCT变换, :math:`{\rm DCT}({\bm X}, 2)` 表示对 :math:`{\bm X}` 的第二维(行)进行DCT变换, 则矩阵 :math:`{\bm X}` 的二维DCT变换可以表示为

.. math::
   {\bm Y} = {\rm DCT2}({\bm X}) = {\rm DCT}({\rm DCT}({\bm X}, 1),2)  = {\rm DCT}({\rm DCT}({\bm X}, 2),1)
   :label: equ-DCT2D

逆二维离散余弦变换可以表示为

.. math::
   {\bm X} = {\rm IDCT2}({\bm Y}) = {\rm IDCT}({\rm IDCT}({\bm Y}, 1),2)  = {\rm IDCT}({\rm IDCT}({\bm Y}, 2),1)
   :label: equ-IDCT2D



.. _SubSection_ODFTDICT:

过完备DCT字典
-------------------

在过完备字典(参见 :ref:`Section-DictionaryType`)中, 原子(列)间是线性相关的, 存在冗余原子, 原子的数目 :math:`N` 大于原子的维度 :math:`M`. :eq:`equ-DCTII_Orth_Matrix` 所表示的DCT基矩阵是一个完备字典, 那么如何得到过完备的DCT字典呢? 可以通过对其进行上采样和调制得到.

对于给定的信号 :math:`{\bm y}\in {\mathbb R}^{M\times 1}`, 期望找到一组过完备基 :math:`{\bm D} = [{\bm d}_0, {\bm d}_1,\cdots, {\bm d}_{N-1}]` 和一组系数 :math:`{\bm x} = [x_0, x_1, \cdots, x_{N-1}]`, 满足

.. math::
   {\bm y} = {\bm D}{\bm x} = x_0 {\bm d}_0 + x_1 {\bm d}_1 + \cdots, x_{N-1}{\bm d}_{N-1}

其中, :math:`{\bm d}_i = \{1/{\sqrt 2}, \cdots, {\rm cos}\frac{(2i + 1)k\pi}{2N}, \cdots, {\rm cos}\frac{(2i + 1)(M-1)\pi}{2N}\} \in {\mathbb R}^{M\times 1}` 为DCT基向量, :math:`i=0, 1, \cdots, N-1`, :math:`k=1, \cdots, M-1`, 过完备DCT字典 :math:`{\bm D} \in {\mathbb R}^{M\times N}`, 可表示为

.. math::
   {\bm D} = \sqrt{\frac{2}{N}}\left[\begin{array}{ccccc}{1/\sqrt{2}} & {1/\sqrt{2}} & {1/\sqrt{2}} & {\cdots} & {1/\sqrt{2}} \\ {\cos \frac{\pi}{2 N}} & {\cos \frac{3 \pi}{2 N}} & {\cos \frac{5 \pi}{2 N}} & {\cdots} & {\cos \frac{(2 N-1) \pi}{2 N}} \\ {\vdots} & {\vdots} & {\vdots} & {\vdots} \\ {\cos \frac{(M-1) \pi}{2 N}} & {\cos \frac{3(M-1) \pi}{2 N}} & {\cos \frac{5(M-1) \pi}{2 N}} & {\cdots} & {\cos \frac{(2 N-1)(M-1) \pi}{2 N}}\end{array}\right]
   :label: equ-ODCT_Matrix

通常, 会对字典的列进行归一化, 归一化后的字典可以表示为

.. math::
   {\bm D} = \left[\frac{{\bm d}_0}{\|{\bm d}_0\|_2}, \frac{{\bm d}_1}{\|{\bm d}_1\|_2},\cdots, \frac{{\bm d}_{N-1}}{\|{\bm d}_{N-1}\|_2}\right]
   :label: equ-ODCT_Matrix_normed

一维过完备DCT字典
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

一维过完备DCT字典的构建较为简单, 只需按照 :eq:`equ-ODCT_Matrix` 生成矩阵, 再按照 :eq:`equ-ODCT_Matrix_normed` 对字典的每一列(原子)进行归一化即可.


多维过完备DCT字典
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

多维过完备DCT字典的构建以一维过完备DCT字典为基础, 设矩阵 :math:`{\bm D}_{1d} \in {\mathbb R}^{M\times N}` 为一维归一化过完备DCT字典, 则二维DCT字典 :math:`{\bm D}_{2d}` 可以通过下式计算

.. math::
   {\bm D}_{2d} = {\bm D}_{1d} \times {\bm D}_{1d},
   :label: equ-Create2DDCT_Matrix

其中, :math:`\times` 表示 :ref:`SubSection-KroneckerProduct` (Kronecker Product). 依次类推可以得到多维过完备DCT字典

.. math::
   {\bm D}_{nd} = {\bm D}_{(n-1)d} \times {\bm D}_{(n-1)d}.
   :label: equ-CreatenDDCT_Matrix


.. hint::
   按此规则生成的字典 :math:`{\bm D}_{nd}` 大小为 :math:`M^n \times N^n`, 每一列代表一个原子, 将原子重新排成 :math:`n` 维的矩阵即可.


实验与分析
---------------------

一维离散余弦变换
~~~~~~~~~~~~~~~~~~


原始定义
^^^^^^^^^^^

Python实现

.. code-block:: python
   :emphasize-lines: 10-12
   :linenos:
   :name: bind-id

   def dct1(x):
       x = np.array(x)
       N = np.size(x)

       y = np.zeros(N)

       y[0] = np.sum(x) / np.sqrt(N)

       for k in range(1, N):
           d = np.cos(
               (np.linspace(0, N, N, endpoint=False) * 2 + 1) * k * np.pi / (2.0 * N))
           y[k] = np.sqrt(2.0 / N) * np.sum(x * d)

       return y

设置序列 :math:`x[n] = n, n=0,1,2,\cdots,5`, 调用上述函数以及Matlab中的 ``dct`` 函数, 得实验结果

Matlab结果 ::

   >> x=[0,1,2,3,4,5]

   x =

        0     1     2     3     4     5

   >> dct(x)

   ans =

       6.1237   -4.1626         0   -0.4082         0   -0.0801


Python结果 ::

   x = [0, 1, 2, 3, 4, 5]
   y = dct(x)
   print(y)

   >> [ 6.12372436e+00 -4.16256180e+00 -1.53837015e-15 -4.08248290e-01 -1.53837015e-15 -8.00788912e-02]


矩阵法实现
^^^^^^^^^^^


Matlab实现构造DCT变换矩阵

.. code-block:: matlab
   :emphasize-lines: 7,8,10
   :linenos:
   :name: bind-id

   x = [0, 1, 2, 3, 4, 5]

   n = length(x)

   [cc,rr] = meshgrid(0:n-1);

   T = sqrt(2 / n) * cos(pi * (2*cc + 1) .* rr / (2 * n));
   T(1,:) = T(1,:) / sqrt(2);

   y = T * x;
   disp(y)


Python实现构造DCT变换矩阵

.. code-block:: python
   :emphasize-lines: 7,8,10
   :linenos:
   :name: bind-id

   x = [0, 1, 2, 3, 4, 5]

   N = np.size(x)

   r, c = np.mgrid[0: N, 0: N]

   T = np.sqrt(2 / N) * np.cos(np.pi * (2 * c + 1) * r / (2 * N))
   T[0, :] = T[0, :] / np.sqrt(2)

   y = np.matmul(T, x)
   print(y)


图像的1维DCT变换
^^^^^^^^^^^^^^^^

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/RepresentationDictionary/lenaDCT1.*
   :scale: 80 %
   :alt: lena 图像的1维DCT变换
   :align: center

   lena 图像的1维DCT变换


二维离散余弦变换
~~~~~~~~~~~~~~~~~~~~

仿真数据
^^^^^^^^^^^^^^^^

Matlab结果

.. code-block:: matlab
   :emphasize-lines: 6
   :linenos:
   :name: bind-id

   a =

        0     1     2
        3     4     5

   >> dct2(a)

   ans =

       6.1237   -2.0000   -0.0000
      -3.6742         0         0

.. code-block:: python
   :emphasize-lines: 5,7,9,13,19
   :linenos:
   :name: bind-id

   def dct1(x, axis=0):
       x = np.array(x)
       if np.ndim(x) > 1:
           N = np.size(x, axis=axis)
           T = dctmat(N)
           if axis is 0:
               return np.matmul(T, x)
           if axis is 1:
               return np.matmul(T, x.transpose()).transpose()
       if np.ndim(x) is 1:
           N = np.size(x)
           T = dctmat(N)
           return np.matmul(T, x)

   def dct2(X):
      return dct1(dct1(x, axis=0), axis=1)

   x = [[0, 1, 2], [3, 4, 5]]
   y = dct2(x)
   print(y)

   >> [[ 6.12372436e+00 -2.00000000e+00  5.32490308e-16]
       [-3.67423461e+00 -3.44458101e-16 -2.51493529e-16]]



真实图像数据
^^^^^^^^^^^^^^^^

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/RepresentationDictionary/lenaDCT2.*
   :scale: 80 %
   :alt: lena 图像的二维DCT变换及IDCT变换
   :align: center

   lena 图像二维DCT变换及IDCT变换



DCT过完备字典
~~~~~~~~~~~~~~~~~~

Python 实现参见文件 `demo_odctdict.py <https://github.com/antsfamily/pysparse/tree/master/examples/representation/dct/demo_odctdict.py>`_

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/representation/dct/demo_odctdict.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 22,27,32,37
   :linenos:
   :caption: demo_odctdict.py
   :name: bind-id

生成大小分别为 :math:`16\times 8, 16\times 16, 16\times 32, 16\times 64` 的一维过完备DCT字典, 基于这些字典, 根据 :eq:`equ-Create2DDCT_Matrix` 生成的二维过完备字典.

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/RepresentationDictionary/1D-ODCTs.*
   :scale: 80 %
   :alt: 1-dimension overcomplete DCT dictionary
   :align: center

   1-dimension overcomplete DCT dictionary. These four dictionary are generated from 1-dimension DCT dictionary with size of :math:`16\times 8, 16\times 16, 16\times 32, 16\times 64`.

依次将由 :eq:`equ-Create2DDCT_Matrix` 生成的二维过完备字典的每一列(原子) :math:`{\bm d}_i\in {\mathbb R}^{256\times 1}` reshape 成 :math:`16\times 16` 大小的矩阵, 并按顺序从左至右从上至下排列成方阵

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/RepresentationDictionary/2D-ODCTs.*
   :scale: 80 %
   :alt: 2-dimension overcomplete DCT dictionary
   :align: center

   2-dimension overcomplete DCT dictionary. These four dictionary are generated from 1-dimension DCT dictionary with size of :math:`16\times 8, 16\times 16, 16\times 32, 16\times 64` using formular :eq:`equ-Create2DDCT_Matrix` respectively.


.. rubric:: Footnotes

.. [#DCT_larry] http://c.csie.org/~itct/slide/DCT_larry.pdf
.. [#DCTs] http://en.volupedia.org/wiki/Discrete_cosine_transform




