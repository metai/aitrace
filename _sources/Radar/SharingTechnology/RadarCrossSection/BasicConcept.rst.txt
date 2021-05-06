.. _Section-BasicConceptRadarCrossSectionSharingTechnologyRadar:

基础概念
=====================


什么是雷达散射截面积
--------------------


雷达散射截面积 (:term:`Radar Cross Section`, RCS) 用于度量目标在雷达接收方向上反射的信号能量密度. 目标的RCS通常取决于目标的形状与材质材质, 雷达的工作参数.







雷达散射系数的分类
--------------------

常见的有三种雷达散射系数, 第一种是雷达亮度(反射率)系数, 常称为 Beta Naught, 用 :math:`\beta` 表示, 其在斜距方向上的单位面积的反射率是无量纲的. 第二种是标准后向散射系数 Sigma naught, 常指目标反射回来的波的强度, 常记为 :math:`\sigma`, 单位为 :math:`dB`. 第三种是归一化后向散射系数 Gamma naught, 即入射角归一化后向散射系数, 常记为 :math:`\gamma`.



`实现参考 ASF MapReady calibration <https://github.com/asfadmin/ASF_MapReady/blob/devel/src/libasf_ardop/calibration.c>`_



