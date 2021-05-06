.. _Section-FourierTransformationAndConvolutionClassicalSpectralEstimationDigitalSignalProcessing:

傅立叶变换与卷积
=====================

概念与内涵
-----------------







FFT实现卷积
--------------------


通过补零将卷积核与数据补成相同大小, 然后对各自做FFT,



.. note:: FFT实现二维图像卷积(卷积步长为1)

   输入: 数据矩阵 :math:`{\bm I} \in {\mathbb R}^{I_h\times I_W}`, 卷积核 :math:`{\bm K} \in {\mathbb R}^{K_h\times K_w}`
   输出: 卷积结果 :math:`{\bm O} = {\bm I} * {\bm K}`, 其中, :math:`{\bm O} \in {\mathbb R}^{O_h\times O_w}`, :math:`O_h = I_h+K_h/2-1`, :math:`O_w = I_w+K_w/2-1`

   Step 1: 对数据矩阵 :math:`{\bm I}` 与卷积核 :math:`{\bm K}` 周边进行补零, 补成 :math:`{O_h \times O_W}` 大小的矩阵

   Step 2: 对数据矩阵 :math:`{\bm I}` 做二维傅里叶变换, 得到其频域二维形式 :math:`I = {\rm FFT}({\bm I})`

   Step 3: 对卷积核矩阵 :math:`{\bm K}` 做二维傅里叶变换, 得到其频域二维形式 :math:`K = {\rm FFT}(\bm K)`

   Step 4: 通过频域相乘(对应元素相乘)得到卷积后的频域结果 :math:`O = G \odot H`

   Step 5: 通过逆傅里叶变换得到卷积结果 :math:`{\bm O} = {\rm IFFT}(O)`

   Step 6: :math:`{\bm O}`


设有数据矩阵 :math:`{\bm I} \in {\mathbb R}^{I_h\times I_W}`, 卷积核 :math:`{\bm K} \in {\mathbb R}^{K_h\times K_w}`, 利用FFT实现图像二维卷积的步骤为


1. 将数据矩阵 :math:`{\bm I} \in {\mathbb R}^{H\times W}`,





实验与分析
--------------------



FFT实现二维矩阵卷积
~~~~~~~~~~~~~~~~~~~~


MATLAB代码:

.. literalinclude:: ../../../../_static/src/matlab/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/demo_Array_FFT_Conv2d.m
   :language: python
   :encoding: latin-1
   :emphasize-lines: 18-21,24,27
   :linenos:
   :caption: demo_Array_FFT_Conv2d.m
   :name: bind-id



::

    >> demo_Array_FFT_Conv2d
    ---By FFT
       -8.0000   -8.0000  -20.0000  -20.0000  -20.0000  -20.0000
             0         0  -12.0000  -12.0000  -12.0000  -12.0000
       24.0000   24.0000   12.0000   12.0000   12.0000   12.0000
       16.0000   16.0000    4.0000    4.0000    4.0000    4.0000
        8.0000    8.0000   -4.0000   -4.0000   -4.0000   -4.0000
        8.0000    8.0000   -4.0000   -4.0000   -4.0000   -4.0000

    ---By Conv(valid)
        12    12    12    12
         4     4     4     4
        -4    -4    -4    -4
        -4    -4    -4    -4

    ---By Conv(same)
         3     9    11    13    15    24
         0    12    12    12    12    30
       -12     4     4     4     4    30
       -20    -4    -4    -4    -4    26
       -20    -4    -4    -4    -4    26
       -29   -23   -25   -27   -29    -1




FFT实现二维图像卷积
~~~~~~~~~~~~~~~~~~~~




MATLAB代码:

.. literalinclude:: ../../../../_static/src/matlab/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/demo_Image_FFT_Conv2d.m
   :language: python
   :encoding: latin-1
   :emphasize-lines: 20-23,26,29
   :linenos:
   :caption: demo_Image_FFT_Conv2d.m
   :name: bind-id



.. figure:: ../../../../_static/figs/SignalProcessing/Digital/SpectralEstimation/Classical/FourierTransformation/FFT_CONV2d_IMAGE.*
   :scale: 80 %
   :alt: FFT实现图像二维卷积与直接卷积结果对比
   :align: center

   FFT实现图像二维卷积与直接卷积结果对比

   FFT实现图像二维卷积与直接卷积结果对比.