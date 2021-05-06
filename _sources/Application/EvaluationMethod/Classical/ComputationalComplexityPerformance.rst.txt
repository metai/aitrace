.. _Section-ComputationalComplexityPerformanceClassicalEvaluationMethodApplication:

计算复杂度/性能
===========================


操作数相关指标
-----------------

操作数或运算次数通常用于衡量处理器的性能, 也可以用于衡量算法的复杂度.

当用于衡量处理器性能时, 通常用 **操作数/每秒** (Operations Per Second, OPS)表示处理器每秒所能执行的操作次数, 用 **浮点运算次数/每秒** (FLoating-point Operations Per Second, FLOPS) 表示处理器每秒所能执行的浮点运算次数. 有时也用 ``OPS@FPx`` 来表示处理器的 ``x`` 位浮点数处理能力, 如 ``1TOPS@FP16`` 表示半精度浮点数下的浮点数运算能力为 ``1TOPS``, 其中, ``FP`` 表示浮点数(Float Point) :math:`1\rm{TOPS}=10^{12} \rm{OPS}`, 不加说明时, :math:`{\rm FLOPS} = {\rm OPS}@{\rm FP}32`, 下 :table:numref:`table-QuantityUnitLetter` 给出了其它单位的值.


.. table:: 常用数量单位及字母表示
   :name: table-QuantityUnitLetter

   +---------------+----------+-------+-----------------+
   | 单位          | 中文     | 英文  | 值              |
   +===============+==========+=======+=================+
   | :math:`\rm M` | 一百万   | Mega  | :math:`10^6`    |
   +---------------+----------+-------+-----------------+
   | :math:`\rm G` | 十亿     | Giga  | :math:`10^9`    |
   +---------------+----------+-------+-----------------+
   | :math:`\rm T` | 一万亿   | Tera  | :math:`10^{12}` |
   +---------------+----------+-------+-----------------+
   | :math:`\rm P` | 一千万亿 | Peta  | :math:`10^{15}` |
   +---------------+----------+-------+-----------------+
   | :math:`\rm E` |          | Exa   | :math:`10^{18}` |
   +---------------+----------+-------+-----------------+
   | :math:`\rm Z` |          | Zetta | :math:`10^{21}` |
   +---------------+----------+-------+-----------------+
   | :math:`\rm Y` |          | Yotta | :math:`10^{24}` |
   +---------------+----------+-------+-----------------+

.. hint::

   通常用 :math:`{\rm FP}64` 表示64位(bit)双精度浮点数, :math:`{\rm FP}32` 表示32位(bit)单精度浮点数, :math:`{\rm FP}16` 表示16位(bit)半精度浮点数, :math:`{\rm FP}8` 表示8位(bit)浮点数, :math:`{\rm INT}64` 表示64位(bit)整数等等.

   一般地, :math:`1{\rm OPS}@{\rm FP}64 = 2{\rm OPS}@{\rm FP}32 = 4{\rm OPS}@{\rm FP}16 = 8{\rm OPS}@{\rm FP}8`, 不过不是总能成立, 有的处理器略有差异. 此外, 一个 :math:`1{\rm OPS}@{\rm FP}16` 的处理器的16位整数运算性能略大于 :math:`1{\rm OPS}@{\rm INT}16`.


当用于衡量算法的复杂度时, 通常用 **操作数** (OPerations, OPs)表示算法所需要执行的操作次数, 用 **浮点运算次数** (FLoating-point OPerations, FLOPs)表示算法所需要执行的浮点运算次数.




处理器的衡量指标
----------------


传统指标
~~~~~~~~

- 操作数(Operations Per Second, OPS): 即每秒执行的操作次数
- 浮点运算次数(FLoating-point Operations Per Second, FLOPS): 即每秒执行的浮点运算次数
- 单位: 一百万(Mega, :math:`10^6`), 十亿(Giga, :math:`10^9`), 一万亿(Tera, :math:`10^{12}`), 一千万亿(Peta, :math:`10^{15}`)


