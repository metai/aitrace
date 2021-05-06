.. _Section-LinearCSLinearCompressiveSensingSparseSignalProcessing:

线性压缩感知
=====================

压缩感知 (:term:`Compressive Sensing`, CS) 由 :cite:`Donoho` 等人于2004年提出, 压缩感知线性模型, 即线性压缩感知 (:term:`Linear Compressive Sensing`, LCS)


`压缩感知笔记 <https://www.cnblogs.com/AndyJee/category/579870.html>`_


线性压缩感知概述
----------------------

为便于描述, 将一个压缩感知系统记为 :math:`{\rm CS}({\mathfrak G}; {\mathfrak F})`, 其中, :math:`{\mathfrak G}` 为观测系统, :math:`{\mathfrak F}` 为重构系统. 例如, 观测系统为 :math:`{\bm \Phi},\cdot`, 重构系统为 :math:`{\bm A}, {\rm omp}`.

压缩感知旨在设计一个观测系统 :math:`{\mathfrak G}` 和一个恢复系统 :math:`{\mathfrak F}`, 使得信号 :math:`{\bm x}` 可以以欠奈奎斯特采样频率采样并得到较好的恢复.

其观测过程可以表示为

.. math::
   {\bm y} = {\mathfrak G}({\bm x})
   :label: equ-CS_Mesurement

恢复过程可以表示为

.. math::
   {\bm x} = {\mathfrak F}({\bm y}).
   :label: equ-CS_Reconstruction


对于线性压缩感知, 有 :math:`{\mathfrak G}({\bm x}) = {\bm \Phi}{\bm x}`.

- :math:`{\bm \Phi}`: 测量矩阵/观测矩阵
- :math:`{\bm \Psi}`: 稀疏基矩阵/稀疏表示字典矩阵
- :math:`{\bm A} = {\bm \Phi}{\bm \Psi}`: 传感矩阵/感知矩阵

压缩感知理论指出, 当测量矩阵 :math:`{\bm \Phi}` 满足 :ref:`Subsection-RestrictedIsometryProperty` 性质时, 信号能够以较大概率被恢复.


一维线性压缩感知
------------------

稀疏信号的压缩采样与恢复
~~~~~~~~~~~~~~~~~~~~~~~

设有原始稀疏信号 :math:`{\bm x}\in {\mathbb R}^{N \times 1}`, 测量矩阵 :math:`{\bm \Phi} \in {\mathbb R}^{M \times N}`, 则测量过程可以表示为

.. math::
   {\bm y} = {\bm \Phi}{\bm x} + {\bm n}
   :label: equ-CS1d_Mesurement

其中, :math:`{\bm y}\in {\mathbb R}^{M\times 1}` 为测量向量, :math:`{\bm n}\in {\mathbb R}^{M \times 1}` , :math:`M<N` 为观测系统噪声. 在已知 :math:`{\bm y}` 和 :math:`\bm \Phi` 时, 原始信号 :math:`\bm x` 的恢复可以通过优化

 .. math::
   \mathop {\rm min}\limits_{\bm x}\|{\bm x}\|_p, \ \  s.t. \  {\bm y} = {\bm \Phi}{\bm x} + {\bm n},
   :label: equ-CS1d_Optimizationst

其中, :math:`|\cdot|_p, (0\le p \le 1)` 表示 :math:`\ell_p` 范数. :eq:`equ-CS1d_Optimizationst` 可以通过 :ref:`Section-OrthogonalMatchingPursuitSignalSparseDecompositionSparseSignalProcessing` 的方法求解. 与 :eq:`equ-CS1d_Optimizationst` 等效的优化问题为

.. math::
   \mathop {\rm min}\limits_{\bm{x}} = \|{\bm x}\|_p + \lambda\|{\bm y} - {\bm \Phi}{\bm x}\|_2,
   :label: equ-CS1d_Optimizationnost


其中, :math:`\lambda` 是平衡因子, :math:`|\cdot|_p, (0\le p \le 1)` 表示 :math:`\ell_p` 范数.


非稀疏信号的压缩采样与恢复
~~~~~~~~~~~~~~~~~~~~~~~

设有原始非稀疏信号 :math:`\bm x`, 设其可通过可逆线性变换 :math:`{\bm \Psi}^{-1}` 变换到稀疏信号 :math:`\bm z` (:math:`{\bm z} = {\bm \Psi}^{-1}{\bm x}`), 即可在字典 :math:`{\bm \Psi}` 下进行稀疏表示 (:math:`{\bm x} = {\bm \Psi}{\bm z}`), 则对于非稀疏信号的压缩采样与恢复有两种方式, 下面进行介绍.


第一种方式
^^^^^^^^^^^^

1. 变换: :math:`{\bm z} = {\bm \Psi}^{-1}{\bm x}`
2. 观测: :math:`{\bm y} = {\bm \Phi}{\bm z}`,
3. 求解: :math:`{\rm min}_{\bm z} \|{\bm z}\|_p  \ \  s.t. \  {\bm y} = {\bm \Phi}{\bm z}`
4. 重构: :math:`{\bm x} = {\bm \Psi}{\bm z}`


