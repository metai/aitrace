.. _Section-IntroductionLispProgramingComputerScience:

引言
=====================


什么是Lisp语言
----------------


Common Lisp语言的实现(解释器)有多种, 如 **CLISP**, **SBCL (Steel Bank Common Lisp)**, **CCL (Clozure Common Lisp)** 等等, 其功能特性对比如下 :table:numref:`table-ComparisonOfImplementationOfCommonLisp` 所示

.. table:: Common Lisp语言的实现特性对比
   :name: table-ComparisonOfImplementationOfCommonLisp


   +----------+--------------------------+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------+
   | 实现名称 | 首页                     | 功能特性                                                         | 适用平台                                                                                                       | 其它     |
   +==========+==========================+==================================================================+================================================================================================================+==========+
   | CLISP    | http://clisp.org/        | 解释、编译、运行、调试、外部函数接口等等                         | Linux、Windows、MacOS X、其它类Unix系统                                                                        | 开源     |
   +----------+--------------------------+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------+
   | SBCL     | http://www.sbcl.org/     | 解释、编译、运行、调试、统计分析、代码覆盖等等                   | Linux、Windows、MacOS X、其它类Unix系统                                                                        | 开源免费 |
   +----------+--------------------------+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------+
   | CCL      | https://ccl.clozure.com/ | 快速编译、本机线程、精确、压缩的垃圾收集、方便的外部函数接口等等 | Linux (x86, x86-64, ppc32, ppc64, armv7l/armv6)、Windows (x86, x86-64)、Mac OS X (x86, x86-64)、其它类Unix系统 | 开源     |
   +----------+--------------------------+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------+



.. hint:: 资源链接

    - `common lisp <https://www.common-lisp.net/>`_ : The amazing world of Common Lisp, the programmable programming language.
    - `lispbox <https://common-lisp.net/project/lispbox/>`_ : 集成了Lisp语言包, Emacs, Slime的集成开发环境.
    - `ANSI Common Lisp ZH <https://acl.readthedocs.io/en/latest/zhCN/>`_ : ANSI Common Lisp 中文版.
    - `practical common lisp <http://www.gigamonkeys.com/book/>`_ : An book on Common Lisp programing.



开发环境配置
----------------



安装Common Lisp实现
~~~~~~~~~~~~~~~~~~~~~

本节介绍Common Lisp实现的安装.



安装SBCL实现
^^^^^^^^^^^^^^^^^^^^^

Ubuntu上安装SBCL十分简单, 只需通过执行命令 ``sudo apt install sbcl`` 即可安装, 安装完成后, 终端输入 ``sbcl`` 即可进入交互界面, 如 :figure:numref:`fig-SBCLUbuntuWelcome` 所示.

.. _fig-SBCLUbuntuWelcome:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Lisp/Introduction/SBCLUbuntuWelcome.*
   :alt: Welcome interface of SBCL on Ubuntu
   :scale: 80 %
   :align: center

   Welcome interface of SBCL on Ubuntu

   Ubuntu上的SBCL欢迎界面


安装CLISP实现
^^^^^^^^^^^^^^^^^

CLISP安装很简单, 从 `clisp.org <http://clisp.org/>`_ 可以下载安装包或源码. 对于Windows系统, 执行下载的可执行文件 `clisp-2.49-win32-mingw-big.exe` 安装即可, 安装完成后双击打开 ``clisp.exe`` 即可进入交互式界面, 如 :figure:numref:`fig-ClispWindowsWelcome` 所示. 对于Ubuntu系统, 可以直接通过包管理器安装, 打开终端, 输入命令 ``sudo apt-get install clisp`` 即可安装, 安装完成后, 终端输入 ``clisp`` 命令进入交互式界面, 如 :figure:numref:`fig-ClispUbuntuWelcome` 所示.

.. _fig-ClispWindowsWelcome:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Lisp/Introduction/ClispWindowsWelcome.*
   :alt: Welcome interface of Clisp on Windows
   :align: center

   Welcome interface of Clisp on Windows

   Windows上的Clisp欢迎界面