计算平台与模型性能指标
--------------------------

衡量一个计算平台或模型的性能指标可以通过计算量(算力/运算量) :math:`\pi` 与访存量(内存读写带宽/内存读写量) :math:`\beta` 以及计算强度 :math:`\mathcal I` 来分析. 通常地, 计算强度定义为

.. math::
   {\mathcal I} = \frac{\pi}{\beta}

当评估计算平台性能时, :math:`\pi` 表示计算平台的算力, 即每秒可执行的运算次数 (Operations Per Second, OPS), :math:`\beta` 表示计算平台内存带宽, 单位通常为 bps(bit per second); 当评估模型性能时, :math:`\pi` 表示模型计算量, 即需要执行的运算次数 (OPerations, OPs),  :math:`\beta` 表示内存读写量, 单位通常为字节 B (Byte).

举个例子, :figure:numref:`fig-FigureSSD_FLOPS_MEMRW` 给出了SSD300网络的各层计算量与内存访问量分析结果, 包括输入输出大小, 参数量 (params), 乘累加量 (Fused multiply–add, Madd), 浮点数运算量 (FLOPs) 以及内存读写量 (MemR+W).

.. _fig-FigureSSD_FLOPS_MEMRW:

.. figure:: ../../../_static/figs/Application/EvaluationMethod/Classical/SSD_FLOPS_MEMRW.*
   :scale: 80 %
   :alt: LeNet
   :align: center

   SSD 300 网络计算量与内存访问量分析

由 :figure:numref:`fig-FigureSSD_FLOPS_MEMRW` 知, SSD300网络含有 :math:`26,285,486` 个参数, 内存占用为 :math:`207.65{\rm MB}`, 总乘累加次数为 :math:`62.78{\rm GB}`, 总浮点运算次数为 :math:`31.44{\rm GFLOPs@FP32}`, 见 :table:numref:`table-ParametersComplexitySSD300`. 即对于每张 :math:`300\times 300` 大小的图片, 前向推理一次需要的浮点数运算量约为 :math:`31.44{\rm GFLOPs}` 访存量为 :math:`542.79{\rm MB}`, 故 SSD300 模型的计算强度为 :math:`{\mathcal I}_{ssd} = 31.44{\rm GFLOPs} / 542.79{\rm MB} = 4\times 31.44e9 / 542.79e6 = 231.69 {\rm FLOPs/Byte}`.


.. table:: SSD300网络参数与计算量
   :name: table-ParametersComplexitySSD300

   +--------------+--------------+------------+-------------+--------------+
   | Total params | Total memory | Total MAdd | Total FLOPs | Total MemR+W |
   +==============+==============+============+=============+==============+
   | 26,285,486   | 207.65MB     | 62.78G     | 31.44G      | 542.79MB     |
   +--------------+--------------+------------+-------------+--------------+


昇腾处理器Ascend 310的开发套件的内存为8GB, 远大于SSD300网络的内存占用量(207.65MB), 内存规格为LPDDR4x, 带宽为 :math:`3200{\rm Mbps}`. 昇腾处理器Ascend 310的浮点数处理能力为 :math:`8{\rm TOPS@FP16}`, 即 :math:`8{\rm TFLOPS@FP16}`, 亦即 :math:`4{\rm TFLOPS@FP32}`. Ascend 310 处理器的计算强度为 :math:`{\mathcal I}_{Ascend310} = (4\times 4e12) / (3200e6/8) = 40000 {\rm FLOPs}/{\rm Byte}`. 由此可知, Ascend 310 处理器的计算强度约为SSD300模型的计算强度的 :math:`172` 倍. 然而, 计算平台的带宽为 :math:`3200{\rm Mbps}`, 即每秒读写数据量最多为 :math:`400{\rm MB}`, 而SSD网络的访存量为 :math:`542.79{\rm MB}`.


