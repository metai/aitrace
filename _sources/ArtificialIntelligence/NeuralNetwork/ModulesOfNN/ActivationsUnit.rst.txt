.. _Section-ActivationsUnit:

激活函数单元
=====================

什么是激活函数
------------------


为什么要有激活函数
------------------



经典激活函数分类
------------------

- 参考文档
   - `CS2131N: Commonly used activation functions <http://cs231n.github.io/neural-networks-1/>`_
   - `激活函数(ReLU, Swish, Maxout) <https://www.cnblogs.com/makefile/p/activation-function.html>`_


.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/Activations_ZoomOut.png
   :scale: 80%
   :alt: Activations函数图像
   :align: center

   Activations函数图像

   Activations函数图像


思维导图补充

恒等函数
~~~~~~~~

- 函数表达式: :math:`y = x`
- 函数特性: 线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/linear.png
   :scale: 80%
   :alt: 恒等函数图像
   :align: center

   恒等函数图像

   恒等函数图像, 线性函数.



tanh
~~~~~~~~

- `tanh, sinh, cosh <http://en.volupedia.org/wiki/Hyperbolic_function#Tanh>`_
- 函数表达式: :math:`y = {\rm tanh}(x) = {{e^{2x} - 1} \over {e^{2x} + 1}}`
- 函数特性: 非线性, 存在梯度弥散

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/tanh.png
   :scale: 80%
   :alt: tanh函数图像
   :align: center

   tanh函数图像

   tanh函数图像, 非线性函数.


Sigmoid
~~~~~~~~

- `sigmoid <http://en.volupedia.org/wiki/Sigmoid_function>`_
- 函数表达式: :math:`y = {e^x \over {e^x + 1}}`
- 函数特性: 非线性, 存在梯度弥散

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/sigmoid.png
   :scale: 80%
   :alt: Sigmoid函数图像
   :align: center

   Sigmoid函数图像

   Sigmoid函数图像, 非线性函数.


softplus
~~~~~~~~

- 函数表达式: :math:`{\rm log}(e^x + 1)`
- 函数特性: 非线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/softplus.png
   :scale: 80%
   :alt: tanh函数图像
   :align: center

   softplus函数图像

   softplus函数图像, 非线性函数.

softsign
~~~~~~~~

- 函数表达式: :math:`\frac{x} {({\rm abs}(x) + 1)}`
- 函数特性: 非线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/softsign.png
   :scale: 80%
   :alt: tanh函数图像
   :align: center

   softsign函数图像

   softsign函数图像, 非线性函数.

elu
~~~~~~~~

- 函数表达式: :math:`y = \left\{ {\begin{array}{ccc}{x,\;\;\;\;\;\;\;\;\;x \ge 0}\\{{e^x} - 1,\;\;\;x < 0}\end{array}} \right.`
- 函数特性: 非线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/elu.png
   :scale: 80%
   :alt: elu函数图像
   :align: center

   elu函数图像

   elu函数图像, 非线性函数.

relu
~~~~~~~~

- 函数表达式: :math:`{\rm max}(x, 0)`
- 函数特性: 非线性+线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/relu.png
   :scale: 80%
   :alt: relu函数图像
   :align: center

   relu函数图像

   relu函数图像, 非线性函数.

relu6
~~~~~~~~

- `Convolutional Deep Belief Networks on CIFAR-10. A. Krizhevsky <http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf>`_
- 函数表达式: :math:`{\rm min}({\rm max}(x, 0), 6)`
- 函数特性: 非线性+线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/relu6.png
   :scale: 80%
   :alt: relu6函数图像
   :align: center

   relu6函数图像

   relu6函数图像, 非线性函数.


leaky relu
~~~~~~~~~~~

- `"Rectifier Nonlinearities Improve Neural Network Acoustic Models" AL Maas, AY Hannun, AY Ng - Proc. ICML, 2013 <http://web.stanford.edu/~awni/papers/relu_hybrid_icml2013_final.pdf>`_
- 函数表达式: :math:`y = \left\{ {\begin{array}{ccc}{x,\;\;\;\;\;\;x \ge 0}\\{\alpha x,\;\;\;x < 0}\end{array}} \right.`
- 函数特性: 非线性+线性

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/leaky_relu.png
   :scale: 80%
   :alt: leaky relu函数图像
   :align: center

   leaky relu函数图像

   leaky relu函数图像, 非线性函数.

selu
~~~~~~~~

- `Self-Normalizing Neural Networks <https://arxiv.org/abs/1706.02515>`_
- 函数表达式: :math:`y = \lambda \left\{ {\begin{array}{ccc}{x,\;\;\;\;\;\;\;\;\;\;\;\;\;x \ge 0}\\{\alpha ({e^x} - 1),\;\;\;\;x < 0}\end{array}} \right.`
- 函数特性: 非线性, 自归一化

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/selu.png
   :scale: 80%
   :alt: selu函数图像
   :align: center

   selu函数图像

   selu函数图像, 非线性函数.


crelu
~~~~~~~~

- `Understanding and Improving Convolutional Neural Networks via Concatenated Rectified Linear Units. W. Shang, et al. <https://arxiv.org/abs/1603.05201>`_
- 函数表达式: :math:`y = e^x \over (e^x + 1)`
- 函数特性: 非线性, 存在梯度弥散


.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/crelu.png
   :scale: 80%
   :alt: crelu函数图像
   :align: center

   crelu函数图像

   crelu函数图像, 非线性函数.


Swish
~~~~~~~~~

- `Searching for Activation Functions" (Ramachandran et al. 2017) <https://arxiv.org/abs/1710.05941>`_
- 函数表达式: :math:`y = x\cdot {\rm sigmoid}(\beta x) = {e^{(\beta x)} \over {e^{(\beta x)} + 1}} \cdot x`
- 函数特性: 非线性, 存在梯度弥散

.. figure:: ../../../_static/figs/ArtificialIntelligence/NeuralNetwork/ModulesOfNN/Activations/swish.png
   :scale: 80%
   :alt: Swish函数图像
   :align: center

   Swish函数图像

   Swish函数图像, 非线性函数.




新颖激活函数
------------------




