.. _Section-SNAPLibrariesSoftwaresSupplementRadar:

STEP与SNAP
=====================

简介
--------------------

`STEP <http://step.esa.int/main/>`_ (Scientific Toolbox Exploitation Platform, STEP) 是欧洲航空局(ESA) 研发的开源科学工具箱开发平台, `SNAP <http://step.esa.int/main/toolboxes/snap/>`_ (SentiNel Application Platform, SNAP) 是其中用于处理哨兵系列数据的开源应用软件平台, 含Windows, Mac OS X和Linux三种操作系统下的软件版本, 支持 RADARSAT1-2, Sentinel1-3等卫星产品.


环境配置
--------------------

安装
~~~~~~~~~~~~~~~~~~~~~~~~


源码构建安装
^^^^^^^^^^^^^

SNAP开源源码目录为 `senbox.org <https://github.com/senbox-org/>`_, 其中有一些 `例子 <https://github.com/senbox-org/snap-examples>`_ 可供参考.


安装包安装
^^^^^^^^^^^^

各版本软件及Sentinel1-3, SMOS, Radarsat2, PROBA-V工具箱可以在 `snap download <http://step.esa.int/main/download/snap-download/>`_ 下载. 本节以Linux版本为例, 介绍SNAP的安装过程.

终端执行 ``./esa-snap_all_unix_7_0.sh`` 命令打开安装设置界面, 选择安装路径后, 继续选择需要安装的组件(Sentinel2-3, SMOS, Radarsat2, PROBA-V工具箱).

.. figure:: ../../../_static/figs/Radar/Supplement/LibrariesSoftwares/SNAP/Setup_SelectToolBox_ESA_SNAP_7_0_004.*
   :alt: ESA SNAP 安装之工具箱选择
   :align: center

   在ESA SNAP安装界面可以选择是否安装Sentinel2-3, SMOS, Radarsat2, PROBA-V工具箱.

接着按提示完成安装即可.

.. hint:: 为了后期可以在Python中使用SNAP, 在SNAP的安装设置过程中, 需要配置Python, 参见 :ref:`SubSubSection-ConfigurePythonToUseSnappy` 小节.


Level1数据处理示例
--------------------


Python与SNAP
--------------------

简介
~~~~~~~~~~~~~~~~~~~

通过SNAP提供的snappy接口, 可以在Python中使用SNAP API, 本节主要介绍, 如何进行Python与SNAP的交互式开发. 可以通过以下两种方式, 既可以在Python中调用SNAP函数(Java API), 又可以扩展基于Python的SNAP插件:

- 使用标准Python（CPython）安装

- 使用与SNAP捆绑在一起的Python的Jython纯Java实现


如果你不准备开发桌面GUI环境并且想使用Python的科学计算库, 那么推荐使用第一种方式, 反之推荐第二种方式.

.. hint::
   可参考 `SNAP Wiki <https://senbox.atlassian.net/wiki/spaces/SNAP>`_ 中的教程 `Using SNAP in your Python programs <https://senbox.atlassian.net/wiki/spaces/SNAP/pages/24051781/Using+SNAP+in+your+Python+programs>`_ . 此功能目前仅支持Python2.7, 3.3, 3.4.


.. _SubSubSection-ConfigurePythonToUseSnappy:

配置 Python 以使用snappy
~~~~~~~~~~~~~~~~~~~~~~~~

最简单的方法是在安装SNAP的过程中配置, 需要配置Python可执行文件路径, 可以通过 ``which python2``, ``which python3`` 分别查看Python2和Python3的路径, 配置好路径后, 点击 :attr:`Next` 安装即可.

.. figure:: ../../../_static/figs/Radar/Supplement/LibrariesSoftwares/SNAP/Setup_Python_ESA_SNAP_7_0_004.*
   :alt: ESA SNAP 安装之Python设置
   :align: center

   在ESA SNAP安装过程中配置Python可执行文件路径.

如果安装时没有配置Python, 也可以手动通过命令配置. 打开终端, 使用如下命令进入SNAP安装目录并配置Python环境. 其中 ``<python-exe-fullpath>`` 为Python可执行文件的完整路径, ``<snappy-installdir>`` 为snappy的安装路径, 默认为 ``~/.snap/snap-python``.

.. code-block:: bash
   $ cd <snap-install-dir>/bin

   # Unix:
   $ ./snappy-conf <python-exe-fullpath> <snappy-installdir>

   # Windows:

   $ snappy-conf <python-exe-fullpath> <snappy-installdir>


为了在Python中方便导入snappy包, 可以通过 ``sudo gedit ~/.bashrc`` 打开 `.bashrc` 文件并添加如下环境变量::

   export PYTHONPATH=$PYTHONPATH:~/.snap/snap-python/

接着, 在Python中, 执行 ``from snappy import ProductIO`` 来测试配置是否成功. 配置不成功将会提示错误, 如 `No module named snappy`.


在Python中调用SNAP函数
~~~~~~~~~~~~~~~~~~~~~~~~



开发SNAP的Python处理器插件
~~~~~~~~~~~~~~~~~~~~~~~~






使用Python接口导出原始SAR数据
~~~~~~~~~~~~~~~~~~~~~~~~~~~







总结
------------------


链接
~~~~~~~~~~~~~~~


- `Homepage of ESA <http://www.esa.int/>`_
- `Homepage of STEP <http://step.esa.int/main/>`_
- `Homepage of SNAP <http://step.esa.int/main/toolboxes/snap/>`_
- `Source code of SNAP <https://github.com/senbox-org/>`_
- `Download SNAP <http://step.esa.int/main/download/snap-download/>`_
- `SNAP Wiki <https://senbox.atlassian.net/wiki/spaces/SNAP>`_
- `Documentation of SNAP <http://step.esa.int/main/doc/>`_
- `SNAP Engine API <http://step.esa.int/docs/v2.0/apidoc/engine/>`_
- `forum of SNAP <https://forum.step.esa.int/>`_ 论坛
