.. _Section-STFTClassicalTimeFrequencyAnalysisDigitalSignalProcessing:

短时傅立叶变换
=====================


短时傅立叶变换
--------------------

短时傅立叶变换 ( :term:`Short Time Fourier Transform` , STFT) 是和傅里叶变换相关的一种数学变换, 用以确定时变信号其局部区域正弦波的频率与相位. 通过将长时间信号分成等长的短的片段,  计算每个片段的傅里叶变换, 将这些片段组成一个频率-时间矩阵得到. 与傅里叶变换类似, 分为连续时间 (Continuous-time) STFT 和离散时间 (Discrete-time) STFT.

连续时间STFT
~~~~~~~~~~~~~

设有连续时间信号 :math:`x(t)` , 窗函数 :math:`w(t)` , 在信号上滑动窗函数, 计算信号与窗函数乘积的傅里叶变换, 得到连续时间信号的二维时频STFT表示, 即

.. math::
    {\rm STFT}\{x(t)\}(\tau, \omega) = X(\tau, \omega) = \int_{-\infty}^{+\infty}x(t)w(t-\tau)e^{-j\omega t}{\rm d}t


其中, :math:`t, \tau` , :math:`\omega=2\pi f` 均为连续的.

.. hint::
   信号 :math:`x(t)` 的傅里叶变换表示为

   .. math::
      F(\omega) = \int_{-\infty}^{+\infty} x(t)e^{-j\omega t} {\rm d}t

   逆傅里叶变换表示为

   .. math::
      x(t) = \frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{+j\omega t} {\rm d}\omega

离散时间STFT
~~~~~~~~~~~~~

设有离散时间信号 :math:`x[n]` , 窗函数 :math:`w[n]` , 在信号上滑动窗函数, 计算信号与窗函数乘积的傅里叶变换, 得到离散时间信号的二维时频STFT表示, 即


.. math::
   {\rm STFT}\{x[n]\}(m, \omega) = X(m, \omega) = \sum_{n=-\infty}^{+\infty} x[n]w[n-m]e^{-j\omega n}

其中, :math:`n, m` 是离散的, :math:`\omega=2\pi f` 为连续的. 然而, 通常情况下傅里叶变换采用快速傅里叶变换(FFT)计算, 此时 :math:`\omega` 也是离散的.


.. hint::
   通常情况下, 窗取为重叠的 (overlap) ,


频谱表示
-----------------

信号的功率谱密度的频谱表示为STFT结果的平方

.. math::
   {\rm{spectrogram}}\{x(t)\}(\tau, \omega) = |X(\tau, \omega)|^2


逆短时傅立叶变换
------------------

STFT是可逆的, 即原始信号可以从变换后的数据中恢复出来.


连续时间逆STFT
~~~~~~~~~~~~~

设有连续时间信号 :math:`x(t)` 的STFT表示 :math:`X(\tau, \omega)` , 则

.. math::
   x(t) = \frac{1}{2\pi}{\int_{-\infty}^{+\infty}}{\int_{-\infty}^{+\infty}} X(\tau, \omega)e^{+j\omega t} {\rm d}\tau {\rm d}\omega

或

.. math::
   x(t) = {\int_{-\infty}^{+\infty}}\left[\frac{1}{2\pi}{\int_{-\infty}^{+\infty}} X(\tau, \omega)e^{+j\omega t} {\rm d}\omega\right]{\rm d}\tau


离散时间逆STFT
~~~~~~~~~~~~~




实现步骤
-----------------

- 离散时间STFT

  - 使用窗函数在信号上滑动, 将长时间信号分成等长的短的片段
  - 计算每个片段与窗函数乘积的傅里叶变换
  - 计算每个片段变换后的幅度或功率密度谱
  - 将这些片段组成一个频率-时间矩阵


实例分析
------------------

实验1: 仿真信号
~~~~~~~~~~~~~~~


实验内容
^^^^^^^^^^

生成四个子信号, 四种频率:

.. math::
    x_1 = {\rm cos}(2πf_1 t), (0\Delta T \leq t < 1\Delta T) \\
    x_2 = {\rm cos}(2πf_2 t), (1\Delta T \leq t < 2\Delta T) \\
    x_3 = {\rm cos}(2πf_3 t), (2\Delta T \leq t < 3\Delta T) \\
    x_4 = {\rm cos}(2πf_4 t), (3\Delta T \leq t < 4\Delta T) \\


合成一个信号, 含上述四种频率:

.. math::
    x = x_1 + x_2 + x_3 + x_4

做以下实验

#. 不同窗
#. Gauss窗, 不同std
#. Gauss窗, 不同窗大小
#. Gauss窗, 不同重叠大小
#. Gauss窗, 不同FFT大小


实验代码
^^^^^^^^^^^


核心函数: ``scipy.signal.spectral.spectrogram``

#. 不同窗: `demo_stft_windows.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_windows.py>`_
#. 不同窗, 不同窗大小: `demo_stft_gauss_windowsize.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_gauss_windowsize.py>`_
#. Gauss窗, 不同std: `demo_stft_gauss_std.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_gauss_std.py>`_
#. Gauss窗, 不同窗大小: `demo_stft_gauss_windowsize.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_gauss_windowsize.py>`_
#. Gauss窗, 不同重叠大小: `demo_stft_gauss_noverlap.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_gauss_noverlap.py>`_
#. Gauss窗, 不同FFT大小: `demo_stft_gauss_nfft.py <../../../_static/src/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/demo_stft_gauss_nfft.py>`_



