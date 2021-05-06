.. _Section-IntroductionJuliaProgramingComputerScience:

引言
=====================


什么是Julia语言
----------------



.. hint:: 资源链接

    - `Homepage of Julia <https://julialang.org/>`_
    - `Julia computing <https://juliacomputing.com/>`_
    - `Github of Julia <https://github.com/JuliaLang>`_
    - `Julia doc, en <https://docs.julialang.org/>`_
    - `Julia doc, zh <https://docs.juliacn.com/latest/>`_
    - `Julia doc, zh <https://julia-cn.readthedocs.io/>`_
    - `Julia By Example <https://juliabyexample.helpmanual.io/>`_



- `JuliaLang <https://github.com/JuliaLang>`_
- `JuliaIO <https://github.com/JuliaIO>`_ : MAT, HDF5,
- `JuliaPackaging <https://github.com/JuliaPackaging>`_ : BinaryBuilder, BinaryProvider,
- `JuliaOpt <https://github.com/JuliaOpt>`_ : JuMP, Convex, NLopt ..., see `juliaopt <http://juliaopt.org/>`_
- `JuliaNLSolvers <https://github.com/JuliaNLSolvers>`_ : Optim(Optimization), LsqFit(Curve Fitting), NLsolve(nonlinear equations), LineSearches
- `Flux <https://github.com/FluxML/Flux.jl>`_ : ``Pkg.add("Flux")``
- `ScikitLearn <https://github.com/cstjean/ScikitLearn.jl>`_ : ``Pkg.add("ScikitLearn")``
- `TensorFlow <https://github.com/malmaud/TensorFlow.jl>`_ : ``Pkg.add("TensorFlow")``



开发环境配置
----------------



安装Julia实现
~~~~~~~~~~~~~~~~~~~~~

安装包安装
^^^^^^^^^^^^^^^

Julia 的安装十分简单, 从 `主页 <https://julialang.org/>`_ 或者镜像站点下载对应操作系统版本的安装包. 对于Windows系统, 双击安装包根据提示安装即可; 对于Linux系统, 下载解压后将 ``bin`` 目录添加至系统环境变量 ``PATH`` 中即可. 添加好环境变量, 打开终端, 输入 ``julia`` 进入Julia交互式界面, 如 :figure:numref:`fig-WelcomJuliaWindowsUbuntu` 所示.


.. _fig-WelcomJuliaWindowsUbuntu:

.. figure:: ../../../_static/figs/ComputerScience/Programing/Julia/Introduction/WelcomJuliaWindowsUbuntu.*
   :alt: Welcome interface of Julia on Windows and Ubuntu
   :scale: 80 %
   :align: center

   Welcome interface of Julia on Windows and Ubuntu



源码安装
^^^^^^^^^^^^^^^

从 `github julia <https://github.com/JuliaLang/julia>`_ 或者镜像站点下载源码, 解压进入目录, 输入 ``make`` 构建生成可执行文件.


卸载Julia实现
~~~~~~~~~~~~~~~~~~~~~

直接删除安装目录和包目录 ``~/.julia`` 即可.



开发环境配置
~~~~~~~~~~~~~~~~~~~


Sublime 环境
^^^^^^^^^^^^^^^^^^^



如果想直接在Sublime中运行Julia程序, 可以添加Julia编译选项, 然后通过 :kbd:`Ctrl+b` 或 :kbd:`Ctrl+Shift+b` 选择编译. 具体方法为: 新建 :file:`sublime_rootdir/Packages/Users/Julia.sublime-build` 文件, 输入如下代码, 保存即可::

  {
      "cmd": ["julia", "$file"],
      "file_regex":"^(?:julia:)?[\t](...*?):([0-9]*):?([0-9]*)",
      "selector":"source.jl,source.julia"
  }



Julia编程入门
----------------

交互式界面使用
~~~~~~~~~~~~~~~





第一个Julia程序
~~~~~~~~~~~~~~~~~~~



第三方包管理
-----------------------------

Julia第三方库的安装很简单, 在Julia交互窗口执行 ``using Pkg; Pkg.add("PkgName")`` 即可安装; 或者按 :kbd:`]` 进入包管理器交互界面, 输入 ``add PkgName`` 安装. 以安装线性代数库为例, 安装记录见 :numref:code-block:`code-UsingPkgOfJulia`

.. code-block:: julia
    :lineno-start: 1
    :emphasize-lines: 1,14
    :linenos:
    :caption: Use julia's Pkg manager to install library
    :name: code-UsingPkgOfJulia

    julia> using Pkg; Pkg.add("LinearAlgebra")
       Updating registry at `~/.julia/registries/General`
    ┌ Warning: Some registries failed to update:
    │     — `~/.julia/registries/General` — registry dirty
    └ @ Pkg.Types /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.4/Pkg/src/Types.jl:1108
      Resolving package versions...
       Updating `~/.julia/environments/v1.4/Project.toml`
      [37e2e46d] + LinearAlgebra 
       Updating `~/.julia/environments/v1.4/Manifest.toml`
     [no changes]

    julia> 

    (@v1.4) pkg> add LinearAlgebra
      Resolving package versions...
       Updating `~/.julia/environments/v1.4/Project.toml`
      [37e2e46d] + LinearAlgebra 
       Updating `~/.julia/environments/v1.4/Manifest.toml`
     [no changes]

    (@v1.4) pkg> 





包库管理器Pkg
~~~~~~~~~~~~~~~~~~

- ``Pkg.add("PkgName")``
- ``Pkg.rm("PkgName")``
- ``Pkg.up("PkgName")``


设置包下载镜像
~~~~~~~~~~~~~~~~~~~~~

中国国内镜像站点有:

- `USTC <https://mirrors.ustc.edu.cn/>`_
- `ZJU <https://mirrors.zju.edu.cn/>`_

这里介绍使用 ``PkgMirrors`` 包来选择安装源镜像. 如果你已经使用了GitHub源, 可以进入 ``.julia`` 目录, 删除 ``General`` 目录, 然后按如下提示注册国内源

::

  julia> # Type "]" to enter Pkg REPL-mode.

  # If you have a clean Julia environment, you can initialize the General registry (where you the packages are registered) by using:
  (v1.1) pkg> registry add https://mirrors.zju.edu.cn/julia/registries/General.git

  # Install this package from the mirror:
  (v1.1) pkg> add https://mirrors.zju.edu.cn/julia/PkgMirrors.jl.git#v1.3.0


终端输入 ``julia`` 进入交互界面, 输入 ``using Pkg; Pkg.add("PkgMirrors")`` 安装, 输入 ``PkgMirrors.setmirror("MIRRORNAME")`` 选择源, 其中, ``MIRRORNAME`` 为镜像源名称, 中国境内可用的有 ``ZJU``, ``USTC``. 重新导入 ``import PkgMirrors`` 以激活, 继续输入 ``update`` 可以更新, 还可以输入 ``PkgMirrors.deactivate()`` 取消激活, 输入 ``PkgMirrors.clear()``   清空缓存.

::

  import PkgMirrors









生成可独立执行文件
----------------





问题与解决
----------------------


curl: (51) SSL: certificate subject name (ubuntu) does not match target host namERROR: Unable to automatically install 



add https://github.com/JuliaLang/PackageCompiler.jl



