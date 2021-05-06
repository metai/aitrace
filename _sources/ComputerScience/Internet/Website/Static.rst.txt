.. _Section-StaticWebsite:

静态网站
=====================


Jekyll 工具
----------------

`Jekyll <http://jekyllcn.com/>`_ 是一个将纯文本转换为静态博客网站的工具.

安装
~~~~~~~~

1. 安装 `Ruby <http://www.ruby-lang.org/en/>`_
2. 安装Jekyll和bundler

Ruby安装
^^^^^^^^^

Ubuntu下执行: ``sudo apt-get intall ruby ruby-dev`` 命令安装, 若所安装版本<2.4, 可通过下述源码方式安装.

从 `这里 <http://www.ruby-lang.org/en/downloads/>`_ 下载源码包, 解压并进入目录后执行: ::

    ./configure
    make
    sudo make install

.. hint:: 若需要修改安装路径, 执行 ``./configure --prefix=DIR``.


安装Jekyll和bundler
^^^^^^^^^^^^^^^^^^^

执行 ``sudo gem install jekyll bundler``, ``bundle update`` 安装即可.



使用
~~~~~~~~~~~~~~~

安裝其它库
^^^^^^^^^^^^^

- 安装: ``gem install libname --version 0.7.0``
- 卸载: ``gem uninstall libname``


安装主题
^^^^^^^^^^^^


以安装 ``jekyll-theme-dinky`` 主题为例, 输入 ``gem install jekyll-theme-dinky`` 即可自动安装. 最后, 向站点的 `_config.yml` 文件中加入下列代码来启用主题: ``theme: jekyll-theme-dinky``.


一个例子
~~~~~~~~


1. 创建新的站点: ``jekyll new myblog``
2. 进入站点目录: ``cd myblog``
3. 安装Gem依赖: ``bundle install``
4. 构建站点: ``bundle exec jekyll serve``
5. 构建站点: ``bundle exec jekyll build --trace --incremental``


.. hint::
   - 使用 ``bundle install`` 安装依赖
   - 使用 ``bundle update`` 解决版本不一致
   - 使用 ``bundle exec xxx`` 执行, 解决版本不一致
