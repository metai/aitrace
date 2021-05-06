.. _SubSection-MultipleSignalClassificationNoiseSubspaceBasedModernSpectralEstimationDigitalSignalProcessing:


多重信号分类
===========

在许多实际信号处理问题中, 目标是从测量中估计接收信号所依赖的一组常量参数. 对于这类问题, 有几种方法可以解决, 如Capon 1969年提出的最大似然法和Burg提出的最大熵法. 虽然这些方法已经被广泛使用, 但它们有一定的局限性(尤其是参数估计中的偏差和敏感性), 这主要是因为它们使用了不正确的测量模型(例如, 使用自回归AR模型而不是特殊的ARMA模型). Pisarenko 于1973年首次利用数据模型结构来估计信号参数, 如使用协方差方法估计带有加性噪声的复杂正弦信号的参数. Schmidt于1977年, 通过研究干净无噪声信号, 推导出一个完整的几何解, 然后巧妙地扩展几何概念, 在有噪声的情况下获得一个合理的近似解. 该算法被称为多信号分类(MUSIC), 并得到了广泛的研究. MUSIC是目前公认的最有效的高分辨率算法之一, 尽管音乐的性能优势是实质性的, 但其计算与存储资源消耗大.




多信号分类用于频率估计
---------------------

多重信号分类 ( :term:`MUltiple SIgnal Classiﬁcation` , MUSIC)





实例分析
-----------

仿真信号
~~~~~~~~~~


实验内容
^^^^^^^^^^^^^


实验代码
^^^^^^^^^^^^^

实验结果
^^^^^^^^^^^^^



.. figure:: ../../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Modern/NoiseSubspaceBased/MUSIC/demo_matlab_fft_music1.png
   :scale: 80 %
   :alt: demo matlab fft music
   :align: center

   Synthetic signal

   合成的信号, 包含四种频率成分.


.. figure:: ../../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Modern/NoiseSubspaceBased/MUSIC/demo_matlab_fft_music2.png
   :scale: 80 %
   :alt: demo matlab fft music
   :align: center

   Synthetic signal

   合成的信号, 包含四种频率成分.
