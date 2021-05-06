.. _Section-LuaNotesLuaProgramingComputerScience:

Lua笔记
=====================


Lua相关资料
-------------------------

基础
~~~~~~~~~~~~~~~~~~

-  `Lua官网 <http://www.lua.org>`_
-  `Lua Users <http://lua-users.org/>`_
-  `Lua 5.3 英文参考手册 <http://www.lua.org/manual/5.3/manual.html>`_
-  `Lua 5.3 中文参考手册 <http://www.lua.org/manual/5.3/manual.html>`_
-  `Programming in Lua <http://vdisk.weibo.com/s/z63ACRNxK4cLS?sudaref=www.baidu.com>`_

从这里开始
--------------------

在类Unix系统上 (Linux、OSMax等等) , 可能已经安装了Lua, 或者有可用的安装包; 对于Windows可以使用\ `LuaDist <http://luadist.org/>`__\ 等发布的预编译包.

由于Lua开源, 所以还有另外一种安装方法: 通过源码安装, 分构建和安装两步完成.

类Unix系统
~~~~~~~~~~~~~~~~~~~~~

-  **构建Lua (Build Lua) **
   Lua在类Unix系统上的构建很简单, 输入\ ``make + 平台名``\ 即可, 如Linux平台下:

   .. code:: bash

       make linux

-  **安装Lua (Install Lua) ** 通过以下命令即可安装至默认位置.

   .. code:: bash

       make install

Windows
~~~~~~~~~~~~~~~~~~~~~~~

Windows下的构建过程稍微复杂一些, 看到两种方案都挺好, 大同小异.

1. 参考Lua官网给出的Wiki上的文章\ `Building Lua In Windows For
   Newbies <http://lua-users.org/wiki/BuildingLuaInWindowsForNewbies>`__\ 很容易实现, 基本上需要两样工具, 一是Lua源码, 二是编译工具TDM-GCC.
2. 参照\ `这里 <http://www.thijsschreijer.nl/blog/?p=863>`__\ , 需要安装MinGW, 文中还给出了LuaRocks的安装流程.

方法一
^^^^^^^^^^^^^^^^^^^

**构建Lua**

-  安装GCC编译器
   TDM-GCC的安装参照\ `这里 <http://blog.csdn.net/enjoyyl/article/details/46545263#tdm-gccgccg>`__\ .

-  新建一个名为\ **lua-gcc-Install**\ 的文件夹, 在里面新建文本文档, 命名为\ **buil.cmd**\ , 将下面的代码复制到该文件中, 注意更改你的编译器路径
   和 lua版本.

.. code:: cmd

    @echo off
    :: ========================
    :: file build.cmd
    :: ========================
    setlocal
    :: you may change the following variable's value
    :: to suit the downloaded version
    set lua_version=5.3.2

    set work_dir=%~dp0
    :: Removes trailing backslash
    :: to enhance readability in the following steps
    set work_dir=%work_dir:~0,-1%
    set lua_install_dir=%work_dir%\lua
    set compiler_bin_dir=E:\devtools\TDM-GCC-64\bin
    set lua_build_dir=%work_dir%\lua-%lua_version%
    set path=%compiler_bin_dir%;%path%

    cd /D %lua_build_dir%
    mingw32-make PLAT=mingw

    echo.
    echo **** COMPILATION TERMINATED ****
    echo.
    echo **** BUILDING BINARY DISTRIBUTION ****
    echo.

    :: create a clean "binary" installation
    mkdir %lua_install_dir%
    mkdir %lua_install_dir%\doc
    mkdir %lua_install_dir%\bin
    mkdir %lua_install_dir%\include

    copy %lua_build_dir%\doc\*.* %lua_install_dir%\doc\*.*
    copy %lua_build_dir%\src\*.exe %lua_install_dir%\bin\*.*
    copy %lua_build_dir%\src\*.dll %lua_install_dir%\bin\*.*
    copy %lua_build_dir%\src\luaconf.h %lua_install_dir%\include\*.*
    copy %lua_build_dir%\src\lua.h %lua_install_dir%\include\*.*
    copy %lua_build_dir%\src\lualib.h %lua_install_dir%\include\*.*
    copy %lua_build_dir%\src\lauxlib.h %lua_install_dir%\include\*.*
    copy %lua_build_dir%\src\lua.hpp %lua_install_dir%\include\*.*

    echo.
    echo **** BINARY DISTRIBUTION BUILT ****
    echo.

    %lua_install_dir%\bin\lua.exe -e"print [[Hello!]];print[[Simple Lua test successful!!!]]"

    echo.

    pause

