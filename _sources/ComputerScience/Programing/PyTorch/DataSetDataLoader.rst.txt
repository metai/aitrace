.. _Section-DataSetDataLoaderPytorchProgramingComputerScience:

数据集制作与加载
=====================


借助 Torch 提供的 DataSet 和 DataLoader 类实现自定义数据集的制作与加载.


DataSet
-------------

数据集有以下几个类

- ``Dataset()``: 无输入参数
- ``TensorDataset(*tensors)``: 将多个``Tensor``做成一个数据集, 输入为多个``Tensors``
- ``ConcatDataset(datasets)``: 将多个数据集拼成一个数据集,输入为多个数据集
- ``Subset(dataset, indices)``: 取数据集的子集, 输入为数据集与索引


使用 Dataset
~~~~~~~~~~~~~~~~~~~

需要重写该类的 ``__len__``, ``__getitem__``, ``__init__`` 方法. 下面举例说明, 假设网络含两个输入 :math:`x_1, x_2`, 一个输出 :math:`y`, 构造 ``MyDataset`` 类, 实现代码为


.. literalinclude:: ../../../_static/src/PyTorch/DataSets/demo_DatasetDataLoader.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 19,21,28,31,34,36
   :linenos:
   :caption: demo_DatasetDataLoader.py
   :name: bind-id


使用 TensorDataset
~~~~~~~~~~~~~~~~~~~

TensorDataset 类的使用非常简单, 省去了重写类方法的麻烦, 下面举例说明, 假设网络含两个输入 :math:`x_1, x_2`, 一个输出 :math:`y`, 构造 ``MyDataset`` 类, 实现代码为

.. literalinclude:: ../../../_static/src/PyTorch/DataSets/demo_TensorDatasetDataLoader.py
   :language: python
   :encoding: latin-1
   :emphasize-lines: 18, 20
   :linenos:
   :caption: demo_TensorDatasetDataLoader.py
   :name: bind-id


DataLoader
-------------





