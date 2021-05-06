.. _Section-PolSARproLibrariesSoftwaresSupplementRadar:

PolSARpro
=====================

简介
--------------------

`PolSARpro <https://www.ietr.fr/polsarpro-bio/>`_ 由欧洲航空局(ESA)于2003年起开发维护至今, 含Windows和Linux两种操作系统下的软件版本, 支持的极化SAR卫星产品有: AIRSAR, ALOS2, RADARSAT2, ALOS1, GAOFEN3, RISAT, S1A_20180125, S1B_20180102.


基础教程
--------------------

安装
~~~~~~~~~~~~~~~~~~~~~~~~

从 `这里 <https://www.ietr.fr/polsarpro-bio/>`_ 选择要安装的版本, 下载软件安装包, 这里以 ``Linux`` 版为例. 解压安装包 ``PolSARpro_v6.0_Biomass_Edition_Linux_Installer_20190404.zip``, 终端输入 ``xterm`` 命令打开 Xterm 终端. 执行 ``wish PolSARpro_v6.0_Biomass_Edition_Linux_Installer.tcl `` 打开安装界面, 根据提示需要安装依赖库.

.. code-block:: bash
   :caption: 安装依赖库
   :linenos:
   :emphasize-lines: 3,5

   sudo apt install libtk-img iwidgets4 bwidget
   sudo apt install gcc g++ build-essential libglew-dev freeglut3-dev libfreeimage-dev
   sudo apt install gimp gnuplot googleearth-package imagemagick snap

选择好安装目录后点击 ``Install`` 按钮执行安装即可. 安装完成后, 在安装根目录可以看到如下文件夹

 ColorMap directory: 包含用户定义与修改的PolSARpro颜色映射文件
 Config directory: 包含软件的所有不同配置文件
 GUI directory: 包含所有widget窗口Tcl-Tk文件
 Help directory: 包含PolSARpro帮助文件
 License directory: 包含所有的 PolSARpro licenses 文件
 Log directory: 包含所有会话的日志文件
 Soft directory: 包含可使用的可执行处理文件和库
 TechDoc directory: 包含与PolSARpro中使用的所有GUI和C例程相关的技术文档
 Tmp directory: Tmp目录在安装后为空, PolSARpro在每个会话期间都会使用它
 Tutorial directory: 包含PDF格式的PolSARpro教程材料




进阶教程
--------------------
