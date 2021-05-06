.. _Section-OverviewRadarEmitterSignalEmitterSignalAnalysis:


概述
====================

有关雷达的概念参见 :ref:`volume-SignalProcessingOfRadar` 之 :ref:`volume-IntroductionSignalProcessingOfRadar` 小节.


雷达辐射源信号描述方式
---------------------

雷达辐射源描述方式也称辐射源描述字(:term:`Emitter Discription Word`, EDW)或脉冲描述字(:term:`Pulse Discription Word`, PDW)指雷达辐射源脉冲参数构成的数字化描述字, 常见的类型有

- 脉冲重复间隔 (Pulse Repetition Interval, PRI)
- 脉冲重复频率 (Pulse Repetition Frequency, PRF)
- 脉冲到达时间 (Time Of Arrival, TOA)
- 脉冲到达方向 (Direction Of Arrival, DOA)
- 脉冲宽度 (Pulse Width, PW)
- 脉冲幅度 (Pulse Amplitude, PA)
- 信号载频 (Radio Frequency, RF): 载频一般用 carrier frequency 表示, 但文献里常用RF表示


参见文献 :cite:`GS2017FZ` p6.



脉冲重复间隔
~~~~~~~~~~~~~~~~~~~~~

常见的脉冲重复间隔形式有: 1) 固定PRI; 2) 参差PRI; 3) 抖动PRI 4) 参差抖动PRI.

.. _fig-CommonPRI:

.. figure:: ../../../_static/figs/Radar/EmitterSignalAnalysis/RadarEmitterSignal/CommonPRI.png
   :alt:
   :align: center

   常见脉冲重复间隔形式(引自 :cite:`GS2017FZ` )


