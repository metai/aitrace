.. _Section-GetStartedPyTorchProgramingComputerScience:

从这里开始
=====================


安装
----------------

在线安装
~~~~~~~~~~~~

参考 `START LOCALLY <https://pytorch.org/get-started/locally/>`_ , 选择环境, 执行安装命令即可.

``conda install pytorch torchvision cudatoolkit=9.0 -c pytorch``


本地安装包安装
~~~~~~~~~~~~


Anaconda
^^^^^^^^^^


``conda install --use-local ./pytorch-1.1.0-py3.7_cuda9.0.176_cudnn7.5.1_0.tar.bz2 -c pytorch``
``conda install torchvision cudatoolkit=9.0 -c pytorch``


Python
^^^^^^^^^^^

从 `pypi <https://pypi.org/>`_ 下载对应版本的安装包, 执行 ``pip install`` 命令安装即可, 如

::

    sudo pip3 install torch-1.1.0-cp35-cp35m-manylinux1_x86_64.whl
    sudo pip3 install torchvision


本地源码安装
~~~~~~~~~~~~~~~~

Pytorch
^^^^^^^^^^

Pytorch的源码安装并不复杂, 与其它深度学习平台的源码安装过程相比, 极为简单, 具体可参考 `pytorch from source <https://github.com/pytorch/pytorch#from-source>`_.


.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption: Pytorch 源码安装
    :name: bind-id

    conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing

    # Add LAPACK support for the GPU if needed
    conda install -c pytorch magma-cuda90 # or [magma-cuda80 | magma-cuda91] depending on your cuda version

    git clone --recursive https://github.com/pytorch/pytorch
    cd pytorch

    export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
    python setup.py install


Torchvision
^^^^^^^^^^^^^^

torchvision的源码安装也非常简单, 进入torchvision根目录, 执行 ``python setup.py install`` 即可, 具体可参考 `torchvision from source <https://github.com/pytorch/vision>`_.




构建本地文档
------------------

API手册
~~~~~~~~~~~

Pytorch
^^^^^^^^^^

Sphinx格式文档, 执行如下命令即可生成 html 与 epub 格式的文档

.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption: 构建Pytorch文档
    :name: bind-id

    cd docs/
    pip install -r requirements.txt

    make html
    make epub


Torchvision
^^^^^^^^^^^^^^

Sphinx格式文档, 执行如下命令即可生成 html 与 epub 格式的文档


.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption: 构建Torchvision文档
    :name: bind-id

    cd docs/
    pip install -r requirements.txt

    make html
    make epub


问题与解决
------------------

安装
~~~~~~~~


PyQt
^^^^^^^


.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption: 构建Torchvision文档
    :name: bind-id

    ImportError: anaconda3/lib/python3.6/site-packages/PyQt5/../../../libQt5Core.so.5: version `Qt_5.9' not found (required by /home/liu/anaconda3/lib/python3.6/site-packages/PyQt5/QtCore.so)

matplotlib 绘图使用 PyQt, 需要安装该库, 通过 ``pip install PyQt`` 安装即可.




使用
~~~~~~~



Torch导入错误1
^^^^^^^^^^^^^^

无论是通过Anaconda还是pip安装完毕PyTorch后, 在Python解释器中导入torch( ``import torch`` )均会报出如下错误: ::

    from torch._C import * ImportError: libcurand.so.8.0: cannot open shared object file

系统为 Ubuntu16.04LTS, Python3.5, Python3.7(Anaconda), CUDA9.0 和 CUDA8.0 共存. 安装前环境已经切换为 CUDA9.0, 上述错误提示找不到 CUDA8.0 相关文件, 因而怀疑一些编译的库使用的是CUDA8.0. 最终发现是之前安装的 ``caffe2`` 的影响, 导致 PyTorch 中的cafe2不能正确安装, 卸载之前安装的 caffe2, 问题解决.


Torch导入错误2
^^^^^^^^^^^^^^^

安装没有问题, 导入时提示如下错误信息

.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption:
    :name: bind-id

    python
    import torch
    # 提示如下错误信息
    ModuleNotFoundError: No module named 'torch._C'

在另一个不含torch的目录使用即可解决该问题.


Torchvision导入失败
^^^^^^^^^^^^^^^^^^^

可能没安装或者安装失败，请注意环境，如果是 conda环境，要在相应环境下执行，如果不是，要退出conda环境。

.. code-block:: bash
    :lineno-start: 1
    :emphasize-lines: 1,4
    :linenos:
    :caption:
    :name: bind-id

    >>> import torch
    >>> import torchvision
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'torchvision'