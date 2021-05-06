.. _Section-MeasurementLinearCompressiveSensingSparseSignalProcessing:

线性压缩感知观测
=====================





感知矩阵的设计
------------------

感知矩阵的设计需要满足如下条件.

零空间条件
~~~~~~~~~~~~

设有信号空间 :math:`{\mathbb X}^n` 中的任意不同信号 :math:`{\bm x}_1, {\bm x}_2 \in {\mathbb X}^n`, 感知矩阵 :math:`{\bm A}\in{\mathbb R}^{m\times n}`, 对应的观测向量分别为 :math:`{\bm y}_1, {\bm y}_2 \in {\mathbb Y}^m`. 若想从 :math:`{\bm y}_1, {\bm y}_2` 中恢复 :math:`{\bm x}_1, {\bm x}_2`, 需保证不同信号在投影后依然不同 :math:`{\bm y}_1 = {\bm A}{\bm x}_1 \neq {\bm y}_2 = {\bm A}{\bm x}_2`, 即 :math:`{\bm A}({\bm x}_1 - {\bm x}_2) \neq 0`, 亦即 :math:`{\bm x}_1 - {\bm x}_2 \notin {\mathcal N}({\bm A})`. 这一性质可以通过矩阵的 Spark, 零空间性质等表达.

.. _theNSP1:

.. proof:theorem::

   对于 :math:`\forall {\bm y}\in {\mathbb Y}^m`, 当且仅当 :math:`{\rm Spark}({\bm A}) > 2k` 时, 最多存在一个 :math:`k` 稀疏信号 :math:`{\bm x}\in {\mathbb X}^n_k`, 使得 :math:`{\bm y} = {\bm A}{\bm x}` 成立.

该定理的证明参见文献 :cite:`Eldar.2012`.

下面介绍矩阵的零空间性质 (Null Space Property, NSP) :cite:`Eldar.2012`.

.. _defNSP1:

.. proof:definition:: 零空间性质 (Null Space Property, NSP)

   设矩阵 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}` , :math:`{\bm a}_i \in {\mathbb R}^m, i=1,2,\cdots, n`. 若 :math:`\forall {\bm v}\in{\mathcal N}({\bm A})`, 满足

   .. math::
      \|{\bm v}_{\mathbb K}\|_1 < \|{\bm v}_{\bar{\mathbb K}}\|_1
      :label: equ_NSP_CS

   其中, :math:`{\mathbb K} \subset {\mathbb N}`, :math:`{\mathbb N}=\{1, 2, \cdots, n\}`, :math:`\bar{\mathbb K}` 为 :math:`{\mathbb K}` 在 :math:`{\mathbb N}` 中的补集, :math:`{\rm card}({\mathbb K}) \leq k`. 则称矩阵 :math:`\bm A` 满足 :math:`k` 阶 **零空间性质** (Null Space Property, NSP).

下面介绍矩阵的零空间性质 (:term:`Null Space Property`, NSP) 的另一种定义 :cite:`Foucart.2013`.

.. _defNSP2:

.. proof:definition:: 零空间性质 (Null Space Property, NSP)

   设矩阵 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}` , :math:`{\bm a}_i \in {\mathbb R}^m, i=1,2,\cdots, n`. 若 :math:`\forall {\bm v}\in{\mathcal N}({\bm A})`, :math:`\exists C>0` 满足

   .. math::
      \|{\bm v}_{\mathbb K}\|_2 \leq C\frac{\|{\bm v}_{\bar{\mathbb K}}\|_1}{\sqrt{k}}
      :label: equ_NSP_CS

   其中, :math:`{\mathbb K} \subset {\mathbb N}`, :math:`{\mathbb N}=\{1, 2, \cdots, n\}`, :math:`\bar{\mathbb K}` 为 :math:`{\mathbb K}` 在 :math:`{\mathbb N}` 中的补集, :math:`{\rm card}({\mathbb K}) \leq k`. 则称矩阵 :math:`\bm A` 满足 :math:`k` 阶 **零空间性质** (:term:`Null Space Property`, NSP).


有限等距性质
~~~~~~~~~~~~

RIP 被广泛用于压缩感知 (:term:`Compressive Sensing`, CS) 中 :cite:`Candes.2008` . 在CS中, 感知矩阵 (:math:`{\bm A} = {\bm \Phi}{\bm \Psi}` ) 是否满足RIP条件直接决定了重构信号质量. 在CS中, 矩阵 :math:`{\bm A}` 的有限等距常数定义为

.. _defRIC2:

