.. _Section-ProbSolveLaTexWritingTypesettingSupplemental:


问题解决
================

安装
----------------

使用
---------------


~~~~~~~~~~~~~~

Extra alignment tab has been changed to \cr
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

提示如下错误: ::

    Extra alignment tab has been changed to \cr. [\end{array}} \right]\end{split}]

查看报错行源码发现, 矩阵实际为4列, 然而只指定了3列的参数( ``ccc`` ): ::

    \begin{equation*}
    \begin{split}{\bm A} = \left[ {\begin{array}{ccc}
    {{a_{11}}}&{{a_{12}}}& \cdots &{{a_{1n}}}\\
    {{a_{21}}}&{{a_{22}}}& \cdots &{{a_{2n}}}\\
     \vdots & \vdots & \ddots & \vdots \\
    {{a_{n1}}}&{{a_{n2}}}& \cdots &{{a_{nn}}}
    \end{array}} \right]\end{split}
    \end{equation*}

将 ``ccc`` 改为 ``cccc`` 即可.