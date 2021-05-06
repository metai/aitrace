.. _Section-EvaluationMethodClassicalSimilarity:

相似性度量指标
===========================


集合方法
-----------------

Jaccard
~~~~~~~~~~~~~~

Jaccard 指数与距离
^^^^^^^^^^^^^^^^^^^

Jaccard 指数 (index), 也称为并上交 (Intersection over Union, IoU) 或 Jaccard 相似性系数 (:term:`Jaccard Similarity Coefficient`), 用于测量样本集的相似性与多样性. Jaccard系数用于衡量有限样本集间的相似性, 被定义为集合交的势除并的势.

.. math::
   J({\mathbb A}, {\mathbb B})=\frac{|{\mathbb A} \cap {\mathbb B}|}{|{\mathbb A} \cup {\mathbb B}|}=\frac{|{\mathbb A} \cap {\mathbb B}|}{|{\mathbb A}|+|{\mathbb B}|-|{\mathbb A} \cap {\mathbb B}|}
   :label: equ-JaccardSimilarityCoefficient

其中, :math:`|\mathbb A|` 表示集合 :math:`\mathbb A` 的势 [#SetCard]_, :math:`0 < J({\mathbb A}, {\mathbb B}) < 1`, 若 :math:`{\mathbb A}, {\mathbb B}` 为空集, 定义 :math:`J({\mathbb A}, {\mathbb B}) = 1`.


.. figure:: ../../../_static/figs/Application/EvaluationMethod/Classical/Intersection_over_Union.*
   :scale: 50 %
   :alt: Jaccard index
   :align: center

   Intersection over Union

   Intersection over Union


Jaccard 距离用于衡量样本集合间的差异, 常定义如下:

.. math::
   d_{J}({\mathbb A}, {\mathbb B})=1-J({\mathbb A}, {\mathbb B})=\frac{|{\mathbb A} \cup {\mathbb B}|-|{\mathbb A} \cap {\mathbb B}|}{|{\mathbb A} \cup {\mathbb B}|}




加权 Jaccard 指数与距离
^^^^^^^^^^^^^^^^^^^^^^


概率 Jaccard 指数与距离
^^^^^^^^^^^^^^^^^^^^^^




Dice 系数
~~~~~~~~~~~~~~

Sørensen–Dice coefficient 简称为 :term:`Dice Coefficient` 或 Dice Similarity Coefficient, 衡量两个样本集合的相似性, 给定集合 :math:`{\mathbb A}, {\mathbb B}`, Dice系数定义为


.. math::
   S = {\rm DSC} = \frac{2|{\mathbb A}\cap{\mathbb B}|}{|{\mathbb A}|+|{\mathbb B}|}.
   :label: equ-DiceCoefficient

对于二值数据, 采用 true positive (TP), false positive (FP), 和 false negative (FN) 的定义, 则Dice系数可以表示为

.. math::
   S = {\rm DSC} = \frac{2{\rm TP}}{2{\rm TP} + {\rm FP} + {\rm FN}}.
   :label: equ-DiceCoefficientBin

容易得出 Dice系数与Jaccard系数间存在如下关系

.. math::
   \begin{array}{l}{J=S /(2-S)} \\ {S=2 J /(1+J)}\end{array}.
   :label: equ-DiceCoefficient

且此时有 :math:`{\rm DSC} = {\rm F}_1`.

.. hint::
   将查准率 :eq:`equ-Precision` 与查全率 :eq:`equ-Recall` 代入 :eq:`equ-Precision` 中, 有

   .. math::
      F_1 = \frac{(1+1^2)⋅P⋅R}{1^2⋅P+R} = \frac{(1+1^2)⋅\frac{\rm TP}{{\rm TP} + {\rm FP}}⋅ \frac{\rm TP}{{\rm TP} + {\rm FN}}}{1^2⋅\frac{\rm TP}{{\rm TP} + {\rm FP}} + \frac{\rm TP}{{\rm TP} + {\rm FN}}}\\
      =\frac{2{\rm TP}^2}{({\rm TP}+{\rm FP})({\rm TP}+{\rm FN})}⋅\frac{({\rm TP}+{\rm FP})({\rm TP}+{\rm FN})}{{\rm TP}(2{\rm TP}+{\rm FP}+{\rm FN})}\\
      = \frac{2{\rm TP}}{2{\rm TP} + {\rm FP}+ {\rm FN}} = {\rm DSC}



结构相似性度量
---------------------



有关图像领域中的结构相似性度量指标(SSIM)参见 :ref:`_Section-EvaluationMethodImageQuality` 小节.




.. rubric:: Footnotes

.. [#SetCard] 集合的势即即集合中元素的个数, 参见 :ref:`SubsubSection-SetCard`.