实验结果
^^^^^^^^^^^

实验中, 设四种信号频率为: :math:`f_1=10Hz, f_2=25Hz, f_3=50Hz, f_4=100Hz` , :math:`\Delta T = 5s` , 采样率为 :math:`400Hz` , 共 :math:`8000` 个样本点, 生成的合成信号如下图



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/signal.*
   :scale: 80 %
   :alt: Synthetic signal
   :align: center

   Synthetic signal

   合成的信号, 包含四种频率成分.

1. 不同窗

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_DIFF_WINDOWS_nfft2048_noverlap1_ws500ms.*
   :scale: 80 %
   :alt: STFT在不同窗下的结果
   :align: center

   STFT在不同窗下的结果

   对合成信号施加六种不同的窗 ( tukey, kaiser, gauss, hamming, cosine, blackman), 窗大小取 :math:`500ms` , FFT点数取 :math:`2048`, 重叠点数取 :math:`1` , 然后进行STFT分析.

2. 不同窗, 不同窗大小

对合成信号施加不同窗, 并改变窗大小, FFT点数取 :math:`2048` , 重叠点数取 :math:`1` , 其它参数见图. 由图可见窗大小影响较大, 窗过小, 频率难分辨.

窗大小为 :math:`10ms` 时的结果

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_DIFF_WINDOWS_nfft2048_noverlap1_ws10ms.*
   :scale: 80 %
   :alt: STFT在不同窗大小下的结果
   :align: center

   STFT在窗大小为 :math:`10ms` 时的结果

窗大小为 :math:`100ms` 时的结果

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_DIFF_WINDOWS_nfft2048_noverlap1_ws100ms.*
   :scale: 80 %
   :alt: STFT在不同窗大小下的结果
   :align: center

   STFT在窗大小为 :math:`100ms` 时的结果

窗大小为 :math:`1000ms` 时的结果

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_DIFF_WINDOWS_nfft2048_noverlap1_ws1000ms.*
   :scale: 80 %
   :alt: STFT在不同窗大小下的结果
   :align: center

   STFT在窗大小为 :math:`1000ms` 时的结果



3. gauss窗, 不同 std

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_GAUSS_STD_nfft2048_noverlap1.*
   :scale: 80 %
   :alt: STFT在gauss窗不同std下的结果
   :align: center

   STFT在gauss窗, 不同std下的结果

   对合成信号施加gauss窗, 窗大小取 :math:`1000ms` , FFT点数取 :math:`2048`, 重叠点数取 :math:`1` , 使用不同标准差( :math:`0.5, 1.0,10, 30, 50, 100`), 然后进行STFT分析.

4. gauss窗, 不同窗大小

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_GAUSS_WINDOWSIZE_nfft2048_noverlap1.*
   :scale: 80 %
   :alt: STFT在gauss窗, 不同窗大小下的结果
   :align: center

   STFT在gauss窗, 不同窗大小下的结果

   对合成信号施加gauss窗, 标准差取 :math:`30` , FFT点数取 :math:`2048` , 重叠点数取 :math:`1` , 使用不同窗大小( :math:`25ms, 100ms, 500ms, 1000ms, 2000ms, 3000ms`), 然后进行STFT分析.

对于Gauss窗, 窗过小频率难区分, 窗过大时间难区分.


5. 不同重叠点数

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_GAUSS_NOVERLAP_std30_nfft2048.*
   :scale: 80 %
   :alt: STFT在不同重叠点数下的结果
   :align: center

   STFT在不同重叠点数下的结果

   对合成信号施加gauss窗, 标准差取 :math:`30` , 窗大小取 :math:`1000ms` , FFT点数取 :math:`2048` , 使用不同重叠点数, 然后进行STFT分析.

6. 不同FFT点数

.. figure:: ../../../../_static/figs/SignalProcessing/Digital/TimeFrequencyAnalysis/Classical/STFT/STFT_GAUSS_NFFT_std30_noverlap1.*
   :scale: 80 %
   :alt: STFT在不同FFT点数下的结果
   :align: center

   STFT在不同FFT点数下的结果

   对合成信号施加gauss窗, 标准差取 :math:`30` , 窗大小取 :math:`1000ms` , 重叠点数取 :math:`1` , 使用不同FFT点数, 然后进行STFT分析.


实验分析
^^^^^^^^^^^

- 对于所有窗函数, 窗大小影响较大
- 重叠点数影响较小, 但不能过大
- FFT点数影响较小, 但要大于分段长度
- 窗函数及其参数影响较大, 应仔细选取
- 对于Gauss窗, 窗过小频率难区分, 窗过大时间难区分
- 对于Gauss窗, 窗大小及标准差影响较大;
- 对于tukey, 其参数影响较小;
- 对于kaiser, 其参数影响较大.



实验2: 真实信号
~~~~~~~~~~~~~~~

语音信号


