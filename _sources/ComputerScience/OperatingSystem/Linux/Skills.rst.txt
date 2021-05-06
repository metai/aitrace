.. _Section-SkillsLinuxOperationSystemComputerScience:

常用技巧
=====================



第三方工具
-------------------------



.. _SubSubSection-MultiThreadDownload:

多线程下载
~~~~~~~~~~~~~~~~

Ubuntu下可用的多线程下载工具有 `aria2c <http://aria2.github.io/>`_, `uget <https://ugetdm.com/>`_, `axel <https://wiki.ubuntu.org.cn/Axel>`_ 等等, 且支持断点续传. 这里介绍使用 aria2c 多线程下载需要用户名密码认证的文件, 以下载 `ERS雷达数据 <https://www.asf.alaska.edu/>`_ 为例, 对于单个文件可以使用

.. code-block:: bash
   :caption: 下载单个文件
   :linenos:
   :emphasize-lines: 2,5

   # 无需认证下载
   aria2c -x 16 downloadlink

   # 需要认证
   aria2c -x 16 -p --http-user=$yourusername --http-passwd=$yourpasswd downloadlink


对于多个文件, 可以自己写个脚本逐个下载, 新建 `urls` 文件, 添加文件下载链接(每行代表一个下载链接), 如下 ::


    https://datapool.asf.alaska.edu/L0/E2/E2_84699_STD_L0_F303.zip
    https://datapool.asf.alaska.edu/L1/E2/E2_84699_STD_F303.zip
    https://datapool.asf.alaska.edu/L0/E2/E2_84699_STD_L0_F301.zip
    https://datapool.asf.alaska.edu/L1/E2/E2_84699_STD_F301.zip
    https://datapool.asf.alaska.edu/L1/E2/E2_84690_STD_F137.zip
    https://datapool.asf.alaska.edu/L0/E2/E2_84690_STD_L0_F137.zip
    https://datapool.asf.alaska.edu/L1/E2/E2_84686_STD_F203.zip
    https://datapool.asf.alaska.edu/L0/E2/E2_84686_STD_L0_F203.zip
    https://datapool.asf.alaska.edu/L1/E2/E2_84697_STD_F273.zip
    https://datapool.asf.alaska.edu/L0/E2/E2_84697_STD_L0_F273.zip
    https://datapool.asf.alaska.edu/L0/R1/R1_65200_ST1_L0_F301.zip
    https://datapool.asf.alaska.edu/L1/R1/R1_65200_ST1_F301.zip


新建 `download.sh` 文件, 添加如下代码, 执行 ``./download.sh``, 即可实现从 `urls` 文件中读取每个文件的下载链接, 逐个下载.


.. code-block:: bash
   :caption: 下载单个文件
   :linenos:
   :emphasize-lines: 15

   #!/bin/bash

   # 1-16 -x, --max-connection-per-server=NUM The maximum number of connections to one for each download.
   thread=16

   FILE=urls
   yourusername=[username]
   yourpasswd=[passwd]

   echo "################################"
   k=1
   while read line;do
        echo "Line # $k: $line"

        aria2c -x $thread -p --http-user=$yourusername --http-passwd=$yourpasswd $line

        ((k++))
   done < $FILE
   echo "$k files are downloaded!"





