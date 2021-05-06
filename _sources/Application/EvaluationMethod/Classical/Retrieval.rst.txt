.. _Section-EvaluationMethodClassicalRetrieval:

信息检索
===========================


常用数据检索指标
-----------------

基本概念
~~~~~~~~~~~~~~~~

信息检索是指从一些相关(relevant)和不相关(irrelevant)的信息中检索出相关信息, 为便于论述, 记检索出的为正 (positive) 响应, 未检索出的为负 (negative) 响应. 下面论述的这些评价指标也通常被用在目标检测, 图像分割, 变化检测等应用领域. 主要包括以下指标

- 真正 (True Positive, TP): 实际上是正样本, 被检索为正样本, 真相关, 也称正确检出数
- 真负 (True Negative, TN): 实际上是负样本, 被检索为负样本, 真不相关
- 假正 (False Positive, FP): 实际上是负样本, 被检索为正样本, 假相关, 也称为虚警
- 假负 (False Negative, FN): 实际上是正样本, 被检索为负样本, 假不相关, 也称为漏检
- 查准率 (Precision): 检索到的真相关样本占检索到的样本的比例
- 查全率 (Recall): 检索到的真相关样本占总体相关样本的比例
- 相关样本总体: 检索到的真相关样本(正确检出数, TP)与未检索到的相关样本(FN)之和
- 不相关样本总体: 检索到的假相关样本(虚警, FP)与未检索到的不相关样本(TN)之和
- 检索到的样本: 检索到的真相关样本(正确检出数, TP)与检索到的假相关样本(FN)之和

.. figure:: ../../../_static/figs/Application/EvaluationMethod/Classical/Precisionrecall.*
   :scale: 50 %
   :alt: Precision and recall
   :align: center

   Precision and recall (来自维基百科)

   Precision and recall (来自维基百科)


查准率
~~~~~~~~~~~~~~~

**查准率** (:term:`Precision`) 指检索到的真相关样本占检索到的样本的比例, 即在所有检索结果中, 真正相关样本所占比例, 亦即所有正响应中, 真正相关的样本所占比例, 在分类问题中也称正预测值 (Positive PredictIve Value, PPV), 可以表示为

.. math::
   {\rm PPV} = {P} = \frac{\rm TP}{{\rm TP} + {\rm FP}}
   :label: equ-Precision



查全率
~~~~~~~~~~~~~~~

**查全率** (:term:`Recall`), 指检索到的真相关样本占总体相关样本的比例; 即在总体相关样本中, 检出的真正相关样本所占比例; 亦即所有正样本中, 响应为正的样本所占比例, 也称 **召回率** 在其它领域也称灵敏度(Sensitivity), 真正率(True Positive Rate, TPR)可以表示为

.. math::
   {\rm TPR} = {R} = \frac{\rm TP}{{\rm TP} + {\rm FN}}
   :label: equ-Recall



F-measure
~~~~~~~~~~~~~~~

查准率(:math:`P`)与查全率(:math:`R`)只能从一个方面衡量模型性能, 当查准率与查全率均比较高时, 模型效果越好. :term:`F-measure` 是一种融合了查准率与查全率的综合评价指标, 可以表示为

.. math::
   F_{\beta} = \frac{(1+\beta^2)⋅P⋅R}{\beta^2⋅P + R}
   :label: equ-F-measure

其中, :math:`\beta` 用于调整查准率与查全率所占比重, 通常取 :math:`\beta=0.5, 1, 2`. 当 :math:`\beta=0.5` 时, 更强调查准率; 当 :math:`\beta=2` 时, 更强调查全率.

.. warning::
   举例: 假设有 n 对预测与真值数据对 :math:`\{{\bm X}_i, {\bm Y}_i\}_{i=1}^n`, 其中前 :math:`n-1` 对的值全为零, 第 :math:`n` 对, 仅有一个正例样本点且被正确预测/检索.

   若将所有数据对看作总体, 有 :math:`{\rm TP}=1`, :math:`{\rm FP}=0, {\rm FN}=0`, 从而有查准率 :math:`P=1`, 查全率 :math:`R=1`, 继而有F值 :math:`F_{all} = 1`

   若将每一个数据对看作总体, 对于前 :math:`n-1` 个数据, 有 :math:`{\rm TP}=0`, :math:`{\rm FP}=0, {\rm FN}=0`, 从而有查准率 :math:`P=0`, 查全率 :math:`R=0`, :math:`F^{(i)}=0, i=1,2,\cdots, n-1`; 对于第 :math:`n` 个数据对有 :math:`{\rm TP}=1`, :math:`{\rm FP}=0, {\rm FN}=0`, 从而有查准率 :math:`P=1`, 查全率 :math:`R=1`, :math:`F^{(n)}=1`, 故平均F值为 :math:`F_{avg}=(F^{(1)} + F^{(2)} + F^{(n-1)} + F^{(n)}) / n = 1/n`.