.. proof:definition:: 有限等距常数 (Restricted Isometry Constant)

   设 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}` , :math:`{\bm a}_i \in {\mathbb R}^m, i=1,2,\cdots, n`. 对于每个整数 :math:`k\in [1, n]` , 定义矩阵 :math:`{\bm A}` 的 :math:`k` 阶有限等距常数为满足下式的最小的数 :math:`\delta_k`

   .. math::
      (1-\delta_k)\|{\bm x}\| \leq \|{\bm A}{\bm x}\| \leq (1+\delta_k)\|{\bm x}\|
      :label: equ_RIP_CS

   其中, :math:`{\bm x} \in {\mathbb R}^n_k` 为 :math:`k` 稀疏信号.

   更一般地, 设 :math:`0 < \beta < \gamma <+\infty`,

   .. math::
      {\beta}\|{\bm x}\| \leq \|{\bm A}{\bm x}\| \leq {\gamma}\|{\bm x}\|
      :label: equ_RIP_CS2

   其中, :math:`{\bm x} \in {\mathbb R}^n_k` 为 :math:`k` 稀疏信号.

矩阵 :math:`{\bm A}` 具有 **有限等距特性** (:term:`Restricted Isometry Property`, RIP) :cite:`Foucart.2013` 是指对于足够大的 :math:`k` 和充分小的 :math:`\delta_k` , 矩阵 :math:`{\bm A}` 满足 :eq:`equ_RIP_CS`. :eq:`equ_RIP_CS` 表明, 矩阵 :math:`{\bm A}` 对信号 :math:`\bm x` 投影前后的长度仅有微小的改变. **即RIP特性保证了来自矩阵** :math:`\bm A` **的投影可以保持两个信号** :math:`{\bm x}_1, {\bm x}_2` **间的距离**, :eq:`equ_RIP_CS` 可以等价地表示为

.. math::
   (1-\delta_k)\|{\bm x}_1-{\bm x}_2\| \leq \|{\bm A}({\bm x}_1-{\bm x}_2)\| \leq (1+\delta_k)\|{\bm x}_1-{\bm x}_2\|.
   :label: equ_RIP_CS_2


一个矩阵 :math:`\bm A` 以很高概率满足 RIP, 也就保证了稀疏信号 :math:`\bm x` 可以被以高概率重构.

.. hint::
   对于 :eq:`equ_RIP_CS2` 中的矩阵 :math:`\bm A`, 用 :math:`\sqrt{2/(\beta + \gamma)}` 乘以 :math:`\bm A`, 则有 :math:`\sqrt{2/(\beta + \gamma)}{\bm A}` 满足 :eq:`equ_RIP_CS`, 其中, :math:`\delta_k = (\beta-\gamma)/(\beta+\gamma)`.
   更多内容参见 :ref:`Subsection-RestrictedIsometryProperty` 小节.



相干性/一致性条件
~~~~~~~~~~~~~~~~~~~


.. _defCoherence:

.. proof:definition:: 相干性/一致性 (Coherence)

   设 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}` , :math:`{\bm a}_i \in {\mathbb R}^m, i=1,2,\cdots, n`. 对于每个整数 :math:`k\in [1, n]` , 定义矩阵 :math:`{\bm A}` 的一致性为

   .. math::
      \mu({\bm A}) = \max _{1 \leq i \neq j \leq N}\left|\left\langle{\frac{\bm{a}_{i}}{\|\bm{a}_{i}\|_2}}, \frac{\bm{a}_{j}}{\|\bm{a}_{j}\|_2}\right\rangle\right| = \max _{1 \leq i \neq j \leq N}\frac{\left|\left\langle \bm{a}_{i}, \bm{a}_{j}\right\rangle\right|}{\|\bm{a}_{i}\|_2\|\bm{a}_{j}\|_2}
      :label: equ-MatrixCoherence

.. proof:theorem::

   对于任意矩阵 :math:`{\bm A}` 有

   .. math::
      {\rm Spark}({\bm A}) \geq 1+\frac{1}{\mu({\bm A})}
      :label: equ-CoherenceTheorem1


.. proof:theorem::

   对于矩阵 :math:`{\bm A}` , 若

   .. math::
      k < \frac{1}{2}\left(1+\frac{1}{\mu({\bm A})}\right)
      :label: equ-CoherenceTheorem2

   则对于 :math:`\forall {\bm y}\in{\mathbb R}^m` , 最多存在一个 :math:`k` 稀疏信号, 满足 :math:`{\bm y} = {\bm A}{\bm x}`.

稳定性
~~~~~~~~~~~~~~~~~~~~

.. _defCStable:

.. proof:definition:: C稳定系统

   设有感知系统 :math:`{\mathcal F} = {\bm A}\in{\mathbb R}^{m\times n} : {\mathbb R}^n \rightarrow {\mathbb R}^m`, 重构算法 :math:`{\mathcal G}: {\mathbb R}^m \rightarrow {\mathbb R}^n`, :math:`m \leq n` . 若对于任意 :math:`k` 稀疏信号 :math:`{\bm x}\in {\mathbb R}^n_k` 和误差向量 :math:`{\bm e} \in {\mathbb R}^m`, 有

   .. math::
      \|{\mathcal G}({\mathcal F}({\bm x}) + {\bm e}) - {\bm x}\|_2 = \|{\mathcal G}({\bm A}{\bm x} + {\bm e}) - {\bm x}\|_2 \leq C\|{\bm e}\|_2
      :label: equ-labelname

   则称系统 :math:`\{{\mathcal F}={\bm A}, {\mathcal G}\}` 是 :math:`C` 稳定的.

该定义说明, 对于 :math:`C` 稳定的系统, 若观测存在很小的误差或者对观测施加小量的噪声, 重建质量不会受到大的影响, RIP 保证了上述性质的成立.

讨论
~~~~~~~~~~~~~~~~~~~


- NSP 不容易证明, 且容易受噪声影响;
- RIP 比 NSP 更为严格和鲁棒 [#f1]_ .





感知矩阵的构造
------------------


常见感知矩阵
------------------



.. rubric:: Footnotes

.. [#f1] 参见文献 :cite:`Eldar.2012` p24.
