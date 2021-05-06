.. _Section-SARTrainingProcessorLibrariesSoftwaresSupplementRadar:

SAR Training Processor
=========================




基础教程
----------------


源码安装
~~~~~~~~~~~~~



在 `ASF_Mapready/src/stp` 目录下含 `STP` 源码, 修改该目录下的 `Makefile` 文件, 添加如下路径, 注意修改为自己的路径:::

    BINDIR=/mnt/e/sfw/sar/ASF_MapReady/bin/
    SHAREDIR=/mnt/e/sfw/sar/ASF_MapReady/share/asf_tools/mapready/

然后在 `ASF_Mapready` 源码目录直接执行如下命令安装:

.. code-block:: bash

    cd ./src/stp/
    make


安装完成后输入 ``stp`` 可以启动 STP 软件.


源码简析
~~~~~~~~~~~~~~~~~~~


成像处理: :func:`ardop` --> :func:`processPatch`


问题与解决
----------------------


使用
~~~~~~~~~~~~~~~~~~



内存溢出
^^^^^^^^^^^^^^^

若安装完, 在导入数据时提示如下内存溢出错误信息, 则可判定程序有内存溢出现象, 如在导入 ``CEOS`` 格式的数据时提示如下错误信息, 后经排查是 :func:`import_ceos_raw` 函数中的代码导致的 ``strcpy(meta->sar->polarization, meta->general->bands);``, `meta_sar->polarization` 是一个大小为 15 的数组, 理论上已经够用, 而从文件中读出的 ``meta->general->bands`` 信息实际超过了此大小, 如多了很多空格, 从而导致内存溢出, 适当增加polarization的大小即可.


::

    *** buffer overflow detected ***: stp terminated
    ======= Backtrace: =========
    /lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7f307f5797e5]
    /lib/x86_64-linux-gnu/libc.so.6(__fortify_fail+0x5c)[0x7f307f61b15c]
    /lib/x86_64-linux-gnu/libc.so.6(+0x117160)[0x7f307f619160]
    /lib/x86_64-linux-gnu/libc.so.6(+0x1164b2)[0x7f307f6184b2]