第二种方式
^^^^^^^^^^^^

1. 观测: :math:`{\bm y} = {\bm \Phi}{\bm x}`
2. 求解: :math:`{\rm min}_{\bm z} \|{\bm z}\|_p \ \  s.t. \  {\bm y} = {\bm \Phi}{\bm \Psi}{\bm z}`
3. 重构: :math:`{\bm x} = {\bm \Psi}{\bm z}`




二维压缩感知
~~~~~~~~~~~~~~



复压缩感知
----------------------

对于复数域压缩感知问题可以转换成实数域压缩感知处理. 若 :math:`{\bm y}\in{\mathbb C}^{M\times 1}, {\bm \Phi}\in {\mathbb C}^{M\times N}, {\bm x} \in {\mathbb C}^{N\times 1}`, 问题可以转化为

.. math::
   {\mathop{\rm Re}\nolimits} ({\bm{y}}) + j{\rm Im}({\bm{y}}) = {\rm Re}({\bm \Phi}{\bm x}) + j{\mathop{\rm Im}\nolimits} ({\bm \Phi}{\bm x})
   :label: equ-CCS_equation

写成矩阵形式为

.. math::
   \left[ {\begin{array}{c}
   {{\mathop{\rm Re}\nolimits} ({\bm{y}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{y}})}
   \end{array}} \right] = \left[ {\begin{array}{cr}
   {{\mathop{\rm Re}\nolimits} ({\bm{\Phi }})}&{ - {\mathop{\rm Im}\nolimits} ({\bm{\Phi }})}\\
   {{\rm Im}({\bm{\Phi }})}&{{\mathop{\rm Re}\nolimits} ({\bm{\Phi }})}
   \end{array}} \right]\left[ {\begin{array}{c}
   {{\mathop{\rm Re}\nolimits} ({\bm{x}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{x}})}
   \end{array}} \right]




压缩感知与流形
-----------------------------

流形与压缩感知中的一些重要结果有着密切的关系, 如一组满足 :math:`\|{\bm x}\|_0 = k` 的信号构成了一个 :math:`k` 维黎曼流形. 又如压缩感知中的许多随机感知矩阵可看作是低维流形中的保留结构 :cite:`Baraniuk.2009,Duarte.Jan.2007` .



参见 :cite:`Eldar.2012` Chapter 1




压缩感知分析实验
--------------------

设计Gaussian观测矩阵 :math:`\bm \Phi`, DCT稀疏表示字典 :math:`\bm \Psi`, 记感知矩阵 :math:`{\bm A} = {\bm \Phi}{\bm \Psi}`. 为便于描述, 记一个压缩感知系统为 :math:`{\rm CS}({\mathfrak G}; {\mathfrak F})`, 其中, :math:`{\mathfrak G}` 为观测系统, :math:`{\mathfrak F}` 为重构系统. 以完成对二维图像的高度维压缩采样与恢复为例, 实验中分析: a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})` 四种压缩感知系统的性能.

Python 实现参见文件 `demo_csAnalysis.py <https://github.com/antsfamily/pysparse/tree/master/examples/cs/demo_csAnalysis.py>`_

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/cs/demo_csAnalysis.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 22,27,32,37
   :linenos:
   :caption: demo_csAnalysis.py
   :name: bind-id


以cameraman图像为例, 可视化该图像, 观测矩阵, DCT字典和稀疏表示系数

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/cameramanCSanalysisData.*
   :scale: 100 %
   :alt: Orignal image signal, dictionary matrix, observation matrix, sparse coefficient matrix.
   :align: center

   Orignal image signal, dictionary matrix, observation matrix, sparse coefficient matrix.

压缩比设置为4, 采用OMP算法重构图像信号, 稀疏度设置为 :math:`k=32` 时的结果为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/cameramanCSanalysisResultsk32.*
   :scale: 100 %
   :alt: a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`
   :align: center

   a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`

压缩比设置为4, 采用OMP算法重构图像信号, 稀疏度设置为 :math:`k=64` 时的结果为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/cameramanCSanalysisResultsk64.*
   :scale: 100 %
   :alt: a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`
   :align: center

   a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`


压缩比设置为4, 采用OMP算法重构图像信号, 稀疏度设置为 :math:`k=128` 时的结果为


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/cameramanCSanalysisResultsk128.*
   :scale: 100 %
   :alt: a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`
   :align: center

   a) :math:`{\rm CS}({\bm \Phi}; {\bm \Phi})`, b) :math:`{\rm CS}({\bm \Phi}; {\bm A})`, c) :math:`{\rm CS}({\bm A}; {\bm \Phi})`, d) :math:`{\rm CS}({\bm A}; {\bm A})`

.. note::
   可见, 针对非稀疏信号, 正确的感知系统有两种

   1. 在观测时先将信号变换成稀疏信号, 再对稀疏信号进行压缩观测, 通过测量矩阵和观测值求解稀疏信号, 再进行逆变换重构原始信号.

   2. 采用测量矩阵直接测量非稀疏信号, 在求解时, 假设信号在某一字典下可以进行稀疏表示, 通过字典和测量矩阵以及观测值求解稀疏信号, 再进行逆变换重构原始信号
