.. _Section-SupportVectorMachine:

支撑矢量机
=====================

**支撑矢量机** (:term:`Support Vector Machine`) 也称支持向量机, Vladimir N. Vapnik and Alexey Ya. Chervonenkis等人于1963年提出一种通过将核技巧应用于最大边缘超平面(maximum-margin hyperplanes)来创建非线性分类器的方法. 现今使用最多的标准的SVM是由 Corinna Cortes and Vapnik 等人于1993年提出并于1995年出版的 :cite:`Cortes.1995` .

假设有训练样本集 :math:`{\mathbb S} = \{({\bm x}_i, {\bm y}_i)\}_{i=1}^N` , SVM的优化问题为

.. math::
	\begin{array}{c}{\text { ninimize } \frac{1}{2} \|\bm{w}\|^2 + C \sum_{i=1}^{N} \xi_{i}} \\ {\text { subject to } y_{i}\left(\bm{w} \cdot \bm{z}_{i}+b\right) \geq 1-\xi_{i}, \quad i=1, \ldots, N} \\ {\xi_{i} \geq 0, \quad i=1, \ldots, N}\end{array},
	:label: equ-SVM_problem

其中, :math:`{\bm w}` 为模型参数, :math:`C` 为平衡因子, :math:`\xi_i` 为第 :math:`i` 个样本对应误差, :math:`{\bm z}_i` 为第 :math:`i` 个样本 :math:`{\bm x}_i` 在特征空间中的象 :math:`{\bm z}_i = f({\bm x}_i)` , :math:`f: {\mathbb R}^n \rightarrow {\mathbb R}^m` .

SVM中的参数 :math:`C` 用于平衡最大边缘(margin)和错分的数量, 大的 :math:`C` 使得训练的SVM具有窄的边缘和减少错分; 减小 :math:`C` 使得SVM忽略更多训练样本, 分类边缘更宽.









- `libsvm <http://www.csie.ntu.edu.tw/~cjlin/libsvm/>`_ : a popular library of SVM learners
- `liblinear <http://www.csie.ntu.edu.tw/~cjlin/liblinear/>`_ : a library for large linear classification including some SVMs
- `SVM light <http://svmlight.joachims.org/>`_ a collection of software tools for learning and classification using SVM
- `SVMJS live demo <http://cs.stanford.edu/people/karpathy/svmjs/demo/>`_ a GUI demo for JavaScript implementation of SVMs



