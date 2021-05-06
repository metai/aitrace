.. _Section-FourierTransformationClassicalSpectralEstimationDigitalSignalProcessing:

傅立叶变换
=====================

简介
-----------------



连续时间傅立叶变换及其逆变换
-------------------------

一维连续时间FT与IFT
~~~~~~~~~~~~~~~~~~~~

一维连续时间信号 :math:`x(t)` 的 **傅立叶变换** 可表示为

.. math::
   X(\omega) = \int_{-\infty}^{+\infty} x(t)e^{-j\omega t} {\rm d}t
   :label: equ-ContinuousFourierTransform1D

其中, :math:`\omega` 为角频率, 单位为 :math:`\rm rad/s`, :math:`X(\omega)` 为变换后的频域信号. 傅里叶变换为可逆变换, 即可以从频域信号 :math:`X(\omega)` 变回时域信号 :math:`x(t)`, **逆傅立叶变换** 可以表示为

.. math::
   x(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty}X(\omega)e^{+j\omega t} {\rm d}\omega
   :label: equ-InverseContinuousFourierTransform1D

对于周期为 :math:`T` 的信号, 式 :eq:`equ-ContinuousFourierTransform1D` 的积分区间可变为 :math:`[-T/2, T/2]`.


二维连续时间FT与IFT
~~~~~~~~~~~~~~~~~~~~





离散时间傅立叶变换及其逆变换
-------------------------


一维离散时间FT与IFT
~~~~~~~~~~~~~~~~~~~~

一维离散时间信号 :math:`x[n], n=0,1,\cdots, N-1` **傅立叶变换** 可表示为

.. math::
   X[k] = \sum_{n=0}^{N-1} x[n]e^{-j \frac{2\pi k}{N} n}
   :label: equ-DiscreteFourierTransform1D

其中, :math:`\frac{2\pi k}{N}, k=0, 1, \cdots, K-1` 为角频率, 单位为 :math:`\rm rad/s`, :math:`X[k]` 为变换后的频域信号. 傅里叶变换为可逆变换, 即可以从频域信号 :math:`X[k]` 变回时域信号 :math:`x[n]`, **逆傅立叶变换** 可以表示为

.. math::
   x[n] = \frac{1}{N}\sum_{k=0}^{K-1} X[k] e^{j \frac{2\pi k}{N} n}
   :label: equ-InverseDiscreteFourierTransform1D


.. hint::
   :math:`K` 为傅里叶变换点数, 控制了频率分辨率.

二维离散时间FT与IFT
~~~~~~~~~~~~~~~~~~~~

`二维离散傅里叶变换与逆变换的原理与手动实现 <https://www.jianshu.com/p/98f493de01db>`_




快速傅立叶变换
-------------------------



实验分析
----------------



仿真数据实验
~~~~~~~~~~~~

实验代码
^^^^^^^^^^^^^^

MATLAB代码

`test_FFT.m <../../../../_static/src/matlab/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/test_FFT.m>`_  .

.. literalinclude:: ../../../../../src/matlab/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/test_FFT.m
   :language: matlab
   :encoding: latin-1
   :emphasize-lines: 43
   :linenos:
   :caption: test_FFT.m
   :name: bind-id


PYTHON代码

`test_FFT.py <../../../../_static/src/python/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/test_FFT.py>`_  .

.. literalinclude:: ../../../../../src/python/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/test_FFT.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43
   :linenos:
   :caption: test_FFT.py
   :name: bind-id

实验结果
^^^^^^^^^^^^^


.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/testFFT_matlab.png
   :scale: 80 %
   :alt: FFT test matlab
   :align: center

   FFT matlab

   FFT matlab


.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/testFFT_python.png
   :scale: 80 %
   :alt: FFT test python
   :align: center

   FFT python

   FFT python


真实数据实验
~~~~~~~~~~~~