虚警率
~~~~~~~~~~~~

**虚警率** (:term:`False Alarm Rate`) 也称错误发现率 (False Discovery Rate, FDR), 是指在检索出的样本中, 不相关的样本所占比例, 与查准率互补, 可以表示为

.. math::
   {\rm FDR} = \frac{\rm FP}{{\rm TP} + {\rm FP}} = 1 - P
   :label: equ-FalseDiscoveryRate


漏检率
~~~~~~~~~~~~

**漏检率** (:term:`Miss Alarm Rate`) 也称假负率 (False Negative Rate, FNR), 是指未检索出的正类样本占总正类样本的比例, 与召回率互补, 可以表示为

.. math::
   {\rm FNR} = \frac{\rm FN}{{\rm FN} + {\rm TP}} = 1 - R
   :label: equ-FalseNegativeRate


总结
~~~~~~~~~~~~~~~~



- sensitivity, recall, hit rate, or true positive rate (TPR)

  .. math::
     { \mathrm {TPR} ={\frac {\mathrm {TP} }{\mathrm {P} }}={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FN} }}=1-\mathrm {FNR} }
- specificity, selectivity or true negative rate (TNR)

  .. math::
     { \mathrm {TNR} ={\frac {\mathrm {TN} }{\mathrm {N} }}={\frac {\mathrm {TN} }{\mathrm {TN} +\mathrm {FP} }}=1-\mathrm {FPR} }
- precision or positive predictive value (PPV)

  .. math::
     { \mathrm {PPV} ={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FP} }}=1-\mathrm {FDR} }
- negative predictive value (NPV)

  .. math::
     { \mathrm {NPV} ={\frac {\mathrm {TN} }{\mathrm {TN} +\mathrm {FN} }}=1-\mathrm {FOR} }
- miss rate or false negative rate (FNR)

  .. math::
     { \mathrm {FNR} ={\frac {\mathrm {FN} }{\mathrm {P} }}={\frac {\mathrm {FN} }{\mathrm {FN} +\mathrm {TP} }}=1-\mathrm {TPR} }
- fall-out or false positive rate (FPR)

  .. math::
     { \mathrm {FPR} ={\frac {\mathrm {FP} }{\mathrm {N} }}={\frac {\mathrm {FP} }{\mathrm {FP} +\mathrm {TN} }}=1-\mathrm {TNR} }
- false discovery rate (FDR)

  .. math::
     { \mathrm {FDR} ={\frac {\mathrm {FP} }{\mathrm {FP} +\mathrm {TP} }}=1-\mathrm {PPV} }
- false omission rate (FOR)

  .. math::
     { \mathrm {FOR} ={\frac {\mathrm {FN} }{\mathrm {FN} +\mathrm {TN} }}=1-\mathrm {NPV} }
- Threat score (TS) or Critical Success Index (CSI)

  .. math::
     { \mathrm {TS} ={\frac {\mathrm {TP} }{\mathrm {TP} +\mathrm {FN} +\mathrm {FP} }}}
- accuracy (ACC)

  .. math::
     { \mathrm {ACC} ={\frac {\mathrm {TP} +\mathrm {TN} }{\mathrm {P} +\mathrm {N} }}={\frac {\mathrm {TP} +\mathrm {TN} }{\mathrm {TP} +\mathrm {TN} +\mathrm {FP} +\mathrm {FN} }}}
- F1 score: is the harmonic mean of precision and sensitivity

  .. math::
     { \mathrm {F} _{1}=2\cdot {\frac {\mathrm {PPV} \cdot \mathrm {TPR} }{\mathrm {PPV} +\mathrm {TPR} }}={\frac {2\mathrm {TP} }{2\mathrm {TP} +\mathrm {FP} +\mathrm {FN} }}}
- Matthews correlation coefficient (MCC)

  .. math::
     { \mathrm {MCC} ={\frac {\mathrm {TP} \times \mathrm {TN} -\mathrm {FP} \times \mathrm {FN} }{\sqrt {(\mathrm {TP} +\mathrm {FP} )(\mathrm {TP} +\mathrm {FN} )(\mathrm {TN} +\mathrm {FP} )(\mathrm {TN} +\mathrm {FN} )}}}}
- Informedness or Bookmaker Informedness (BM)

  .. math::
     { \mathrm {BM} =\mathrm {TPR} +\mathrm {TNR} -1}
- Markedness (MK)

  .. math::
     { \mathrm {MK} =\mathrm {PPV} +\mathrm {NPV} -1}