.. _fig-ClispUbuntuWelcome:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Lisp/Introduction/ClispUbuntuWelcome.*
   :alt: Welcome interface of Clisp on Ubuntu
   :scale: 80 %
   :align: center

   Welcome interface of Clisp on Ubuntu

   Ubuntu上的Clisp欢迎界面




开发环境配置
~~~~~~~~~~~~~~~~~~~

Emacs + Slime 环境
^^^^^^^^^^^^^^^^^^^




Sublime 环境
^^^^^^^^^^^^^^^^^^^



Lisp编程入门
----------------

交互式界面使用
~~~~~~~~~~~~~~~

:figure:numref:`fig-ClispWindowsWelcome` 和  :figure:numref:`fig-ClispUbuntuWelcome` 中同时给出了两个示例: 1) 打印字符串 (``(princ "Hello World!")``); 2) 计算1+2的和 (``(+ 1 2)``), 你可以尝试一下其它表达式的计算.





第一个Lisp程序
~~~~~~~~~~~~~~~~~~~

这里介绍如何像在Python和Lua中那样导入其它文件中的函数. 首先建立文件 `add.lisp`, 加入如下代码, 代码仅含1行, 定义了一个返回两个数加和的函数 :func:`add`.

.. code-block:: lisp
    :lineno-start: 1
    :emphasize-lines: 1
    :linenos:
    :caption: add.lisp
    :name: bind-id

    (defun add (&key a b) (+ a b))

然后新建 `first.lisp` 文件, 并加入如下代码, 代码第1行完成加载`add`模块的功能; 第3行完成打印字符串 ``Hello world!`` 的功能;  第5行调用 :func:`add`, 传入参数 :math:`a=1, b=2`, 并将返回值赋予变量 :math:`c`; 第7行以两位小数格式化打印结果, 第9行是将程序编译成可执行文件 `main.exe`.

