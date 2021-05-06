.. _Section-ReconstructionSparsitySamplingReconSparseSignalProcessing:

重构
=====================


.. _Subsection-RestrictedIsometryProperty:

有限等距性
---------------

Candes等人于2005年提出 **有限等距常数** (:term:`Restricted Isometry Constant`, RIC) :cite:`E.J.Candes.2005` , 文中给出的定义如下

.. _defRIC1:

.. proof:definition:: 有限等距常数 (Restricted Isometry Constant)

   设矩阵 :math:`{\bm A}` 由向量集合 :math:`\{{\bm a}_i \in {\mathbb R}^p, i\in {\mathbb I}\}` 构成. 对于每个整数 :math:`1\leq s \leq |{\mathbb I}|` , 定义 :math:`{\bm A}` 的 :math:`s` 阶有限等距常数 :math:`\delta_s` 为使得 :math:`{\bm A}_{\mathbb T}` 满足如下条件的最小正数

   .. math::
      (1-\delta_s)\|{\bm x}\| \leq \|{\bm A}_{\mathbb T}{\bm x}\| \leq (1+\delta_s)\|{\bm x}\| \\
      \forall {\mathbb T}\subset {\mathbb I}
      :label: equ_RIC1_CS


   其中, :math:`{\bm x} \in {\mathbb R}^n_k` 为 :math:`k` 稀疏信号. :math:`|{\mathbb I}|` 为集合 :math:`{\mathbb I}` 的势 (:term:`Cardinality`).


RIP 被广泛用于压缩感知 (:term:`Compressive Sensing`, CS) 中 :cite:`Candes.2008` . 在CS中, 感知矩阵 (:math:`{\bm A} = {\bm \Phi}{\bm \Psi}` ) 是否满足RIP条件直接决定了重构信号质量. 在CS中, 矩阵 :math:`{\bm A}` 的有限等距常数定义为

.. _defRIC2:

.. proof:definition:: 有限等距常数 (Restricted Isometry Constant)

   设 :math:`{\bm A} = [{\bm a}_1, {\bm a}_2, \cdots, {\bm a}_n]\in {\mathbb R}^{m\times n}` , :math:`{\bm a}_i \in {\mathbb R}^m, i=1,2,\cdots, n`. 对于每个整数 :math:`s\in [1, n]`, 定义矩阵 :math:`{\bm A}` 的有限等距常数为满足下式的最小的数 :math:`\delta_s`

   .. math::
      (1-\delta_s)\|{\bm x}\| \leq \|{\bm A}{\bm x}\| \leq (1+\delta_s)\|{\bm x}\|
      :label: equ_RIC2_CS

   其中, :math:`{\bm x} \in {\mathbb R}^n_k` 为 :math:`k` 稀疏信号.

矩阵 :math:`{\bm A}` 具有有限等距特性 (:term:`Restricted Isometry Property`, RIP) :cite:`Foucart.2013` 是指对于充分小的 :math:`\delta_s` , 矩阵 :math:`{\bm A}` 满足 :eq:`equ_RIC2_CS`. :eq:`equ_RIC2_CS` 表明, 矩阵 :math:`{\bm A}` 对信号 :math:`\bm x` 投影前后的长度仅有微小的改变. **即RIP特性保证了来自矩阵** :math:`\bm A` **的投影可以保持两个信号** :math:`{\bm x}_1, {\bm x}_2` **间的距离**, :eq:`equ_RIC2_CS` 可以等价地表示为

.. math::
   (1-\delta_s)\|{\bm x}_1-{\bm x}_2\| \leq \|{\bm A}({\bm x}_1-{\bm x}_2)\| \leq (1+\delta_s)\|{\bm x}_1-{\bm x}_2\|.
   :label: equ_RIC2_CS_2

RIP 保证了稀疏信号 :math:`\bm x` 可以被以高概率重构.
