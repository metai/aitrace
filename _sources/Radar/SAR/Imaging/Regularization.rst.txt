.. _Section-RegularizationImagingSARRadar:

正则化成像方法
=====================

正则化成像
---------------

SAR imaging process can be formulated as

.. math::
   {\bm s} = {\bm A}{\bm g},

where, :math:`{\bm s}` is the :math:`MN\times 1` recieved SAR raw data vector in phase history domain,
:math:`\bm g` is the :math:`HW \times 1` reflection vector of scene, and :math:`\bm A` represents the
the mapping from scene to SAR raw data.

Given :math:`\bm s, \bm A` , regularization methods try to reconstruct :math:`\bm g` by minmizing

.. math::
   \mathop {\rm min}\limits_{\bm{g}} {\left\| {{\bm{Ag}} - {\bm{s}}} \right\|_2} + \lambda |{\bm{g}}{|_p},

where, :math:`\lambda` is the balance factor, and :math:`|\cdot|_p` is the :math:`\ell_p` norm.

Note that, if :math:`{\bm s, A, g} \in {\mathbb C}` , the problem changes to

.. math::
   {\mathop{\rm Re}\nolimits} ({\bm{s}}) + j{\rm Im}({\bm{s}}) = {\rm Re}({\bm{Ag}}) + j{\mathop{\rm Im}\nolimits} ({\bm{Ag}})

so we have:

.. math::
   \left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{s}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{s}})}
   \end{array}} \right] = \left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{A}})}&{ - {\mathop{\rm Im}\nolimits} ({\bm{A}})}\\
   {{\rm Im}({\bm{A}})}&{{\mathop{\rm Re}\nolimits} ({\bm{A}})}
   \end{array}} \right]\left[ {\begin{array}{ccc}
   {{\mathop{\rm Re}\nolimits} ({\bm{g}})}\\
   {{\mathop{\rm Im}\nolimits} ({\bm{g}})}
   \end{array}} \right]



实验与分析
---------------------

实验说明
~~~~~~~~~~~~


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
~~~~~~~~~~~~~

`iprs2.0 <https://github.com/antsfamily/iprs2.0>`_  ``demo_regular_sar.py``



实验结果
~~~~~~~~~~~~~

点目标结果

.. figure:: ../../../_static/figs/Radar/SAR/Imaging/Regularization/Regularizationl1l2_RDA_Points.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/Regularization/Regularizationl1l2_RDA_Lotus.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


.. figure:: ../../../_static/figs/Radar/SAR/Imaging/Regularization/Regularizationl1l2_RDA_Ship.png
   :scale: 100 %
   :alt: Imaging result of :math:`\ell_1, \ell_2` regularization and RDA.
   :align: center

   Imaging result of :math:`\ell_1, \ell_2` regularization and RDA. :math:`\lambda=0.001` , max iter 1000


- 运行时间:

- 重构误差: