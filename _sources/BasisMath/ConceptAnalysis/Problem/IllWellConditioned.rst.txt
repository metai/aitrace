.. _Section-IllWellConditioned:

病态与良态
=====================

问题的病态与良态是根据 **问题输出随问题输入扰动的变化程度** 定义的, 这种扰动程度通过 **条件数** 来定义, 故先说明条件数的含义. 具有小条件数的问题是良态的, 相反, 具有大条件数的问题是病态的.

http://en.volupedia.org/wiki/Condition_number

条件数
---------------

.. _def-ConditionNumber:

.. proof:definition:: 条件数

    设有问题 :math:`f(x)` , 解算法 :math:`{\tilde f}(x)` 和输入 :math:`x` . 记输入的扰动(或误差)为 :math:`\delta x` 解的扰动(或误差)为 :math:`\delta f` , 则有绝对误差 :math:`||\delta f|| = ||f(x) - {\tilde f}(x)||` 和相对误差 :math:`||\delta f|| / ||f(x)||` .

    **绝对条件数** 定义为

    .. math::
        \lim_{\epsilon \to 0}\sup\limits_{||\delta x|| \le \epsilon} \frac{||\delta f(x)||}{||\delta x||}

    **相对条件数** 定义为

    .. math::
        \lim_{\epsilon \to 0}\sup\limits_{||\delta x|| \le \epsilon} \frac{||\delta f(x)||/||f(x)||}{||\delta x||/||x||}



病态的
-----------------------

病态的 ( :term:`Ill-conditioned` )





良态的
-----------------------

良态的 ( :term:`Well-conditioned` )