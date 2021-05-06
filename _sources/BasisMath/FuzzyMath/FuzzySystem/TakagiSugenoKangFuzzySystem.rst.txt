.. _Section-TakagiSugenoKangFuzzySystem:

Takagi-Sugeno-Kang模糊系统
=============================

如今比较常用的是 Takagi-Sugeno-Kang (TSK) 型模糊推理系统 (Fuzzy Inference System, FIS) :cite:`Takagi.1985,Sugeno.1988`. Petr 等人于2005年提出 在线学习式TSK模型 :cite:`1C.Petr.2005` , Gu等人于2018年提出基于贝叶斯的TSK-FIS :cite:`X.Gu.2018` .


TSKFIS原理
-------------------

一个TSK模糊系统主要由 "IF-THEN" 模糊规则构成. 给定 :math:`d-` 维输入向量 :math:`{\bm x} = [x_1, x_2, \cdots, x_d]^T` , 记第 :math:`k` 个规则为 :math:`R^k` , 在则TSK模糊系统中, :math:`R^k` 可以表示为

.. math::
   {\rm IF}\; x_1(k)\; {\rm is}\; A_{k1}, x_2(k)\; {\rm is}\; A_{k2}, \cdots, x_d(k)\; {\rm is}\; A_{kd} \\
   {\rm THEN} \; f_k({\bm x}) = q_{k0} + \sum_{j=1}^d q_{kj}x_j = {\bm q}_k^T \tilde{\bm x}_n

其中, :math:`A_{ki} (i=1,2,\cdots, d)` 是一个模糊集, :math:`k=1,2,\cdots, K` , :math:`\tilde{{\bm x}} = [1, {\bm x}_n^T]^T` . 且 :math:`{\bm q}_k = [q_{k0}, q_{k1}, \cdots, q_{kd}]^T` 是第 :math:`k` 个规则对应结论的参数向量, 为指定或可学习(如自适应神经模糊推理系统中的权重).

若使用高斯核表示模糊集 :math:`A_{ki}` 对应的隶属函数 :math:`A_{ki}(x_i)` , 则

.. math::
   \mu_{A_{ki}}(x_i) = {\rm exp}\left(\frac{-\|x_i - c_{ki}\|^2}{\sigma_{ki}^2}\right)

其中, :math:`c_{ki}, \sigma_{ki}` 分别对应高斯隶属函数中心(均值)和宽度(标准差). 

TSK模糊系统的输出可以表示为

.. math::
   \hat{y} = \sum_{k=1}^K \frac{\mu_k({\bm x})}{\sum_{k=1}^K\mu_{k}({\bm x})} f_k({\bm x}) = \sum_{k=1}^K \hat{\mu}_K({\bm x})f_k({\bm x})

其中, :math:`\mu_k({\bm x})` 和 :math:`\hat{\mu}({\bm x})` 分别为第 :math:`k` 个规则对应的模糊隶属函数和归一化模糊隶属函数:

.. math::
   \mu_k({\bm x}) = \prod_{i=1}^d \mu_{A_{ki}}(x_i), \; \hat{\mu}_k({\bm x}) = \frac{\mu_k({\bm x})}{\sum_{k=1}^K \mu_k({\bm x})}




