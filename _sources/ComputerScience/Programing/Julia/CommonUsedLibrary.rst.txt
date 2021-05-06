.. _Section-CommonUsedLibraryJuliaProgramingComputerScience:

常用依赖库
=====================


基础库
------------------


构建编译
~~~~~~~~~~~~~~

CMake
^^^^^^^^^^^

使用命令 ``add CMake`` 即可安装, 本书作者在安装过程中提示如下错误::

    (@v1.4) pkg> add CMake
      Resolving package versions...
      Installed CMake ─ v1.2.0
       Updating `~/.juliapro/JuliaPro_v1.4.0-1/environments/v1.4/Project.toml`
      [631607c0] + CMake v1.2.0
       Updating `~/.juliapro/JuliaPro_v1.4.0-1/environments/v1.4/Manifest.toml`
     [no changes]
       Building CMake → `~/.juliapro/JuliaPro_v1.4.0-1/packages/CMake/ULbyn/deps/build.log`
    ┌ Error: Error building `CMake`: 
    │   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
    │                                  Dload  Upload   Total   Spent    Left  Speed
    100   607  100   607    0     0    338      0  0:00:01  0:00:01 --:--:--   337
      0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
    │ curl: (51) SSL: certificate subject name (ubuntu) does not match target host name 'github-production-release-asset-2e65be.s3.amazonaws.com'
    │ [ Info: Attempting to create directory /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/CMake/ULbyn/deps/downloads
    │ [ Info: Downloading file https://github.com/Kitware/CMake/releases/download/v3.15.3/cmake-3.15.3.tar.gz
    │ ERROR: LoadError: failed process: Process(`curl -f -o /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/CMake/ULbyn/deps/downloads/cmake-3.15.3.tar.gz -L https://github.com/Kitware/CMake/releases/download/v3.15.3/cmake-3.15.3.tar.gz`, ProcessExited(51)) [51]
    │ 
    │ Stacktrace:
    │  [1] pipeline_error at ./process.jl:525 [inlined]
    │  [2] run(::Cmd; wait::Bool) at ./process.jl:440
    │  [3] run(::Cmd) at ./process.jl:438
    │  [4] run(::BinDeps.SynchronousStepCollection) at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/BinDeps/eiJeV/src/BinDeps.jl:524
    │  [5] run(::FileRule) at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/BinDeps/eiJeV/src/BinDeps.jl:486
    │  [6] run(::BinDeps.SynchronousStepCollection) at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/BinDeps/eiJeV/src/BinDeps.jl:524
    │  [7] run(::FileRule) at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/BinDeps/eiJeV/src/BinDeps.jl:486
    │  [8] run(::BinDeps.SynchronousStepCollection) at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/BinDeps/eiJeV/src/BinDeps.jl:524
    │  [9] top-level scope at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/CMake/ULbyn/deps/build.jl:158
    │  [10] include(::String) at ./client.jl:439
    │  [11] top-level scope at none:5
    │ in expression starting at /home/liu/.juliapro/JuliaPro_v1.4.0-1/packages/CMake/ULbyn/deps/build.jl:158
    └ @ Pkg.Operations /home/buildbot/build-worker/worker/juliapro-release-centos7-0_6/build/tmp_julia/share/julia/stdlib/v1.4/Pkg/src/Operations.jl:892

根据错误提示可知, 证书名不匹配, 所以无法下载文件 ``cmake-3.15.3.tar.gz``, 故手动下载该文件, 并放在目录 `downloads` 目录下, 执行 ``build CMake`` 命令即可. 构建完成后, 输入 ``using CMake`` 若无错误提示, 则证明安装成功.

.. hint::
   在下面的安装过程中出现类似错误均可通过自行下载解决. 如在安装 ``HDF5`` 时, 可能需要自行下载 `HDF5, Zlib, Blosc`.


IO库
~~~~~~~~~~~~~~


在安装本节提及的库时, 可能会用到上一节中的库, 故建议先安装上一节中的库.


HDF5
^^^^^^^^^^^^

执行 ``using Pkg; Pkg.add("HDF5")`` 即可, 若出现文件无法下载的情况, 可参考 ``CMake`` 部分的解决方法, 以下不再赘述.


MAT
^^^^^^^^^^^^

Julia交互窗口执行 ``using Pkg; Pkg.add("MAT")`` 即可安装, 或者按 :kbd:`]` 进入包管理器交互界面, 执行 ``add MAT`` 即可安装.


科学计算库
------------------







