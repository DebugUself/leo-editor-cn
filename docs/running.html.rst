.. rst3: filename: docs/running.html

##############
Running Leo
##############

.. index:: Running Leo

This chapter tells how to run Leo and discusses Leo's command-line options.

.. contents:: Contents
    :depth: 3
    :local:

运行 Leo
++++++++++

你可以按照如下方式从 Python 解释器中运行 Leo::

    import leo
    leo.run() # 运行 Leo, 打开一个新的提纲, 或,
    leo.run(fileName=aFileName) # 运行 Leo, 打开给定的文本名. 

运行 Leo 的另一种方式如下::

    cd <path-to-launchLeo.py>
    python launchLeo.py %*

这里有一些提示会让 Leo 更容易运行:

**Linux**
    
接下来的 shell 脚本将允许你通过键入 leo foo 打开 foo.leo 文件::

    #!/bin/sh 
    python <leopath>launchLeo.py $1

其中 <leopath> 是指向包含 Leo 文件夹的文件夹路径.  

**Windows**

你可以使用批处理文件将 Leo 和 .leo 文件相关联. 将下列 .bat 文件放在 c:\\Windows中::

    <path-to-python>/python <path-to-leo>/launchLeo.py %*

这里 <path-to-leo> 是指向 *包含* leo 文件夹的文件夹路径, 即包含 launchLeo.py 的文件夹.

第一次运行 Leo
*******************

第一次启动 Leo 时, 对话框会要求您输入唯一的标识符. 如果您使用的是git等源文件控制系统, 请使用您的的 git 登录名. 否则您的姓名首字母就行了. 

Leo 将此标识符存储在 .leoID.txt 文件中 . Leo 尝试在您的主目录下的 .leo 子目录中创建 leoID.txt, 然后在 Leo 的配置目录中, 最后在 Leo 的核心目录中. 您可以随时通过编辑 .leoID.txt 来更改此标识符.

在批处理模式下运行 Leo
*******************************

在启动时, Leo 查找表单中的两个参数::

    --script scriptFile

如果发现, Leo 进入批处理模式. 在批处理模式下, Leo 不显示任何窗口. Leo 假定 scriptFile 包含一个 Python 脚本并使用 Leo 的执行脚本命令执行该文件的内容. 默认情况下, Leo 将所有的输出发送到控制台窗口. scriptFile 中的脚本通过调用 app.log.disable 或 app.log.enable 来禁用或启用此输出. 

scriptFile 中的脚本能够执行任何除了编辑正文和编辑标题命令外的任何 Leo 命令. 这些命令需要与用户交互. 例如, 下面的批处理脚本读取一个 Leo 文件并打印该文件中的所有标题::

    path = r"<path-to-folder-containing-the-leo-folder>\\leo\\test\\test.leo"

    g.app.log.disable() # 打开文件时禁用读取消息
    flag,newFrame = g.openWithFileName(path,None)
    g.app.log.enable() # 重新启用日志. 

    for p in newFrame.c.all_positions():
        g.es(g.toEncodedString(p.h,"utf-8"))

从控制台窗口运行 Leo
****************************

.. _`python.exe`: installing.html#创建-windows-文件关联

Leo 将更详细的错误消息发送到 stderr, 即输出到控制台窗口的流. 在 Linux 和 MacOS 环境中, python 程序通过使用可见的控制台窗口执行. 

在 Windows 中, 你可以通过用 `python.exe`_ 而 *不是* pythonw.exe 关联 .leo 文件, 在可见的控制台窗口运行 Leo.

.leo 目录
***********

如果不存在 HOME 环境变量, 则 Leo 使用 os.expanduser('~') 来确定 HOME 目录. 

Leo 将几个文件放在您的 HOME/.leo 目录: .leoID.txt, .leoRecentFiles.txt 和 myLeoSettings.leo.

Leo 的命令行选项
++++++++++++++++++++++

Leo 支持下面的命令行选项. 像往常一样, 你可以通过在控制台窗口键入以下内容查看列表::

    leo -h

或::

    leo --help

你将会得到如下内容::

    Usage: launchLeo.py [options] file1, file2, ...

    Options:
      -h, --help            显示帮助信息并退出
      --debug               启用调试模式
      --diff                使用 Leo 作为外部 git diff
      --fullscreen          开始全屏
      --ipython             启用 ipython 支持
      --fail-fast           在第一次失败后停止单元测试
      --gui=GUI             gui 使用 (qt/qttabs/console/null)
      --listen-to-log       启动时启动 log_listener.py
      --load-type=LOAD_TYPE @<file> 类型用于从命令行加载非提纲
      --maximized           开始最大化
      --minimized           开始最小化
      --no-cache            禁用对缓存文件的读取
      --no-plugins          禁用所有插件
      --no-splash           禁用启动屏幕
      --screen-shot=SCREENSHOT_FN
                            拍屏幕快照然后退出
      --script=SCRIPT       执行一个脚本然后退出
      --script-window=SCRIPT_WINDOW
                            打开一个脚本窗口
      --select=SELECT       标题或GNX节点选择
      --session-restore     在启动时恢复先前保存的会话选项卡
      --session-save        退出时保存会话选项卡
      --silent              禁用所有日志消息
      --trace-binding=BINDING
                            跟踪密钥绑定
      --trace-focus         跟踪焦点的变化
      --trace-plugins       跟踪插件的导入
      --trace-setting=SETTING
                            跟踪设置的位置
      --trace-shutdown      跟踪关闭逻辑
      -v, --version         打印版本号并退出
      --window-size=WINDOW_SIZE
                            初始窗口大小 (高 x 宽)

Leo 的工作簿文件
++++++++++++++++++++++

如果您在命令行中没有提供任何文件参数, 则Leo将打开 ``~/.leo/workbook.leo``. 起初, 这个文件包含 Leo 的备忘单和来自 rst3 教程的一个例子.

使用会话
++++++++++++

当 Leo 第一次启动时, Leo 会自动打开**会话** 指定的 .Leo 文件列表. 这样地::

    leo --session-save --session-restore <list of .leo files>

当 Leo 关闭时, 它将会话状态存储在 `~/.leo/leo.session` 中. 会话状态由打开的文件列表和每个文件中选定的节点组成. 下一次 Leo 开始使用这些选项时, Leo 将打开这些文件并选择合适的节点.

