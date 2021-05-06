.. _Section-MatrixOperation:

矩阵运算
==========================


乘法
-------------

逐元素积
~~~~~~~~~~~

对于维度相同的任意两个矩阵 :math:`{\bm A} = (a_{ij})_{M\times N}`, :math:`{\bm B} = (b_{ij})_{M\times N}`, 其逐元素积为

.. math::
   {\bm A}\odot{\bm B} = {\bm C} = (c_{ij})_{M\times N} = (a_{ij}b_{ij})_{M\times N}
   :label: equ-ElementWiseProduct

点积/内积
~~~~~~~~~~~

定义矩阵 :math:`{\bm A} = (a_{ij})_{M\times N}` 与矩阵 :math:`{\bm B} = (b_{ij})_{N\times P}` 的点积为

.. math::
   {\bm A}{\bm B} = {\bm C} = (c_{ij})_{M\times P} = \left(\sum_{n=1}^N a_{in}b_{nj}\right)_{M\times P}
   :label: equ-DotProduct2Matrix

设有矩阵 :math:`{\bm A} = (a_{ij})_{M\times N}`, :math:`{\bm B} = (b_{ij})_{N\times P}`, :math:`{\bm C} = (b_{ij})_{P\times Q}`, 则他们的点积为

.. math::
   {\bm A}{\bm B}{\bm C}= {\bm D} = (d_{ij})_{M\times Q} = \left(\sum_{p=1}^P\left(\sum_{n=1}^N a_{in} b_{np}\right)c_{pj}\right)_{M\times Q}
   :label: equ-DotProduct2Matrix

.. _SubSection-KroneckerProduct:

Kronecker积
~~~~~~~~~~~

对于任意维度的两个矩阵 :math:`{\bm A} = (a_{ij})_{M\times N}`, :math:`{\bm B} = (b_{ij})_{P\times Q}`, 其Kronecker积为用右矩阵乘以左矩阵的结果.

.. math::
   {\bm A}\times{\bm B} = {\bm C} = (c_{ij})_{MP\times NQ} = (a_{ij}{\bm B})_{MP\times NQ}
   :label: equ-ElementWiseProduct


卷积
~~~~~~~~~~~~


`卷积与转置卷积 <https://blog.csdn.net/LoseInVain/article/details/81098502>`_


`Deconvolution and Checkerboard Artifacts <https://distill.pub/2016/deconv-checkerboard/>`_



示例
~~~~~~~~~~~


.. code-block:: python
   :emphasize-lines: 7,11,14,19
   :linenos:
   :caption: demo_MatrixOperation.py
   :name: bind-id

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


结果如下: ::

   ---element-wise:
   [[ 10  40  90]
    [160 250 360]]
   ---matmul:
   [[140 320]
    [320 770]]
   ---dot:
   [[140 320]
    [320 770]]
   ---kron:
   [[ 10  20  30  20  40  60  30  60  90]
    [ 40  50  60  80 100 120 120 150 180]
    [ 40  80 120  50 100 150  60 120 180]
    [160 200 240 200 250 300 240 300 360]]


