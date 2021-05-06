.. _Section-sshShellProgramingComputerScience:

ssh协议
=====================


常用命令
-------------------------


- 远程登录: ``ssh username@serverip``
- 远程拷贝文件: ``ssh username@serverip:remotefilepath localfilepath``
- 远程拷贝文件夹: ``ssh -r username@serverip:remotefolderpath localfolderpath``


.. hint:: 多机拷贝
   假设 A, B, C 等多台机器处于同一局域网, 可以使用上述命令共享数据.



