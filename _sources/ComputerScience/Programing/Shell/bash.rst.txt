.. _Section-bashShellProgramingComputerScience:

bash命令
=====================


常用命令
-------------------------

tee
~~~~~~~~


1. 只输出到屏幕: ``python main.py``
3. 只输出到文件(`log.log`): ``python main.py 2>&1 | tee >log.log`` 或 ``python main.py | tee >log.log``
1. 输出到屏幕和文件(`log.log`): ``python main.py |tee log.log``

