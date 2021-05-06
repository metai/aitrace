.. _Section-IntroductionLinearCompressiveSensingSparseSignalProcessing:

简介
=====================


- 线性压缩感知 ( :term:`Linear Compressive Sensing`, LCS)
- 非线性压缩感知 ( :term:`Nonlinear Compressive Sensing`, NCS)
- 可学习压缩感知 ( :term:`Learned Compressive Sensing`, LCS)

.. caution::
   需要注意的是, 在压缩感知中, 当信号不稀疏时, 假设信号在某一字典基 :math:`D` 下可被稀疏表示, 组成新的观测矩阵 :math:`{\bm \Phi} = {\bf A}{\bf D}` , 通过恢复稀疏系数进而恢复非稀疏信号. 这里并不要求在压缩观测时需要先进行稀疏表示(假设某种硬件可以完成稀疏表示), 再进行压缩观测, 而是仍然以 :math:`\bf A` 为观测矩阵, 只是在稀疏求解时引入稀疏表示矩阵. 如果在观测时, 先对稀疏表示, 再进行观测, 并且在恢复时使用 :math:`{\bm \Phi}` 作为观测矩阵, 效果并不如前者好. 这些可以通过实验验证.


- `Compressive Sensing Resources <https://arquivo.pt/wayback/20160516193220/http://dsp.rice.edu/cs>`_ : resources and softwares



