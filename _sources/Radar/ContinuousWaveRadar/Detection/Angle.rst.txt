.. _Section-AngleDetectionContinuesWaveRadarRadar:


角度测量
=============

- 相位法
- 振幅法

简介
-----------

角度测量是探测 “目标——天线中心线的连线” 与法线的夹角，多用于目标定位。设计有一根发射天线 TX，两根接收天线 RX1/RX2，并有 I1、I2、Q1、Q2 四个工作通道，采用比相法来实现此功能。

参考文档：[雷达原理角度测量](https://wenku.baidu.com/view/d44192cee45c3b3567ec8bb7.html)

相位差测角
-----------

相位差法测角原理概览
~~~~~~~~~~~~~~~~~~~~~~~

相位差法测角原理可总结如下图所示：

.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angleall.png
    :scale: 80%
    :align: center

    相位差法测角原理总览



相位差法测角原理详解
~~~~~~~~~~~~~~~~~~~~~~~


相位差测角原理示意图如下图所示：

.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angle_theory.png
    :scale: 80%
    :align: center

    相位差测角原理示意图


相位差法测角算法如下图所示：

.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angle_algo.png
    :scale: 80%
    :align: center

    相位差法测角算法



相位差法测角范围
~~~~~~~~~~~~~~~~~~~~~~~


相位差法测角利用多个天线所接收到的回波信号间的相位差测角，测角范围与波长及天线间距相关，计算方法如下图所示

.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angle_range.png
    :scale: 80%
    :align: center

    相位差法测角范围分析



相位差法测角误差及多值性
~~~~~~~~~~~~~~~~~~~~~~~

相位差法测角误差分析如下，可见该方法存在测角模糊问题。


.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angle_error.png
    :scale: 80%
    :align: center

    相位差法测角误差分析

一种解决方法是采用三天线法测角，原理如下图

.. Figure:: ../../../_static/figs/Radar/ContinuousWaveRadar/Detection/Angle/angle_triantanna.png
    :scale: 80%
    :align: center

    三天线法测角


