.. _Section-FuzzySupportVectorMachine:

模糊支撑矢量机
=====================

**模糊支撑矢量机** (:term:`Fuzzy Support Vector Machine`, FSVM) 通过在SVM中引入模糊性质, 使得对不干净输入更加鲁棒. :cite:`ChunFuLin.2002` , :cite:`Lin.2005` , :cite:`Jiang.2006` .


FSVM原理
-----------------

现实世界中, 每个训练样本的重要性不一, 通常一些训练样本比另外一些更重要, 我们希望有意义的样本正确分类, 而不关心噪声样本是否被错分 :cite:`ChunFuLin.2002` . 假设有训练样本集 :math:`{\mathbb S} = \{({\bm x}_i, {\bm y}_i)\}_{i=1}^N` , 为每一个训练样本分配一个隶属度 :math:`\mu_i`, 则样本集重新表示为 :math:`\tilde{\mathbb S} = \{({\bm x}_i, {\bm y}_i, \mu_i)\}_{i=1}^N`, SVM 优化问题 :eq:`equ-SVM_problem` 变为

.. math::
	\begin{array}{c}{\text { minimize } \frac{1}{2} \|\bm{w}\|^2 + C \sum_{i=1}^{N} \mu_i\xi_{i}} \\ {\text { subject to } y_{i}\left(\bm{w} \cdot \bm{z}_{i}+b\right) \geq 1-\xi_{i}, \quad i=1, \ldots, N} \\ {\xi_{i} \geq 0, \quad i=1, \ldots, N}\end{array},
   :label: equ-FSVM_problem

其中, :math:`{\bm w}` 为模型参数, :math:`C` 为平衡因子, :math:`\xi_i` 为第 :math:`i` 个样本对应误差, :math:`{\bm z}_i` 为第 :math:`i` 个样本 :math:`{\bm x}_i` 在特征空间中的象 :math:`{\bm z}_i = f({\bm x}_i)` , :math:`f: {\mathbb R}^n \rightarrow {\mathbb R}^m`.

.. _SubsubSection-FSVM_MembershipFuncSelection:

隶属函数选择
-----------------

基于时间特性
~~~~~~~~~~~~

对于序列学习, 样本的重要性与样本到达时间紧密相关, 特别是在实时信号处理中, 最新到达的样本比以往的样本更重要, 因而可以根据时间来确定隶属度 :cite:`ChunFuLin.2002` , 即

.. math::
	{\mu}_{i}=f_{1}\left(t_{i}\right)=\frac{1-\sigma}{t_{N}-t_{1}} t_{i}+\frac{t_{N} \sigma-t_{1}}{t_{N}-t_{1}},

其中, :math:`t_{1}<\cdots t_{i}<\cdots t_{N}` 是训练样本到达时间序列.


基于类别中心
~~~~~~~~~~~~

使用样本到类别中心的距离作为隶属度可以减少异常值的影响, 假设有 :math:`K` 个类别, 用 :math:`\bar{{\bm x}_k}` 表示第 :math:`k` 类的均值中心. 可定义如下隶属函数

.. math::
	{\mu}_i={1-\left|\bar{\bm x}_{k}-{\bm x}_{i}\right| / \left(r_{k}+\delta\right)} \;\;{\text { if } y_{i}=k}

其中, :math:`k=1,2,\cdots,K` , :math:`\delta > 0` 以避免 :math:`\mu_i = 0` , :math:`r_{k}` 为类别 :math:`k` 的半径:

.. math::
	r_{k}=\max _{\left\{\bm{x}_{i} : y_i=k\right\}}\left|\bar{\bm x}_{k}-\bm{x}_{i}\right|.


基于训练误差
~~~~~~~~~~~~

还可以根据训练误差来设置隶属度 :cite:`Zheng.2013`, 这种方法需要先使用SVM训练, 将得到的误差 :math:`e` 进行如下公式转换为隶属度:

.. math::
	{\mu}_i=f_{3}\left(e_{i}\right)=1-\frac{e_{i}}{e_{\rm max}+\delta}

其中, :math:`e_{\rm max}=\max \left\{e_{1}, \cdots, e_{i}, \cdots, e_{N}\right\}` , :math:`\delta>0` .



实验及结果
--------------

