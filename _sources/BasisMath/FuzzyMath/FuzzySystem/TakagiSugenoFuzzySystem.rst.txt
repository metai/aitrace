.. _Section-TakagiSugenoFuzzySystem:

Takagi-Sugeno模糊系统
=====================

Takagi-Sugeno模糊系统
-------------------------

Takagi-Sugeno(TS)模糊系统由Takagi等人于1985年提出 :cite:`Takagi.1985` , TS是 :ref:`Section-SingleInputSingleOutputFuzzySystem` , TS系统的规则包括语言类型的先行词和分段线性的明确输出的结论, 这使得去模糊化步骤变得多余.


对于单个先行词(antecedent), TS系统规则举例如下:

.. note::

   - 假定(premise): If :math:`x` is :math:`A_i`  then :math:`z_i = a_ix + b_i, i=1,\cdots,n` 

   - 事实(fact): :math:`x` is :math:`x_0`

   - 结论(conclusion): :math:`z` is :math:`z_0` .


单个先行词下的TS模糊系统控制算法:

.. hint::

   1. 输入明确值 :math:`x_0`
   2. 计算每个模糊规则的触发强度(firing strengths) : :math:`\alpha_i = A_i(x_0)` 
   3. 计算规则输出: :math:`z_i = a_ix_0 + c_i` 
   4. 最终输出: :math:`z_0 = \frac{\sum_{i=1}^n \alpha_i z_i}{\sum_{i=1}^n \alpha_i}` 



对于多个先行词(antecedent), TS系统规则举例如下:

.. note::

   - 假定(premise): If :math:`x` is :math:`A_i` and :math:`y` is :math:`B_i` then :math:`z_i = a_ix + b_iy + c_i, i=1,\cdots,n` 

   - 事实(fact): :math:`x` is :math:`x_0` and :math:`y` is :math:`y_0`

   - 结论(conclusion): :math:`z` is :math:`z_0` .


多个先行词下的TS模糊系统控制算法:

.. hint::

   1. 输入明确值 :math:`x_0, y_0`
   2. 计算每个模糊规则的触发强度(firing strengths) : :math:`\alpha_i = A_i(x_0)\wedge B_i(y_0)` 
   3. 计算规则输出: :math:`z_i = a_ix_0 + b_iy_0 + c_i` 
   4. 最终输出: :math:`z_0 = \frac{\sum_{i=1}^n \alpha_i z_i}{\sum_{i=1}^n \alpha_i}` 


Takagi-Sugeno模糊系统的近似特性
-------------------------------


理论上可以近似任意连续可微函数(differentiable function)

.. math::
   F(f, x) = \frac{\sum_{i=1}^nA_i(x)\cdot(a_ix+b_i)}{\sum_{i=1}^nA_i(x)}

待补充, 参见书籍 :cite:`Bede.2013` p126



