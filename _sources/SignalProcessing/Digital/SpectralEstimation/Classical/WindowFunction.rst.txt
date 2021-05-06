.. _Section-WindowFunctionClassicalSpectralEstimationDigitalSignalProcessing:

窗函数及其性质
=====================

概念
-----------


类型
----------

hamming
~~~~~~~


cosine
~~~~~~~


blackman
~~~~~~~~~



gaussian
~~~~~~~


tukey
~~~~~~~


kaiser
~~~~~~~







实例
----------

窗函数比较
~~~~~~~~~

实验内容
^^^^^^^^

产生 :math:`f=100Hz` 的余弦信号 :math:`x(t)` , 采样率为 :math:`F_s = 1000Hz` , 采样时间 :math:`T_s = 0.5s` , 对信号 :math:`x(t)` 施加六种窗函数, 窗函数持续时间 :math:`T_w = T_s = 0.5s` , 并对加窗前后的数据进行快速傅里叶变换.


- ``hamming``
- ``cosine``
- ``blackman``
- ``gaussian`` , :math:`{\rm{std}} = 100`
- ``tukey`` , :math:`α= 10`
- ``kaiser`` , :math:`β= 10`

实验代码
^^^^^^^^

代码文件 `demo_windows_effect.py <../../../../_static/src/python/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/demo_windows_effect.py>`_


.. literalinclude:: ../../../../_static/src/python/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/demo_windows_effect.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 39
   :linenos:
   :caption: demo_windows_effect.py
   :name: bind-id



实验结果
^^^^^^^^


.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/hamming.png
   :scale: 80 %
   :alt: hamming function
   :align: center

   effect of hamming window function



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/cosine.png
   :scale: 80 %
   :alt: cosine function
   :align: center

   effect of cosine window function



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/blackman.png
   :scale: 80 %
   :alt: blackman function
   :align: center

   effect of blackman window function



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/gauss100.png
   :scale: 80 %
   :alt: gauss100 function
   :align: center

   effect of gauss window function, with :math:`{\rm{std}} = 100`



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/kaiser10.png
   :scale: 80 %
   :alt: kaiser10 function
   :align: center

   effect of kaiser window function, with :math:`{\beta} = 10`



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/WindowFunction/tukey10.png
   :scale: 80 %
   :alt: tukey10 function
   :align: center

   effect of tukey window function, with :math:`{\alpha} = 10`









