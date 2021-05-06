.. _Section-ADMM:

交替方向乘子法
=====================

交替方向乘子法 ( :term:`Alternating Direction Method of Multipliers`, ADMM) :cite:`S.Boyd.2011` 结合了对偶分解 (dual decomposition) 和增广拉格朗日方法的优点, 最早可追溯到20世纪70年代中期 :cite:`GABAY197617,Glowinski.1975`.

主页 [#FootnoteADMMlink]_ 中提供了所有相关论文, 代码及应用文档.



该问题与如下约束优化问题等价

.. math::
    {P_1}: {\rm min}_{{\bm x}, {\bm y}} f({\bm x}) + g({\bm y})\ \ {\rm s.t.} \ \ {\bm x} = {\bm y}.

尽管这种变化可能看起来微不足道, 但现在可以使用约束优化方法来解决这个问题, 如增广拉格朗日方法. 此时目标函数被 :math:`{\bm x}` 与 :math:`{\bm y}` 分离, 对偶更新问题在于求解一个同时满足 :math:`{\bm x}, {\bm y}` 的近似函数. ADMM算法通过交替迭代的方法求解该问题, 即先固定变量 :math:`{\bm y}` 优化另一个变量 :math:`\bm x`, 再固定变量 :math:`{\bm x}` 优化变量 :math:`\bm y`, 如此交替优化求解. 虽然这并非准确地最优化求解, 但该方法最终可以收敛到很好的解.


ADMM原理
------------

ADMM 用于求解如下形式的约束优化问题

.. math::
    \begin{array}{ll}{\text { min }} & {f({\bm x})+g({\bm y})} \\ {\text {s.t. }} & {{\bm A} {\bm x} + {\bm B}{\bm y} = {\bm c}}\end{array}
    :label: equ-ADMM_OriginalProblem

其中, :math:`f,g` 为凸函数, :math:`{\bm x}\in{\mathbb R}^N`, :math:`{\bm y}\in{\mathbb R}^M`, :math:`{\bm A}\in{\mathbb R}^{p\times N}`, :math:`{\bm B}\in{\mathbb R}^{p\times M}`, :math:`{\bm c}\in{\mathbb R}^{p}`.


与乘子法类似, :eq:`equ-ADMM_OriginalProblem` 的增广拉格朗日形式为

.. math::
    L({\bm x}, {\bm y}, {\bm \lambda}) = f({\bm x}) + g({\bm y}) + {\bm \lambda}^T({\bm A}{\bm x}+{\bm B}{\bm y}-{\bm c}) + \frac{\mu}{2}\|{\bm A}{\bm x}+{\bm B}{\bm y}-{\bm c}\|_2^2,
    :label: equ-ADMM_AugmentedLagrangianProblem

其中, :math:`\mu` 为惩罚因子.

ADMM算法的参数迭代更新规则为

.. math::
    \begin{aligned} {\bm x}^{k+1} & :=\underset{\bm x}{\operatorname{argmin}}\ L_{\mu}\left({\bm x}, {\bm y}^{k}, {\bm \lambda}^{k}\right) \\ {\bm y}^{k+1} & :=\underset{\bm y}{\operatorname{argmin}}\ L_{\mu}\left({\bm x}^{k+1}, {\bm y}, {\bm \lambda}^{k}\right) \\ {\bm \lambda}^{k+1} & :={\bm \lambda}^{k}+\mu\left({\bm A} {\bm x}^{k+1} + {\bm B}{\bm y}^{k+1} - {\bm c}\right) \end{aligned}


:eq:`equ-ADMM_OriginalProblem` 增广拉格朗日乘子法参数更新规则为

.. math::
    \begin{aligned}\left({\bm x}^{k+1}, {\bm y}^{k+1}\right) & :=\underset{{\bm x}, {\bm y}}{\operatorname{argmin}} L_{\mu}\left({\bm x}, {\bm y}, {\bm \lambda}^{k}\right) \\ {\bm \lambda}^{k+1} & :={\bm \lambda}^{k}+\mu\left({\bm A} {\bm x}^{k+1}+{\bm B} {\bm y}^{k+1}-{\bm c}\right) \end{aligned}
    :label: equ-ALM_Iterations


可以看出, 增广拉格朗日乘子法需要同时优化两个原始变量 :math:`\bm x`, :math:`\bm y`. 与增广拉格朗日乘子法不同的是, 在ADMM中, :math:`\bm x` 与 :math:`\bm y` 采用交替迭代 (alternating direction) 更新的方法.


Scale版ADMM原理
-----------------

通过组合增广拉格朗日函数中的线性项与二次项并缩放对偶变量.


.. math::
    \begin{aligned}
    {\bm \lambda}^T{\bm r} + {\frac{\mu}{2}}\|{\bm r}\|_2^2 &= \frac{\mu}{2}\|{\bm r}+{\frac{1}{\mu}}{\bm \lambda}\|_2^2 - \frac{1}{2\mu}\|\bm \lambda\|_2^2 \\
    &= \frac{\mu}{2} \|{\bm r} + {\bm u}\|_2^2 - \frac{\mu}{2}\|{\bm u}\|_2^2
    \end{aligned}

其中, :math:`{\bm r} = {\bm A}{\bm x} + {\bm B}{\bm y} - {\bm c}` 为残差, :math:`{\bm u} = \frac{1}{\mu}{\bm \lambda}` 为scale版对偶变量, 对应的scale版更新规则为

.. math::
    \begin{aligned} {\bm x}^{k+1} & :=\underset{{\bm x}}{\operatorname{argmin}}\left(f({\bm x})+(\mu / 2)\left\|{\bm A} {\bm x}+{\bm B} {\bm y}^{k}-{\bm c}+{\bm u}^{k}\right\|_{2}^{2}\right) \\ {\bm y}^{k+1} & :=\underset{{\bm y}}{\operatorname{argmin}}\left(g({\bm y})+(\mu / 2)\left\|{\bm A} {\bm x}^{k+1}+{\bm B} {\bm y}-{\bm c}+{\bm u}^{k}\right\|_{2}^{2}\right) \\ {\bm u}^{k+1} & :={\bm u}^{k}+{\bm A} {\bm x}^{k+1}+{\bm B} {\bm y}^{k+1}-{\bm c} \end{aligned}

记第 :math:`k` 次的残差为 :math:`{\bm r}^k = {\bm A}{\bm x}^k + {\bm B}{\bm y}^k - {\bm c}`, 则有scale版对偶变量更新规则

.. math::
    {\bm u}^k = {\bm u}^0 + \sum_{j=1}^k {\bm r}^j.


收敛性分析
------------


最优条件与停止准则
----------------


实验与分析
------------


.. rubric:: Footnotes

.. [#FootnoteADMMlink] https://web.stanford.edu/~boyd/admm.html



https://blog.csdn.net/pizibing880909/article/details/21192243

