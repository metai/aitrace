.. _Section-CompressiveSensingImagingSARRadar:

压缩感知成像
=====================

压缩感知SAR成像
--------------------------

越来越多的基于压缩感知的SAR成像方法被提出 :cite:`Baraniuk2007Compressive,Patel2010Compressed,Kang2016Two` .

匹配追踪用于量子模拟 :cite:`2003JChPh.118.6720W`

SAR imaging process can be formulated as

.. math::
   {\bm s} = {\bm A}{\bm g} + {\bm n},

where, :math:`{\bm s}` is the :math:`m = MN\times 1` recieved SAR raw data vector in phase history domain,
:math:`\bm g` is the :math:`n = HW \times 1` reflection vector of scene. :math:`\bm A` represents the
the mapping from scene to SAR raw data. :math:`\bm n` is the noise vector.

If :math:`\bm g` is not sparse enough, assume that exist a basis :math:`{\bm D} = ({\bm d}_1, {\bm d}_2, \cdots, {\bm d}_n)`
that satisfies :math:`{\bm g} = {\bm D}{\bm x}` , where, :math:`\bm x` is a :math:`K` sparse :math:`n\times 1` vector, and
:math:`\bm D` is the so called dictionary matrix of size :math:`n\times n` .

Our goal is minimize

.. math::
   \mathop {\rm min}\limits_{\bm x}\|{\bm x}\|_p, \ \  s.t. \  {\bm s} = {\bm A}{\bm D}{\bm x} + {\bm n},

i.e.

.. math::
   \mathop {\rm min}\limits_{\bm{x}} = \|{\bm s} - {\bm A}{\bm D}{\bm x}\|_2 + \lambda \|{\bm x}\|_p,

where, :math:`\lambda` is the balance factor, and :math:`|\cdot|_p, (0<p<1)` is the :math:`\ell_p` norm.

Let :math:`{\bm \Phi} = {\bm A}{\bm D}` , then we have

.. math::
   \mathop {\rm min}\limits_{\bm{x}} = \|{\bm s} - {\bm \Phi}{\bm x}\|_2 + \lambda \|{\bm x}\|_p.

Note that, if :math:`{\bm s, \Phi, x} \in {\mathbb C}` , the problem changes to

.. math::
   {\mathop{\rm Re}\nolimits} ({\bm{s}}) + j{\rm Im}({\bm{s}}) = {\rm Re}({\bm \Phi}{\bm x}) + j{\mathop{\rm Im}\nolimits} ({\bm \Phi}{\bm x})

so we have:

.. math::
   \left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{s}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{s}})}
   \end{array}} \right] = \left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{\Phi }})}&{ - {\mathop{\rm Im}\nolimits} ({\bm{\Phi }})}\\
   {{\rm Im}({\bm{\Phi }})}&{{\mathop{\rm Re}\nolimits} ({\bm{\Phi }})}
   \end{array}} \right]\left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{x}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{x}})}
   \end{array}} \right]


.. hint::
   对于非稀疏场景, 无需先对场景进行稀疏表示, 再进行观测; 然而在重构信号时, 由于信号非稀疏, 需要假设其在某一字典下稀疏.


:guilabel:`ABC`

实验与分析
----------------------


仿真数据
~~~~~~~~~~~~~~

实验说明
^^^^^^^^^^^^^^

- 仿真场景大小: :math:`32 \times 32`
- 回波矩阵大小: :math:`32 \times 32`
- 稀疏表示字典: 无, ``DCT`` ,  ``DWT``
- 优化方法: ``Lasso`` , ``OMP``

仿真点目标场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/pointsAmpPhase.png
   :scale: 80 %
   :alt: 仿真点目标场景图, 仿真SAR原始数据幅度相位图
   :align: center

   仿真点目标场景图, 仿真SAR原始数据幅度相位图


仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/shipAmpPhase.png
   :scale: 80 %
   :alt: 仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下
   :align: center

   仿真船只场景图及仿真生成点SAR原始数据幅度与相位图如下

仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下:

.. figure:: ../../../_static/figs/Radar/SAR/pub/lotusAmpPhase.png
   :scale: 80 %
   :alt: 仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下
   :align: center

   仿真荷花场景图及仿真生成点SAR原始数据幅度与相位图如下



实验代码
^^^^^^^^^^^^^^



实验结果
^^^^^^^^^^^^^^

**1. OMP优化, 不采用字典进行稀疏表示, 和采用DCT字典进行稀疏表示的结果如下:**

点目标结果

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSOMP_DICT_RDA_points.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of points.
   :align: center

   Compressive Sensing based and RDA Imaging Results of points.


船只结果:

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSOMP_DICT_RDA_ship.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of ship.
   :align: center

   Compressive Sensing based and RDA Imaging Results of ship.

荷花结果:

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSOMP_DICT_RDA_lotus.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of lotus.
   :align: center

   Compressive Sensing based and RDA Imaging Results of lotus.



**2. Lasso优化, 不采用字典进行稀疏表示, 和采用DCT字典进行稀疏表示的结果如下:**

点目标结果

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSLASSO_DICT_RDA_points.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of points.
   :align: center

   Compressive Sensing based and RDA Imaging Results of points.


船只结果:

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSLASSO_DICT_RDA_ship.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of ship.
   :align: center

   Compressive Sensing based and RDA Imaging Results of ship.

荷花结果:

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/CS/CSLASSO_DICT_RDA_lotus.*
   :scale: 100 %
   :alt: Compressive Sensing based and RDA Imaging Results of lotus.
   :align: center

   Compressive Sensing based and RDA Imaging Results of lotus.



.. note::
   由实验结果可知:

   - 场景的稀疏性决定了重构的性能, 越稀疏重构越精确
   - 字典的选择很重要

真实数据
~~~~~~~~~~~~~~~


实验说明
^^^^^^^^^^^^^^

由于压缩感知方法占用内存空间大, 该数据为RADARSAT1一景数据中的一小块区域, 区域大小为 :math:`128\times 128` .




实验代码
^^^^^^^^^^^^^^



实验结果
^^^^^^^^^^^^^^



