.. _Section-EvaluationMethodImageQuality:

图像质量评价
===========================


误差类
---------------



均方误差
~~~~~~~~

.. math::
    {\rm MSE} = \frac{1}{MN}\sum_{i=1}^{M}\sum_{j=0}^{N}[|{\bm I}(i,j)|, |\hat{\bm I}(i, j)|]^2





信噪比类
-------------


.. math::
    {\rm PSNR} = 10 \log10(\frac{V_{peak}^2}{\rm MSE})



结构相似性度量
-----------------

SSIM
~~~~~~~~~~

结构相似性指数 (:term:`Structure SIMilarity index`, SSIM) 由周等人于2004年提出 :cite:`Image2004ZhouSSIM`, 设有数据 :math:`x` 和参考数据 :math:`y`, :math:`\mu_x, \mu_y` 分别为其均值, :math:`\sigma_x, \sigma_y` 分别为标准差, :math:`\sigma^2_x, \sigma^2_y` 为其方差, :math:`\sigma_{xy}` 为数据 :math:`x` 和参考数据 :math:`y` 的协方差, 用 :math:`l, c, s` 分别表示亮度(luminance), 对比度(contrast) 和结构 (structure) 相似性, 则

.. math::
       \begin{aligned} l(x, y) &=\frac{2 \mu_{x} \mu_{y}+c_{1}}{\mu_{x}^{2}+\mu_{y}^{2}+c_{1}} \\
       c(x, y) &=\frac{2 \sigma_{x} \sigma_{y}+c_{2}}{\sigma_{x}^{2}+\sigma_{y}^{2}+c_{2}} \\
       s(x, y) &=\frac{\sigma_{x y}+c_{3}}{\sigma_{x} \sigma_{y}+c_{3}} \end{aligned}

其中, :math:`c_1 = (k_1 L)^2, c_2 = (k_2 L)^2, c_3 = c_2 / 2`,
:math:`L` 是数据的动态范围 (dynamic range) ( 典型的 :math:`L = 2 ^{\# \text { bits per pixel }}-1`). 结构则相似性指标可表示为

.. math::
   \operatorname{SSIM}(x, y)=\left[l(x, y)^{\alpha} \cdot c(x, y)^{\beta} \cdot s(x, y)^{\gamma}\right].

当 :math:`\alpha=\beta=\gamma=1`, SSIM 等价于

.. math::
   \operatorname{SSIM}(x, y)=\frac{\left(2 \mu_{x} \mu_{y}+c_{1}\right)\left(2 \sigma_{x y}+
   c_{2}\right)}{\left(\mu_{x}^{2}+\mu_{y}^{2}+c_{1}\right)\left(\sigma_{x}^{2}+\sigma_{y}^{2}+c_{2}\right)}



MSSSIM
~~~~~~~~~~~~




GSSIM
~~~~~~~~~~~~~

基于梯度的结构相似性 (:term:`Gradient-based Structure SIMilarity index`, GSSIM) 度量方法 :cite:`Gradient2006ChenGSSIM`, 对SSIM中的对比度和结构度量部分做了更改, 使用数据的梯度而不是数据来计算. 对于二维图像数据, 梯度的计算可以通过 sobel 算子滤波实现. sobel算子在水平和垂直方向上可表示为


.. math::
   G_v=\left[\begin{array}{ccc}{-1} & {-2} & {-1} \\ {0} & {0} & {0} \\ {+1} & {+2} & {+1}\end{array}\right]

.. math::
   G_h=\left[\begin{array}{ccc}{-1} & {0} & {+1} \\ {-2} & {0} & {+2} \\ {-1} & {0} & {+1}\end{array}\right]

`link text <url>`_  



实验与分析
-------------------

核心代码
~~~~~~~~~


.. code-block:: python
    :lineno-start: 0
    :emphasize-lines: 72
    :linenos:
    :caption: demo_python.m
    :name: bind-id

    def ssim(X, Y, win=None, winsize=11, L=None, k1=0.01, k2=0.03, alpha=1, beta=1, gamma=1, isavg=True, full=False):
        r"""Structural similarity index

        Parameters
        ----------
        X : {ndarray}
            reconstructed
        Y : {ndarray}
            referenced
        win : {[type]}, optional
            [description] (the default is None, which [default_description])
        winsize : {number}, optional
            [description] (the default is 11, which [default_description])
        L : {integer}, optional
            the dynamic range of the pixel-values (typically this is :math:`2 ^{\# \text { bits per pixel }}-1`. (the default is 255)
        k1 : {number}, optional
            [description] (the default is 0.01, which [default_description])
        k2 : {number}, optional
            [description] (the default is 0.03, which [default_description])
            sizeavg : {bool}, optional
            whether to average (the default is True, which average the result)
        alpha : {number}, optional
            luminance weight (the default is 1)
        beta : {number}, optional
            contrast weight (the default is 1)
        gamma : {number}, optional
            structure weight (the default is 1)
        isavg : {bool}, optional
            IF True, return the average SSIM index of the whole iamge,
        full : {bool}, optional
            IF True, return SSIM, luminance, contrast and structure index (the default is False, which only return SSIM)
        """

        if L is None:
            _, L = get_drange(Y.dtype)

        C1 = (k1 * L)**2
        C2 = (k2 * L)**2
        C3 = C2 / 2.

        if win is None and type(winsize) is not int:
            winsize = 11
            win = _SSIM_GAUSSIAN_KERNEL_11X11
        if win is None and type(winsize) is int:
            win = create_window(winsize, 1)

        muX = convolve(X, win)
        muY = convolve(X, win)
        muXsq = muX * muX
        muYsq = muY * muY

        sigmaXsq = np.abs(convolve(X * X, win) - muXsq)
        sigmaYsq = np.abs(convolve(Y * Y, win) - muYsq)
        sigmaXY = convolve(X * Y, win) - muX * muY

        sigmaX = np.sqrt(sigmaXsq)
        sigmaY = np.sqrt(sigmaYsq)

        luminance = (2. * muX * muY + C1) / (muX * muX + muY * muY + C1)
        contrast = (2 * sigmaX * sigmaY + C2) / (sigmaXsq + sigmaYsq + C2)
        structure = (sigmaXY + C3) / (sigmaX * sigmaY + C3)

        ssim_map = (luminance**alpha) * (contrast**beta) * (structure**gamma)

        if isavg:
            ssim_map = np.mean(ssim_map)
            luminance = np.mean(luminance)
            contrast = np.mean(contrast)
            structure = np.mean(structure)

        if full:
            return ssim_map, luminance, contrast, structure
        else:
            return ssim_map



