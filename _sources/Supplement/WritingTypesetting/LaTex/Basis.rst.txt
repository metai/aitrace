.. _Section-BasisLaTexWritingTypesettingSupplemental:

LaTex基础
=====================

- `latex writing <https://www.andy-roberts.net/writing/latex>`_


数学相关
-----------------

定义定理证明等
~~~~~~~~~~~~~

导言区加入:

- ``\newtheorem{环境名}{自定义标题}[主计数器]``
   - ``\newtheorem{theorem}{myTheorem}[Chapter]``
   - ``\newtheorem{theorem}{\hspace{2em}定理}[Chapter]``
- ``\newtheorem{环境名}{自定义标题}[主计数器]``


正文中引用:

::

   \begin{theorem}
   This is a theorem
   \end{theorem}


.. latex::
   \begin{theorem}
   This is a theorem
   \end{theorem}
