.. _Section-ConvolutionLinearOperatorFunctionalAnalysisBasicMath:

卷积算子
=====================

普通卷积
-----------------

在数学中, **卷积** ( :term:`Convolution` ) 是一种由两个函数(:math:`f, g`)产生第三个函数(:math:`h`)的操作, 即将两个函数(:math:`f, g`)中的一个进行翻转和平移不同量后与另一个分别相乘后再累加. 与相关分析类似, 不同的是在相关分析中, 无需进行翻转操作.


.. warning::
   卷积神经网络中的卷积(convolution)运算实际上是互相关(cross-correlation)运算, 详见 :ref:`Section-ConvolutionUnitModuleOfNNNeuralNetworkArtificialIntelligence` 小节.


一维卷积
~~~~~~~~~~~~~~

设有单变量连续函数 :math:`f(t)`, :math:`g(t)`, 两者之间的卷积可以表示为

.. math::
   \begin{aligned}
   (f*g)(t) &= \int_{-\infty}^{+\infty}f(\tau)g(t-\tau){\rm d}\tau \\
            &= \int_{-\infty}^{+\infty}f(t-\tau)g(\tau){\rm d}\tau
   \end{aligned}
   :label: equ-1DConvContinues


单变量离散序列 :math:`f[n]`, :math:`g[n]`, 两者之间的卷积可以表示为

.. math::
   \begin{aligned}
   (f*g)[n] &= \sum_{m=-\infty}^{+\infty}f[m]g[n-m] \\
            &= \sum_{m=-\infty}^{+\infty}f[n-m]g[m]
   \end{aligned}
   :label: equ-1DConvDiscrete


一维卷积具有如下性质 (以连续卷积为例)


- 分配律: :math:`f_1(t)*\left(f_2(t)+f_3(t)\right) = f_1(t)*f_2(t) + f_1(t) * f_3(t)` :math:`\Leftrightarrow` :math:`h(t) = h_1(t) + h_2(t)`
- 结合律: :math:`\left(f_1(t)*f_2(t)\right)*f_3(t) = f_1(t)*\left(f_2(t)*f_3(t)\right)` :math:`\Leftrightarrow` :math:`h(t) = h_1(t) * h_2(t)`
- 交换律: :math:`f_1(t)*f_2(t) = f_2(t)*f_1(t)`
- 时域卷积对应频域相乘: :math:`f_1(t)*f_2(t) \Leftrightarrow F_1(\omega)F_2(\omega)`
- 频域卷积对应时域相乘: :math:`F_1(\omega)*F_2(\omega) \Leftrightarrow 2\pi f_1(t)f_2(t)`
- 卷积的微分: :math:`\frac{{\rm d}}{{\rm d} t}\left[f_{1}(t) * f_{2}(t)\right]=f_{1}(t) * \frac{{\rm d} f_{2}(t)}{{\rm d} t}+f_{2}(t) * \frac{{\rm d} f_{1}(t)}{{\rm d} t}`
- 卷积的积分: :math:`\int_{-\infty}^{t} f_{1}(\tau) * f_{2}(\tau) {\rm d} \tau=f_{1}(t) * \int_{-\infty}^{t} f_{2}(\tau) {\rm d} \tau=f_{2}(t) * \int_{-\infty}^{t} f_{1}(\tau) {\rm d} \tau`



任意函数与冲击响应函数卷积的性质 (以连续卷积为例)

- 任意函数与单位冲激信号卷积结果为自身: :math:`f(t)*\delta(t) = \int_{-\infty}^{+\infty}f(\tau)\delta(t-\tau){\rm d}\tau=f(t)`
- 任意函数与时延为 :math:`t_d` 的单位冲激信号卷积结果为自身时延 :math:`t_d` : :math:`f(t)*\delta(t-t_d) = \int_{-\infty}^{+\infty}f(\tau)\delta(t-t_d-\tau){\rm d}\tau=f(t-t_d)`
- 任意函数与单位冲激信号导数的卷积结果为自身的导数: :math:`f(t)*\delta^{(k)}(t)=f^{(k)}(t)`
- 任意函数与时延为 :math:`t_d` 单位冲激信号导数的卷积结果为自身时延 :math:`t_d` 导数: :math:`f(t)*\delta^{(k)}(t-t_d)=f^{(k)}(t-t_d)`





二维卷积
~~~~~~~~~~~~~~~

对于双变量连续函数 :math:`f(x, y), g(x, y)`, 它们之间的二维卷积定义为

.. math::
   \begin{aligned}
   (f*g)(x, y) &=\int_{-\infty}^{+\infty}f(u,v)g(x-u,y-v){\rm d}u{\rm d}v \\
               &= \int_{-\infty}^{+\infty}f(x-u,y-v)g(u,v){\rm d}u{\rm d}v
   \end{aligned}
   :label: equ-2DConvContinues


回旋卷积
--------------------


**回旋卷积** ( :term:`Circular Convolution` ) 也称 **循环卷积** , 即当 :math:`g` 为周期函数时的卷积, 卷积结果也是周期的.


连续形式
~~~~~~~~~~~~~~~~~~

设有周期为 :math:`T` 的函数 :math:`g` , 定义如下连续形式循环卷积

.. math::
    f(t)*g_T(t) = \int_{t_0}^{t_0+T}\left(\sum_{k=-\infty}^{+\infty}f(\tau+kT)\right)g_T(t-\tau){\rm d}\tau


离散形式
~~~~~~~~~~~~~~~~~~

设有周期为 :math:`T` 的函数 :math:`g` , 定义如下离散形式循环卷积

.. math::
    f[n]*g_N[n] = \sum_{m=0}^{N-1}\left(\sum_{k=-\infty}^{+\infty}f[m+kN]\right)g_N[n-m]



实验分析
-----------------------

二维卷积
~~~~~~~~~~~~~~~~~~~~