-  将解压后的lua源码文件放入\ **lua-gcc-install**\ 文件夹中, 运行\ **build.cmd**\ 文件, 等待提示完成即可看到\ **lua-gcc-install**\ 文件夹下多了一个\ **lua**\ 文件夹 (\ **bin**\ 子文件夹下包含了需要的文件) , 如下图所示:
   |这里写图片描述|

**安装Lua**
将上述构建的文件 (\ **bin**\ 下的文件) 复制到你的安装目录, 并添加路径至PATH环境变量即可.
**注: **\ 由于是用GCC编译生成的, 所以在其它木有GCC的平台上是不能运行的.

方法2
^^^^^^^^^^^^^^^^^^^^

参考\ `Installing Lua on a Windows
system <http://www.thijsschreijer.nl/blog/?p=863>`__\ , 包含以下内容:

1. install a compiler (`MinGW (and
   MSYS) <http://www.mingw.org/wiki/Getting_Started>`__)
2. compile and install `Lua <http://www.lua.org>`__
3. install `LuaRocks <http://www.luarocks.org/>`__

**install a compiler ([MinGW (and MSYS)]**

这里, 我用的\ `MinGW <http://www.mingw.org/>`__\ 中的GCC版本为4.8.1, 且安装在“E:”目录下, 所以添加: \ ``E:\devtools\MinGw\bin;``\ 到系统环境变量PATH.

**compile and install Lua**

去\ `Lua <http://www.lua.org>`__\ 下载Lua源码, 我用的Lua5.3.2, 解压到任意路径, 如: "E:-5.3.2", 然后以管理员身份打开**命令提示符 (管理员) **\ , 输入如下指令:

.. code:: cmd

    SET PATH=%PATH%;E:\devtools\MinGW\msys\1.0\bin
    cd /d E:\lua-5.3.2
    make clean
    make mingw
    make install INSTALL_TOP=E:/devtools/lua/5.3 TO_BIN="lua.exe luac.exe lua53.dll"

输出结果类似这样:

.. code:: cmd

    C:\windows\system32>>SET PATH=%PATH%;E:\devtools\MinGW\msys\1.0\bin

    C:\windows\system32>cd /d E:\lua-5.3.2

    E:\lua-5.3.2>make clean
    cd src && make clean
    make[1]: Entering directory `/e/lua-5.3.2/src'
    rm -f liblua.a lua luac lapi.o lcode.o lctype.o ldebug.o ldo.o ldump.o lfunc.o lgc.o llex.o lmem.o lobject.o lopcodes.o lparser.o lstate.o lstring.o ltable.o ltm.o lundump.o lvm.o lzio.o lauxlib.o lbaselib.o lbitlib.o lcorolib.o ldblib.o liolib.o lmathlib.o loslib.o lstrlib.o ltablib.o lutf8lib.o loadlib.o linit.o  lua.o luac.o
    make[1]: Leaving directory `/e/lua-5.3.2/src'

    E:\lua-5.3.2>make mingw
    cd src && make mingw
    make[1]: Entering directory `/e/lua-5.3.2/src'
    make "LUA_A=lua53.dll" "LUA_T=lua.exe" \
            "AR=gcc -std=gnu99 -shared -o" "RANLIB=strip --strip-unneeded" \
            "SYSCFLAGS=-DLUA_BUILD_AS_DLL" "SYSLIBS=" "SYSLDFLAGS=-s" lua.exe
    make[2]: Entering directory `/e/lua-5.3.2/src'
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lua.o lua.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lapi.o lapi.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lcode.o lcode.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lctype.o lctype.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ldebug.o ldebug.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ldo.o ldo.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ldump.o ldump.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lfunc.o lfunc.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lgc.o lgc.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o llex.o llex.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lmem.o lmem.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lobject.o lobject.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lopcodes.o lopcodes.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lparser.o lparser.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lstate.o lstate.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lstring.o lstring.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ltable.o ltable.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ltm.o ltm.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lundump.o lundump.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lvm.o lvm.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lzio.o lzio.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lauxlib.o lauxlib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lbaselib.o lbaselib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lbitlib.o lbitlib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lcorolib.o lcorolib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ldblib.o ldblib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o liolib.o liolib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lmathlib.o lmathlib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o loslib.o loslib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lstrlib.o lstrlib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o ltablib.o ltablib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o lutf8lib.o lutf8lib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o loadlib.o loadlib.c
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2 -DLUA_BUILD_AS_DLL    -c -o linit.o linit.c
    gcc -std=gnu99 -shared -o lua53.dll lapi.o lcode.o lctype.o ldebug.o ldo.o ldump.o lfunc.o lgc.o llex.o lmem.o lobject.o lopcodes.o lparser.o lstate.o lstring.o ltable.o ltm.o lundump.o lvm.o lzio.o lauxlib.o lbaselib.o lbitlib.o lcorolib.o ldblib.o liolib.o lmathlib.o loslib.o lstrlib.o ltablib.o lutf8lib.o loadlib.o linit.o
    strip --strip-unneeded lua53.dll
    gcc -std=gnu99 -o lua.exe -s  lua.o lua53.dll -lm
    make[2]: Leaving directory `/e/lua-5.3.2/src'
    make "LUAC_T=luac.exe" luac.exe
    make[2]: Entering directory `/e/lua-5.3.2/src'
    gcc -std=gnu99 -O2 -Wall -Wextra -DLUA_COMPAT_5_2     -c -o luac.o luac.c
    ar rcu liblua.a lapi.o lcode.o lctype.o ldebug.o ldo.o ldump.o lfunc.o lgc.o llex.o lmem.o lobject.o lopcodes.o lparser.o lstate.o lstring.o ltable.o ltm.o lundump.o lvm.o lzio.o lauxlib.o lbaselib.o lbitlib.o lcorolib.o ldblib.o liolib.o lmathlib.o loslib.o lstrlib.o ltablib.o lutf8lib.o loadlib.o linit.o
    ranlib liblua.a
    gcc -std=gnu99 -o luac.exe   luac.o liblua.a -lm
    make[2]: Leaving directory `/e/lua-5.3.2/src'
    make[1]: Leaving directory `/e/lua-5.3.2/src'

    E:\lua-5.3.2>make install INSTALL_TOP=E:/devtools/lua/5.3 TO_BIN="lua.exe luac.exe lua53.dll"
    cd src && mkdir -p E:/devtools/lua/5.3/bin E:/devtools/lua/5.3/include E:/devtools/lua/5.3/lib E:/devtools/lua/5.3/man/man1 E:/devtools/lua/5.3/share/lua/5.3 E:/devtools/lua/5.3/lib/lua/5.3
    cd src && install -p -m 0755 lua.exe luac.exe lua53.dll E:/devtools/lua/5.3/bin
    cd src && install -p -m 0644 lua.h luaconf.h lualib.h lauxlib.h lua.hpp E:/devtools/lua/5.3/include
    cd src && install -p -m 0644 liblua.a E:/devtools/lua/5.3/lib
    cd doc && install -p -m 0644 lua.1 luac.1 E:/devtools/lua/5.3/man/man1

    E:\lua-5.3.2>

最后一步是添加Lua安装路径\ ``E:\devtools\lua\5.3\bin``\ 到系统环境变量PATH.

在cmd终端输入: \ ``lua``\ 即可进入Lua解释器交互界面, 也可以输入\ ``lua -e "print('hello world')"``\ 来测试安装是否正确 (打印出hello
world) .

**install LuaRocks**

下载Windows版的\ `LuaRocks <http://luarocks.org/releases/>`__\ , 解压到E盘, 然后输入如下命令安装, 其中, \ ``/P E:\devtools\LuaRocks``\ 指定安装目录, 可以使用\ ``install /?``\ 查看更多选项.

.. code:: cmd

    cd luarocks-2.3.0-win32
    install /MW /F /LV 5.3 /P E:\devtools\LuaRocks

**注**\ : 执行完毕后, 末尾打印如下类似信息, 告诉你如何添加环境变量:

.. code:: cmd

    ============================
    == LuaRocks is installed! ==
    ============================


    You may want to add the following elements to your paths;
    Lua interpreter;
      PATH     :   E:\devtools\lua\5.3\bin\
      PATHEXT  :   .LUA
    LuaRocks;
      PATH     :   E:\devtools\LuaRocks
      LUA_PATH :   E:\devtools\LuaRocks\lua\?.lua;E:\devtools\LuaRocks\lua\?\init.lua
    Local user rocktree (Note: %APPDATA% is user dependent);
      PATH     :   %APPDATA%\LuaRocks\bin
      LUA_PATH :   %APPDATA%\LuaRocks\share\lua\5.3\?.lua;%APPDATA%\LuaRocks\share\lua\5.3\?\init.lua
      LUA_CPATH:   %APPDATA%\LuaRocks\lib\lua\5.3\?.dll
    System rocktree
      PATH     :   e:\devtools\lua\5.3\\bin
      LUA_PATH :   e:\devtools\lua\5.3\\share\lua\5.3\?.lua;e:\devtools\lua\5.3\\share\lua\5.3\?\init.lua
      LUA_CPATH:   e:\devtools\lua\5.3\\lib\lua\5.3\?.dll

    Note that the %APPDATA% element in the paths above is user specific and it MUST be replaced by its actual value.
    For the current user that value is: C:\Users\liu\AppData\Roaming.

根据上述, 添加必要的环境变量, 由于\ ``PATH``\ 已经存在, 所以只需要\ ``LUA_PATH``\ 和\ ``LUA_CPATH``\ , 文\ `Installing
Lua on a Windows
system <http://www.thijsschreijer.nl/blog/?p=863>`__\ 中说, 对于Lua5.3, 添加\ ``LUA_PATH_5_3``\ 和\ ``LUA_CPATH_5_3``\ , 我试了一下, 两个都对, 如果你安装了不同版本的Lua, 应该用后者指示不同版本.

为测试LuaRocks安装正确, cmd命令行输入\ ``luarocks help``\ 会打印很多帮助信息.

比如可以通过\ ``luarocks install pakage``\ 来安装包, 通过\ ``luarocks remove pakage``\ 来卸载包

举例: 安装luafilesystem

.. code:: cmd

    C:\windows\system32>luarocks install luafilesystem
    Installing https://luarocks.org/luafilesystem-1.6.3-2.src.rock...
    Using https://luarocks.org/luafilesystem-1.6.3-2.src.rock... switching to 'build' mode
    mingw32-gcc -O2 -c -o src/lfs.o -IE:/devtools/lua/5.3/include/ src/lfs.c
    In file included from src/lfs.c:67:0:
    src/lfs.h:21:0: warning: "fileno" redefined [enabled by default]
     #define fileno(f) (_fileno(f))
     ^
    In file included from src/lfs.c:38:0:
    e:\devtools\mingw\include\stdio.h:595:0: note: this is the location of the previous definition
     #define fileno(__F) ((__F)->_file)
     ^
    mingw32-gcc -shared -o lfs.dll src/lfs.o E:/devtools/lua/5.3/bin/lua53.dll -lm
    Updating manifest for e:\devtools\lua\5.3\/lib/luarocks/rocks
    luafilesystem 1.6.3-2 is now built and installed in e:\devtools\lua\5.3\ (license: MIT/X11)

语法
------------------------

-  `Lua 5.3 英文参考手册 <http://www.lua.org/manual/5.3/manual.html>`__
-  `Lua 5.3 中文参考手册 <http://www.lua.org/manual/5.3/manual.html>`__
-  `Programming in
   Lua <http://vdisk.weibo.com/s/z63ACRNxK4cLS?sudaref=www.baidu.com>`__

多重赋值
~~~~~~~~~~~~~~~~~~~~~~~

在Lua中, 多重赋值是合法的, 如\ ``a,b,c = 1,2,3``\ , 则相当于\ ``a=1; b=2; c=3``\ . 参考\ `Lua
5.3 Reference Manual §3.3.3 –
Assignment <http://www.lua.org/manual/5.3/manual.html#3.3.3>`__\ , 可以看到赋值规则是这样的:
[Lua5.3][Lua53refman]

    Before the assignment, the list of values is adjusted to the length
    of the list of variables. If there are more values than needed, the
    excess values are thrown away. If there are fewer values than
    needed, the list is extended with as many nil's as needed. If the
    list of expressions ends with a function call, then all values
    returned by that call enter the list of values, before the
    adjustment (except when the call is enclosed in parentheses; see
    §3.4). 在作赋值操作之前, 那值列表会被 *调整*
    为左边变量列表的个数. 如果值比需要的更多的话, 多余的值就被扔掉.
    如果值的数量不够需求, 将会按所需扩展若干个
    nil. 如果表达式列表以\ **一个函数调用结束**\ , 这个函数所返回的所有值都会在调整操作之前被置入值列表中 (除非这个函数调用被用\ **括号括了起来**\ ; 参见
    §3.4) .

    The assignment statement first evaluates all its expressions and
    only then the assignments are performed.
    赋值语句首先让所有的表达式完成运算, 之后再做赋值操作.

看下面一段代码及其对应输出, 函数\ **maxmin**\ 有两个返回值, 依次输出两个输入参数的最大和最小.

.. code:: lua

    function maxmin( a, b )
        if a < b then
            return b, a
        else
            return a,b
        end
    end

    a, b, c, d = maxmin(2,3), 1, 4
    print(a,b,c,d)                 -- <---> 3   1   4   nil

    a, b, c, d = 1, maxmin(2,3), 4
    print(a,b,c,d)                 -- <---> 1   3   4   nil

    a, b, c, d = 1, 4, maxmin(2,3)
    print(a,b,c,d)                 -- <---> 1   4   3   2

    a, b, c, d = 1, 4, (maxmin(2,3))
    print(a,b,c,d)                 -- <---> 1   4   3   nil

    i = 3; a = {}
    i, a[i] = i+1, 20
    print(i, a[3], a[4])           -- <---> 4   20  nil

    -- swap value
    x = 1; y = 2; z = 3
    x,y,z = y,z,x
    print(x,y,z)                   -- <---> 2   3   1

由上面的规则可知: 1.
**只有当表达式列表以一个函数调用结束, 并且函数调用没有被用括号\ ``()``\ 扩起来, 这个函数所返回的所有值才会在调整操作之前都被置入值列表中**\ , 所以只有\ ``a, b, c, d = 1, 4, maxmin(2,3)``\ 对应的右端值列表中有4个值; 2.
**赋值语句首先让所有的表达式完成运算, 之后再做赋值操作**\ , 所以\ ``i, a[i] = i+1, 20``\ , 只改变了\ ``a[3]``\ 的值.

协同
~~~~~~~~~~~~~~~~

-  线程和协同主要区别: 线程同时运行多个线程, 协同在同一时刻只有一个协同程序运行, 且只有在运行的协同程序明确要求挂起才挂起;
-  给 yield 的参数
   会传给resume, 主函数返回值也会传给resume, 传给resume的参数也会传给yield;
-  yield
   是挂起程序, resume时, yield接受resume传来的新的参数, 从挂起处开始执行;

.. code:: lua

    co = coroutine.create(function ( )
        print('suspended follows: ')
        print("co", coroutine.yield())
        -- body
    end)
    print(coroutine.resume(co))         --> suspended follows -->true
    print(coroutine.status(co))         --> suspended
    print(coroutine.resume(co, 4, 5))   -- co   4   5  -->true
    print(coroutine.status(co))         --> dead
    print(coroutine.resume(co, 4, 5))   --> false   cannot resume dead coroutine


    print('------------')
    co = coroutine.create(function()
        return 6, 7
    end)
    print(coroutine.resume(co))         --> true    6   7

GUI开发
-------------------------

可以使用 `wxLua <http://wxlua.sourceforge.net/>`__ 进行 GUI 开发, 参考
`Build using GCC in
Linux <http://wxlua.sourceforge.net/docs/install.html#C2.5>`__
在Linux上安装, Windows上直接下载二进制包安装即可.




.. |这里写图片描述| image:: https://imgconvert.csdnimg.cn/aHR0cDovL2ltZy5ibG9nLmNzZG4ubmV0LzIwMTYwMjIzMjI1MzU5MDcx