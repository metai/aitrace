.. _glossary:

名词术语
========

.. glossary::
   :sorted:


   Sinc Interpolation
      Sinc 插值 ( `Sinc Interpolation <http://en.volupedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula>`_ ) 也叫 **Whittaker–Shannon interpolation** , **Shannon's interpolation** 或 **Whittaker's interpolation** .


   Support
      支撑 ( `Support <http://en.volupedia.org/wiki/Support_(mathematics)#Compact_support>`_ ), 在数学中, 实值函数 :math:`f`   的支撑是包含那些未映射到零的元素的域的子集. 如果 :math:`f` 的域是拓扑空间, 则 :math:`f` 的支撑被定义为包含所有未映射到零点的最小闭集. 这个概念在数学分析中应用非常广泛.


   Compact Support
      紧支撑 ( `Compact support <http://en.volupedia.org/wiki/Support_(mathematics)#Compact_support>`_ ), 在数学中, 如果函数 :math:`f` 的支撑集是拓扑空间 :math:`{\mathbb X}` 的紧集, 则称函数 :math:`f` 紧支撑于空间 :math:`{\mathbb X}` .


   Compact Set
      紧集


   Wavelet
      小波 ( `Wavelet <http://en.volupedia.org/wiki/Wavelet>`_ ) 顾名思义,  "小波" 就是小的波形. 所谓 "小" 是指它具有衰减性；而称之为 "波" 则是指它的波动性, 其振幅正负相间的震荡形式. 与Fourier变换相比, 小波变换是时间（空间）频率的局部化分析, 它通过伸缩平移运算对信号(函数)逐步进行多尺度细化, 最终达到高频处时间细分, 低频处频率细分, 能自动适应时频信号分析的要求, 从而可聚焦到信号的任意细节, 解决了Fourier变换的困难问题, 成为继Fourier变换以来在科学方法上的重大突破. 有人把小波变换称为 "数学显微镜" .

   Mother Wavelet
      母小波 ( `Mother Wavelet <http://en.volupedia.org/wiki/Wavelet#Mother_wavelet>`_ ) 也称小波母函数.

   Daughter Wavelet
      子小波 ( `Daughter Wavelet <http://en.volupedia.org/wiki/Wavelet#Daughter_wavelet>`_ ) 由小波母函数通过平移与尺度缩放得到.

   Time Frequency Analysis
      时频分析 ( `Time–frequency analysis <http://en.volupedia.org/wiki/Time%E2%80%93frequency_analysis>`_   ), 在信号处理中, 时频分析研究时间域与频域的时频表示, 通过时频变换得到信号在时间与频率二维平面中的分布.


   Short Time Fourier Transform
      短时傅里叶变换 ( `Short Time Fourier Transform <http://en.volupedia.org/wiki/Short-time_Fourier_transform>`_ , STFT ) 是和傅里叶变换相关的一种数学变换, 用以确定时变信号其局部区域正弦波的频率与相位.

   Wavelet Transform
      连续小波变换 ( `Wavelet transform <http://en.volupedia.org/wiki/Wavelet_transform>`_ , CWT ), 由于短时傅里叶变换窗口大小是固定的, 只适用于频率波动小的平稳信号, 不适用于频率波动大的非平稳信号. 而小波变换可以根据频率的高低自动调节窗口大小, 是一种自适应的时频分析方法, 可以进行多分辨率分析.

   Continuous Wavelet Transform
      连续小波变换 ( `Continuous wavelet transform <http://en.volupedia.org/wiki/Continuous_wavelet_transform>`_ , CWT ), 由于短时傅里叶变换窗口大小是固定的, 只适用于频率波动小的平稳信号, 不适用于频率波动大的非平稳信号. 而小波变换可以根据频率的高低自动调节窗口大小, 是一种自适应的时频分析方法, 可以进行多分辨率分析.

   Discrete Wavelet Transform
      连续小波变换 ( `Discrete wavelet transform <http://en.volupedia.org/wiki/Discrete_wavelet_transform>`_ , DWT ), 短时傅里叶变换, 但由于窗口大小是固定的, 只适用于频率波动小的平稳信号, 不适用于频率波动大的非平稳信号. 而小波变换可以根据频率的高低自动调节窗口大小, 是一种自适应的时频分析方法, 可以进行多分辨率分析.

   Spectral Estimation
      谱估计 ( `Spectral Density Estimation <http://en.volupedia.org/wiki/Spectral_density_estimation>`_   ), 分为经典谱估计 (非参数化谱估计), 现代谱估计 (参数化谱估计).

   Classical Spectral Estimation
      经典谱估计 (Classical Spectral Estimation), 又称非参数化谱估计.

   Modern Spectral Estimation
      现代谱估计 (Modern Spectral Estimation), 又称参数化谱估计.

   Nonparametric Spectral Estimation
      非参数化谱估计 (Nonparametric Spectral Estimation), 又称经典谱估计.

   Parametric Spectral Estimation
      参数化谱估计 (Parametric Spectral Estimation),  又称现代谱估计.

   Autoregressive Model
      自回归模型 ( `Autoregressive Model <http://en.volupedia.org/wiki/Autoregressive_model>`_   ), 是统计上一种处理时间序列的方法, 是用同一变量之前各期的表现情况, 来预测该变量本期的表现情况, 并假设它们为线性关系. 因为这是从回归分析中的线性回归发展而来, 只是不是用来预测其他变量, 而是用来预测自己, 所以叫做自回归. 自回归模型被广泛运用在经济学、信息学、自然现象的预测上.


   Multiple Signal Classification
      多重信号分类 ( `MUltiple SIgnal Classification <http://en.volupedia.org/wiki/MUSIC_(algorithm)>`_ , MUSIC), 是统计上一种处理时间序列的方法, 是用同一变量之前各期的表现情况, 来预测该变量本期的表现情况, 并假设它们为线性关系. 因为这是从回归分析中的线性回归发展而来, 只是不是用来预测其他变量, 而是用来预测自己, 所以叫做自回归. 自回归模型被广泛运用在经济学、信息学、自然现象的预测上.



