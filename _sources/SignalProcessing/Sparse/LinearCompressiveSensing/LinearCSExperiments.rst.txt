.. _Section-LinearCSExperimentsLinearCompressiveSensingSparseSignalProcessing:

线性压缩感知实践
=====================

.. _SubsubSection_CSOMPSparseSignal:

稀疏信号实验
-----------------

一维仿真信号
~~~~~~~~~~~~~~~


- 信号(时域): :math:`{\bm x}_o = {\rm sin}(2 \pi  f_1 t) + {\rm sin}(2 \pi  f_2 t) + {\rm sin}(2 \pi  f_3 t)`
- 信号(频域): :math:`{\bm x} = {\rm abs}({\rm DFT}({\bm x}_o))`
- 观测矩阵: :math:`{\bm A}` 高斯矩阵和过完备DCT矩阵

.. hint::
   过完备DCT字典的构造参见 :ref:`SubSection_ODCTDICT` 小节.

设置时域信号 :math:`{\bm x}_o` 中的三个频率分别为 :math:`f_1=100Hz, f_2=200Hz, f_3=700Hz`; 设置采样率 :math:`F_s = 2000Hz`, 采样时间 :math:`T_s = 1s`; 则时域信号长度为 :math:`N_s = F_sT_s = 2000`. 信号 :math:`{\bm x}_o` 经离散FFT变换后, 并取模后得到频域信号 :math:`{\bm x}`, 将该信号作为欠采样的信号进行压缩采样.


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/sin3Signal.*
   :scale: 100 %
   :alt: Signal in Time and Frequency domains.
   :align: center

   Signal in Time (left, :math:`{\bm x}_o` ) and Frequency (right, :math:`{\bm x}`) domains.


记压缩比为 :math:`{\rm CR}`, 频域信号长度 :math:`N = N_s`, 则观测向量长度 :math:`M = N/CR`. 易知频域信号 :math:`{\bm x}` 的稀疏度为 :math:`k=6` (包含负频), 实验中分别设置不同的稀疏度 :math:`k_1 = 2, k_2 = 4, k_3 = 6, k_4 = 100` 进行信号重构.


实现代码, 参见文件 `demo_omp_sin3.py <https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs_omp_sparse_sin3.py>`_  .

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs_omp_sparse_sin3.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_cs_omp_sparse_sin3.py
   :name: bind-id


压缩比 :math:`{\rm CR} = 4` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(x, x1) with k = 2:  2020.810604016191
   ---MSE(x, x2) with k = 4:  1051.920200728807
   ---MSE(x, x3) with k = 6:  392.8334107460182
   ---MSE(x, x4) with k = 100:  49.64637577207484


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/sin3CR4alpha0DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(x, x1) with k = 2:  2049.017843656981
   ---MSE(x, x2) with k = 4:  1091.209561325295
   ---MSE(x, x3) with k = 6:  411.9556346140723
   ---MSE(x, x4) with k = 100:  316.7049674291499


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/sin3CR16alpha0DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.


压缩比 :math:`{\rm CR} = 4` 时, DCT过完备观测矩阵, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(x, x1) with k = 2:  2965.911207728454
   ---MSE(x, x2) with k = 4:  2055.5346968994822
   ---MSE(x, x3) with k = 6:  1082.970762562038
   ---MSE(x, x4) with k = 100:  1460.2482895078417


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/sin3CR4alpha0DictDCTRecovery.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, DCT过完备观测矩阵, 设置不同稀疏度下的信号重构均方误差结果如下:

::

   ---MSE(x, x1) with k = 2:  4805.715254609675
   ---MSE(x, x2) with k = 4:  4182.01590082246
   ---MSE(x, x3) with k = 6:  3227.931982399867
   ---MSE(x, x4) with k = 100:  3760.2420462992363


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/sin3CR16alpha0DictDCTRecovery.*
   :scale: 100 %
   :alt: Recovered signal in frequency domain with different sparse degree :math:`k`.
   :align: center

   Recovered signal in frequency domain with different sparse degree :math:`k`.


二维图像信号
~~~~~~~~~~~~~~~


实验设置
^^^^^^^^^

实验中使用稀疏图像信号作为实验对象, 并对图像的每一列采用OMP进行恢复.

- 图像信号: :math:`{\bm X}` 为稀疏图像
- 观测矩阵: :math:`{\bm A}` 为高斯矩阵和过完备DCT矩阵

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/tomographyData.*
   :scale: 100 %
   :alt: Tomography image.
   :align: center

   Tomography image

实验代码
^^^^^^^^^

实现代码, 参见文件 `demo_omp_sin3.py <https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_omp_img.py>`_  .

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_omp_img.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_omp_img.py
   :name: bind-id