.. code-block:: lisp
    :lineno-start: 1
    :emphasize-lines: 1,3
    :linenos:
    :caption: first.lisp
    :name: bind-id

    (load "D:\\zhiliu\\ws\\Lisp\\add.lisp")

    (princ "Hello world!")

    (setq c (add :a 1 :b 2))

    (print c)

    (EXT:SAVEINITMEM "main" :QUIET t :INIT-FUNCTION 'main :EXECUTABLE t :NORC t)



打开lisp交互界面, 输入 ``(load "D:\\zhiliu\\ws\\Lisp\\first.lisp")`` 可以加载并执行first模块. 也可以打开系统命令行终端, 输入 ``sbcl --load .\first.lisp`` 或 ``clisp .\first.lisp`` 运行程序, 如 :figure:numref:`fig-RunLispFile` 所示

.. _fig-RunLispFile:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Lisp/Introduction/RunLispFile.*
   :alt: Run lisp file
   :align: center

   Run lisp file

   运行lisp程序


.. hint:: 以上代码可以直接在交互式界面窗口执行.


包库管理
-----------------------------

quicklisp
~~~~~~~~~~~~~~~~~~

安装
^^^^^^^

`quicklisp <https://www.quicklisp.org/beta/>`_ 是Common Lisp的库管理器, 支持用简单的几条命令下载, 安装和加载库. quicklisp的安装很简单, 以Ubuntu系统为例, 从quicklisp首页下载 `quicklisp.lisp` 安装脚本文件, 打开终端, 进入 `quicklisp` 文件所在目录, 执行 ``clisp --load quicklisp.lisp`` 或 ``sbcl --load quicklisp.lisp`` 进入安装界面, 如 :figure:numref:`fig-InstallQuickLispUbuntu` 所示, 按照提示, 执行 ``(quicklisp-quickstart:install :path "/mnt/e/sfw/lisplib/quicklisp/")`` lisp命令既可安装, 其中 :attr:`path` 用于指定安装路径.

.. _fig-InstallQuickLispUbuntu:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Lisp/Introduction/InstallQuickLispUbuntu.*
   :alt: Install quicklisp on ubuntu
   :align: center

   Install quicklisp on ubuntu

   Install quicklisp on ubuntu


设置默认加载
^^^^^^^^^^^^^^^^^

在Lisp交互界面, 首先加载quicklisp, 然后设置为启动默认加载, 命令如下::

    (load "/mnt/e/sfw/lisplib/quicklisp/setup.lisp")
    (ql:add-to-init-file)

命令输出如下::

    [1]> (load "/mnt/e/sfw/lisplib/quicklisp/setup.lisp")
    ;; Loading file /mnt/e/sfw/lisplib/quicklisp/setup.lisp ...
    ;; Loading file /mnt/e/sfw/lisplib/quicklisp/cache/asdf-fasls/0hq63s/asdf.fas ...
    ;; Loaded file /mnt/e/sfw/lisplib/quicklisp/cache/asdf-fasls/0hq63s/asdf.fas
    ;; Loaded file /mnt/e/sfw/lisplib/quicklisp/setup.lisp
    T
    [2]> (ql:add-to-init-file)
    I will append the following lines to #P"/home/liu/.clisprc.lisp":

      ;;; The following lines added by ql:add-to-init-file:
      #-quicklisp
      (let ((quicklisp-init
    (merge-pathnames "/mnt/e/sfw/lisplib/quicklisp/setup.lisp"
     (user-homedir-pathname))))
        (when (probe-file quicklisp-init)
          (load quicklisp-init)))

    Press Enter to continue.


使用
^^^^^^^^^^^^^^^^^^^^^

.. hint:: quicklisp 用法

    - To load/install a system, use: (ql:quickload "system-name")
    - To remove a system, use: (ql:uninstall "system-name")
    - To find systems, use: (ql:system-apropos "term")
    - To get updated software, use: (ql:update-dist "quicklisp")
    - To update the Quicklisp client, use: (ql:update-client)
    - To see what systems depend on a particular system, use: (ql:who-depends-on "system-name")
    - To load Quicklisp every time you start Lisp, use: (ql:add-to-init-file)
    - For more information, see http://www.quicklisp.org/beta/


以安装 `lisp-binary <https://github.com/j3pic/lisp-binary>`_ 进入Lisp交互环境, 执行 ``(ql:quickload "lisp-binary")`` 命令即可安装, 安装日志如下 ::

  $ sbcl
  This is SBCL 1.3.1.debian, an implementation of ANSI Common Lisp.
  More information about SBCL is available at <http://www.sbcl.org/>.

  SBCL is free software, provided as is, with absolutely no warranty.
  It is mostly in the public domain; some portions are provided under
  BSD-style licenses.  See the CREDITS and COPYING files in the
  distribution for more information.
  * (ql:quickload "lisp-binary")
  To load "lisp-binary":
    Load 1 ASDF system:
      lisp-binary
  ; Loading "lisp-binary"
  [package uiop/package]............................
  ..................................................
  ..................................................
  ..................................................
  ..................................................
  [package closer-mop]..............................
  [package closer-common-lisp]......................
  [package closer-common-lisp-user].................
  [package metabang.moptilities]....................
  [package impl-specific-gray]......................
  [package trivial-gray-streams]....................
  [package flexi-streams]...........................
  ..................................................
  ..................................................
  ..................................................
  ..................................................
  [package iterate].................................
  ..................................................
  [package quasiquote-2.0]..........................
  [package uiop/package]............................
  ..................................................
  ..................................................
  [package alexandria.0.dev]........................
  ..................................................
  [package babel-encodings].........................
  [package babel]...................................
  ..................................................
  [package cffi-sys]................................
  [package cffi]....................................
  ..................................................
  [package cffi-features]...........................
  [package lisp-binary-utils].......................
  [package lisp-binary/integer].....................
  [package lisp-binary/float].......................
  [package simple-bit-stream].......................
  [package reverse-stream]..........................
  [package lisp-binary].............................
  ...........
  ("lisp-binary")
  *



生成可独立执行文件
----------------

Lisp是脚本语言, 具备跨平台的特性. Ecl是一个开源的Lisp语言实现, 可以将lisp文件编译成独立可执行程序.

3.编译
 CL-USER> (setf c::*delete-files* nil)
 CL-USER> (compile-file "test.lisp" :system-p t)
 CL-USER> (c:build-program "test" :lisp-files '("test.o"))
4.执行
 #./test

5.github demo:https://github.com/cwndrws/lisp-c-example




