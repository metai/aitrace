.. _Section-ContrastEnhancementDigitalImageSignalProcessing:

对比度增强
=================



.. _SubSection-LogContrastEnhancementDigitalImageSignalProcessing:

对数增强
-----------------


对数增强可以用公式表示为:

.. math::
   {\bm I}_{log} = 20 \times {\rm log}_{10}\left({\bm I} + \epsilon\right),

其中, :math:`\epsilon>0` 为很小的正数, :math:`\bm I` 为图像数据矩阵, :math:`{\bm I}_{log}` 表示对数增强后的图像数据矩阵. 通常还会对 :math:`{\bm I}_{log}` 进行截断处理得到 :math:`{\bm I}_{truncated}`, 即对不在区间 :math:`[a, b]` 内的数值做如下处理:

.. math::
   \left\{ {\begin{array}{ll}
   {i = a,}&{i < a}\\
   {i = b,}&{i > b}
   \end{array}} \right.

其中, :math:`i\in{\bm I}_{truncated}` 为图像的像素. 最后将 :math:`{\bm I}_{truncated}` 中的元素值从区间 :math:`[a, b]` 映射到图像域区间 (如 :math:`[0, 255]`) 即可.





