.. _Section-DictionaryTypeRepresentationDictionarySparseSignalProcessing:

字典的类型
=====================

什么是字典
--------------



字典的种类
---------------


完备与过完备
~~~~~~~~~~~~~~~~~~~


对于给定的信号 :math:`{\bm y}\in {\mathbb R}^{M\times N}`, 期望找到一组过完备基 :math:`{\bm D} = [{\bm d}_1, {\bm d}_2,\cdots, {\bm d}_N]`, :math:`{\bm d}_i\in {\mathbb R}^{M\times 1}`, 和一组系数 :math:`{\bm x}`, 满足

.. math::
   {\bm y} = {\bm D}{\bm x} = x_1 {\bm d}_1 + x_2 {\bm d}_2 + \cdots, x_N{\bm d}_N

当基的个数 :math:`N` 大于信号 :math:`{\bm y}` 的维度 :math:`M` 时, 称基/字典 :math:`{\bm D}` 是 **过完备字典** (Overcomplete Dictionary); 当基的个数 :math:`N` 等于信号 :math:`{\bm y}` 的维度 :math:`M` 时, 称基/字典 :math:`{\bm D}` 是 **完备字典** (Overcomplete Dictionary).


冗余与非冗余
~~~~~~~~~~~~~~~~~~


正交与非正交
~~~~~~~~~~~~~~~~~~~




总结
~~~~~~~~~~~~

.. note::
   - 完备字典是指字典中的原子张成的空间可以覆盖整个信号空间.
   - 冗余字典是指字典中存在线性相关的原子.
   - 冗余字典可能不完备, 完备字典有可能冗余.




