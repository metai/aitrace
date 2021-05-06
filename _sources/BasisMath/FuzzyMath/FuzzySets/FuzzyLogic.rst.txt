.. _Section-FuzzyLogic:

模糊逻辑
=====================

布尔逻辑与模糊逻辑
--------------------

在经典二值逻辑(也称布尔逻辑)运算中, 变量只能取 :math:`0` 或 :math:`1`, 与经典的二值逻辑运算不同, **模糊逻辑** (:term:`Fuzzy Logic`) 允许变量取 :math:`0, 1` 之间的实数.


布尔逻辑与模糊逻辑算子
---------------------

常用布尔逻辑与模糊逻辑算子定义如下, 更多参见 :ref:`SubsubSectionFFuzzyOperator`

:: 

   |    |  布尔逻辑  |  模糊逻辑 |
   |====|===========|===========|
   | 与 | AND(x, y) | MIN(x, y) |
   |----|-----------|-----------|
   | 或 | OR(x, y)  | MAX(x, y) |
   |----|-----------|-----------|
   | 非 | NOT(x)    | 1 - x     |



模糊规则
--------------------

**模糊规则** (:term:`Fuzzy Rules`) 可用于对专家知识和常识进行建模. 一个模糊规则可以表示成三元组 :math:`(A, B, R)` 

IF-THEN
~~~~~~~~

``IF-THEN`` 模糊规则(Fuzzy Rules)

- 前提(Premise): x is A
- 含义(Implication): IF x is A THEN y is B
- 结果(Consequent): y is B


模糊逻辑推理步骤
------------------

模糊逻辑推理步骤如下

1. 模糊化(Fuzzification): 
2. 模糊运算(Fuzzy Logic Operator): 
3. 模糊规则推理(Fuzzy Rule): 
4. 去模糊化(De-fuzzyfication): 


.. .. blockdiag::

..    blockdiag {
..       "模糊化(Fuzzification)" -> "模糊运算(Fuzzy Logic Operator)" -> "模糊规则推理(Fuzzy Rule)" -> "去模糊化(De-fuzzyfication)";

..       blockdiag [color = "greenyellow"];
..       "模糊规则推理(Fuzzy Rule)" [color = "pink"];
..       "去模糊化(De-fuzzyfication)" [color = "green"];
..    }


.. hint::
   参考文献 :cite:`EnricTrillas.2015` Chapter 13 Reasoning and Fuzzy Logic


- [模糊逻辑与模糊推理](https://wenku.baidu.com/view/3039bbd73186bceb19e8bbf8.html)
- [模糊逻辑与模糊推理](https://wenku.baidu.com/view/261aac1eaeaad1f347933fbf.html?rec_flag=default)
- [模糊推理算法及应用](https://wenku.baidu.com/view/a89c6ac8a58da0116c1749c3.html)