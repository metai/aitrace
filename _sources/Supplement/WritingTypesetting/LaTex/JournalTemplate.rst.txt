.. _Section-JournalTemplateLaTexWritingTypesettingSupplemental:

Journal Template
=====================


IEEE Access
----------------

模板获取与编译
~~~~~~~~~~~~~~~~

从 `这里 <url>`_ 下载模板, 解压后编译提示如下错误::

    Package pdftex.def Error: File `Logo.png' not found. []
    Package pdftex.def Error: File `notaglineLogo.png' not found. []

可是文件夹中明明是有这两个文件, 而且在 Windows 系统上编译可以通过, 仔细观察可以发现, 图片文件名与实际文件名大小写不一致, 在Ubuntu等Linux系统上是区分大小写的, 而Windows则不然.