实验结果
^^^^^^^^^

压缩比 :math:`{\rm CR} = 4` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  15.580596793850813 1798.9565809738183 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  16.51005632425414 1452.36150189551 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  16.236071194072142 1546.9391881886033 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  15.509964880400881 1828.4533008529795 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  14.650356290567599 2228.6646872408483 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  13.870332301892105 2667.148094123919 255 uint8

   [Finished in 1475.4s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/tomographyCR4alpha1e-6DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered tomography image with different sparse degree :math:`k`.
   :align: center

   Recovered tomography image with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  12.971158037789456 3280.6851824428386 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  12.936695435825893 3306.8219923587253 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  14.334155129944055 2396.9824147020495 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  14.869213943506328 2119.136669233503 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  14.284916845043584 2424.312922047151 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  13.839801158638902 2685.9643555265966 255 uint8

   [Finished in 1470.3s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/tomographyCR16alpha1e-6DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered tomography image with different sparse degree :math:`k`.
   :align: center

   Recovered tomography image with different sparse degree :math:`k`.



压缩比 :math:`{\rm CR} = 4` 时, 一维DCT过完备观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  14.440057558389176 2339.239048987087 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  14.407312672319945 2356.9430754649925 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  14.392225830410263 2365.1450361331595 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  14.438509731511893 2340.0729030920506 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  15.093057465950091 2012.6794588911266 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  14.015175521723268 2579.6620142755596 255 uint8

   [Finished in 1378.4s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/tomographyCR4alpha1e-6Dict1DODCTRecovery.*
   :scale: 100 %
   :alt: Recovered tomography image with different sparse degree :math:`k`.
   :align: center

   Recovered tomography image with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, 一维DCT过完备观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  12.971158037789456 3280.6851824428386 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  12.936695435825893 3306.8219923587253 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  14.334155129944055 2396.9824147020495 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  14.869213943506328 2119.136669233503 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  14.284916845043584 2424.312922047151 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  13.839801158638902 2685.9643555265966 255 uint8

   [Finished in 1380.3s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/tomographyCR16alpha1e-6Dict1DODCTRecovery.*
   :scale: 100 %
   :alt: Recovered tomography image with different sparse degree :math:`k`.
   :align: center

   Recovered tomography image with different sparse degree :math:`k`.



非稀疏信号CS
-----------------

压缩感知方式实验
~~~~~~~~~~~~~~~~~~~~~

Python 实现参见文件 `demo_csTwoWayAnalysis.py <https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_csTwoWayAnalysis.py>`_


.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_csTwoWayAnalysis.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 22,27,32,37
   :linenos:
   :caption: demo_csTwoWayAnalysis.py
   :name: bind-id


以cameraman图像为例, 两种非稀疏信号的压缩采样与恢复结果如下

压缩比设置为2, 采用OMP算法重构图像信号, 稀疏度设置为 :math:`k=32` 时的结果为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/cameramanNonSparseCS1hCR2k32.*
   :scale: 100 %
   :alt:
   :align: center


压缩比设置为4, 采用OMP算法重构图像信号, 稀疏度设置为 :math:`k=32` 时的结果为

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/cameramanNonSparseCS1hCR4k32.*
   :scale: 100 %
   :alt:
   :align: center


两种非稀疏信号的压缩采样与恢复方式表示为

方式1

1. 变换: :math:`{\bm z} = {\bm \Psi}_1{\bm x}`
2. 观测: :math:`{\bm y} = {\bm \Phi}{\bm z}`,
3. 求解: :math:`{\rm min}_{\bm z} \|{\bm z}\|_p  \ \  s.t. \  {\bm y} = {\bm \Phi}{\bm z}`
4. 重构: :math:`{\bm x} = {\bm \Psi}_2{\bm z}`

方式2

1. 观测: :math:`{\bm y} = {\bm \Phi}{\bm x}`
2. 求解: :math:`{\rm min}_{\bm z} \|{\bm z}\|_p \ \  s.t. \  {\bm y} = {\bm \Phi}{\bm \Psi}_1{\bm z}`
3. 重构: :math:`{\bm x} = {\bm \Psi}_2{\bm z}`

记 :math:`\bm D` 为正交DCT变换矩阵 (:math:`{\bm D}^{-1} = {\bm D}^T`), 使用不同的 :math:`{\bm \Psi}_1`, :math:`{\bm \Psi}_2` 组合, 衡量两种CS方法重构图像与原图间的均方误差, 结果为

+----------------------+----------------------+-------+-------+
| :math:`{\bm \Psi}_1` | :math:`{\bm \Psi}_2` | 方式1 | 方式2 |
+======================+======================+=======+=======+
| :math:`{\bm D}`      | :math:`{\bm D}`      | 3802  | 743   |
+----------------------+----------------------+-------+-------+
| :math:`{\bm D}^T`    | :math:`{\bm D}`      | 770   | 3816  |
+----------------------+----------------------+-------+-------+
| :math:`{\bm D}`      | :math:`{\bm D}^T`    | 616   | 3754  |
+----------------------+----------------------+-------+-------+
| :math:`{\bm D}^T`    | :math:`{\bm D}^T`    | 3874  | 589   |
+----------------------+----------------------+-------+-------+




一维压缩感知实验
~~~~~~~~~~~~~~~~~~~~~

实验完成对二维图像的高度维压缩采样与恢复.

无稀疏表示
^^^^^^^^^^^

- 图像信号: :math:`H\times W = 256\times 256`
- 表示字典: 无
- 观测矩阵: Gaussian观测矩阵, 一维DCT过完备观测矩阵, 尺寸 :math:`M\times N` , :math:`N = 256`
- 压缩比率: :math:`{\rm CR} = N/M`



.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaData.*
   :scale: 100 %
   :alt: Lena image.
   :align: center

   Lena image

压缩比 :math:`{\rm CR} = 4` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  5.22232377711354 19536.554946899414 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  5.251123223918265 19407.430450439453 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  5.356613492689134 18941.702514648438 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  5.456996728640617 18508.903366088867 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  6.588493687182973 14263.660461425781 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  6.0725505137777835 16062.950073242188 255 uint8

   [Finished in 431.7s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCR4alpha1e-6DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered lena image with different sparse degree :math:`k`.
   :align: center

   Recovered lena image with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, Gaussian观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  5.210776416835353 19588.569381713867 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  5.229416619643459 19504.67413330078 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  5.409661839488037 18711.740112304688 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  5.444672361916549 18561.502349853516 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  5.33433084335866 19039.137771606445 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  5.271223842201596 19317.813842773438 255 uint8

   [Finished in 374.4s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCR16alpha1e-6DictGaussianRecovery.*
   :scale: 100 %
   :alt: Recovered lena image with different sparse degree :math:`k`.
   :align: center

   Recovered lena image with different sparse degree :math:`k`.



压缩比 :math:`{\rm CR} = 4` 时, 一维DCT过完备观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  5.343276737179728 18999.960021972656 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  5.4361581642123955 18597.92724609375 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  5.456286226270971 18511.93165588379 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  5.477199979749907 18423.000457763672 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  6.330385584444022 15137.069412231445 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  10.306663047919827 6059.182815551758 255 uint8

   [Finished in 426.0s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCR4alpha1e-6Dict1DODCTRecovery.*
   :scale: 100 %
   :alt: Recovered lena image with different sparse degree :math:`k`.
   :align: center

   Recovered lena image with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 16` 时, 一维DCT过完备观测矩阵, 设置不同稀疏度下的信号重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  5.241856072986026 19448.88702392578 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  5.225959176230842 19520.208099365234 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  5.354500199748536 18950.92185974121 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  5.515306696304636 18262.056884765625 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  6.040420221353212 16182.22885131836 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  9.144875858455052 7917.585739135742 255 uint8

   [Finished in 383.2s]


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCR16alpha1e-6Dict1DODCTRecovery.*
   :scale: 100 %
   :alt: Recovered lena image with different sparse degree :math:`k`.
   :align: center

   Recovered lena image with different sparse degree :math:`k`.




含稀疏表示
^^^^^^^^^^^^


- 图像信号: :math:`H\times W = 256\times 256`
- 表示字典: DCT, 尺寸 :math:`256\times 256`
- 观测矩阵: Gaussian, 尺寸 :math:`M\times N` , :math:`N = 256`
- 压缩比率: :math:`{\rm CR} = N/M`


.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCS1hObsmatGaussionDictDCT.*
   :scale: 100 %
   :alt: Orignal image signal, dictionary matrix, observation matrix, sparse coefficient matrix.
   :align: center

   Orignal image signal, dictionary matrix, observation matrix, sparse coefficient matrix.



实现代码, 参见文件 `demo_cs1h_omp_img.py <https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs1h_omp_img.py>`_  .

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs1h_omp_img.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_cs1h_omp_img.py
   :name: bind-id


压缩比 :math:`{\rm CR} = 2` 时, Lena 图像重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  19.35324312034611 754.6681976318359 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  21.35199359181007 476.3004608154297 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  22.084221813206373 402.4001922607422 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  21.93230942365929 416.72486877441406 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  18.413869479192858 936.9003753662109 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  5.772999668544614 17209.98112487793 255 uint8
   [Finished in 754.8s]

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCS1hCR2ObsmatGaussionDictDCTalpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 2`) with different sparse degree :math:`k`.
   :align: center

   Recovery results (:math:`{\rm CR} = 2`) with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 4` 时, Lena 图像重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  17.30050349526095 1210.6817932128906 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  17.13251590038045 1258.4291534423828 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  16.41341724769021 1485.0416564941406 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  15.891063092434477 1674.8428039550781 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  6.054397672821921 16130.231246948242 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  5.569662696862794 18034.914642333984 255 uint8
   [Finished in 352.2s]

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCS1hCR4ObsmatGaussionDictDCTalpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 4`) with different sparse degree :math:`k`.
   :align: center

   Recovery results (:math:`{\rm CR} = 4`) with different sparse degree :math:`k`.

压缩比 :math:`{\rm CR} = 8` 时, Lena 图像重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  12.711132296542491 3483.1095275878906 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  12.24455126500644 3878.1556396484375 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  12.08576911176013 4022.5685119628906 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  6.243422364533981 15443.229461669922 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  5.658814132793683 17668.470169067383 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  5.437810904144429 18590.851013183594 255 uint8
   [Finished in 380.7s]

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCS1hCR8ObsmatGaussionDictDCTalpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 8`) with different sparse degree :math:`k`.
   :align: center

   Recovery results (:math:`{\rm CR} = 8`) with different sparse degree :math:`k`.


压缩比 :math:`{\rm CR} = 16` 时, Lena 图像重构结果:

::

   ---PSNR1, MSE1, Vpeak1, dtype:  12.530425704027621 3631.0964965820312 255 uint8
   ---PSNR2, MSE2, Vpeak2, dtype:  12.46201822823682 3688.744186401367 255 uint8
   ---PSNR3, MSE3, Vpeak3, dtype:  6.453316341931616 14714.609008789062 255 uint8
   ---PSNR4, MSE4, Vpeak4, dtype:  5.758194148603205 17268.751739501953 255 uint8
   ---PSNR5, MSE5, Vpeak5, dtype:  5.461627943974914 18489.17642211914 255 uint8
   ---PSNR6, MSE6, Vpeak6, dtype:  5.355063389623071 18948.464477539062 255 uint8
   [Finished in 396.7s]

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/lenaCS1hCR16ObsmatGaussionDictDCTalpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 16`) with different sparse degree :math:`k`.
   :align: center

   Recovery results (:math:`{\rm CR} = 16`) with different sparse degree :math:`k`.

二维压缩感知实验1
~~~~~~~~~~~~~~~~~~~~~

实验完成对二维图像的高度维和宽度维压缩采样与恢复, 实验中将原始图像拉成列向量, 应用压缩感知理论进行采样模拟与恢复.



二维压缩感知实验2
~~~~~~~~~~~~~~~~~~~~~

实验完成对二维图像的高度维和宽度维压缩采样与恢复, 实验中, 应用压缩感知理论, 对图像信号分别进行高度维和宽度维的两次压缩采样与恢复.



复压缩感知实验
-----------------------


核磁共振成像
~~~~~~~~~~~~~~~~~~~

对核磁共振图像(MRI)原始 k-space 数据进行行方向上的压缩采样与恢复, 采用OMP算法恢复信号.

实验代码
^^^^^^^^^^^

实现代码, 参见文件 `demo_cs1d_omp_mri.py <https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs1h_omp_img.py>`_  .

.. literalinclude:: https://github.com/antsfamily/pysparse/tree/master/examples/LinearCS/demo_cs1d_omp_mri.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 43-49
   :linenos:
   :caption: demo_cs1d_omp_mri.py
   :name: bind-id

实验结果
^^^^^^^^^^^^^

压缩比 :math:`{\rm CR} = 4`, 无稀疏表示字典时, MRI 图像重构结果:

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/mriCCS1hCR4ObsmatGaussionDictNoneSparseDegree100alpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 4`) with sparse degree :math:`k=100`.
   :align: center

   Recovery results (:math:`{\rm CR} = 4`) with sparse degree :math:`k=100`.

压缩比 :math:`{\rm CR} = 4`, DCT稀疏表示字典时, MRI 图像重构结果:

.. figure:: ../../../_static/figs/SignalProcessing/Sparse/LinearCS/Experiments/mriCCS1hCR4ObsmatGaussionDictDCTSparseDegree100alpha1e-6.*
   :scale: 100 %
   :alt: Recovery results (:math:`{\rm CR} = 4`) with sparse degree :math:`k=100`.
   :align: center

   Recovery results (:math:`{\rm CR} = 4`) with sparse degree :math:`k=100`.

