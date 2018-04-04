.. rst3: filename: docs/installing.html

##############
安装 Leo
##############

.. index:: 安装 Leo

.. _`Leo 的帮助论坛`: http://groups.google.com/group/leo-editor

本章介绍在 Windows, Linux 和 MacOS 中, 如何安装和运行 Leo . 

**要点**: 如果你安装Leo有 *任何* 问题, 请向 `Leo 的帮助论坛`_ 寻求帮助. 

.. contents:: Contents
    :depth: 4
    :local:

依赖项
+++++++++

.. _`Anaconda`:   https://www.anaconda.com/download/
.. _`Miniconda`:  https://conda.io/miniconda.html
.. _`Docutils`:   http://docutils.sourceforge.net
.. _`feedparser`: https://pypi.python.org/pypi/feedparser
.. _`Markdown`:   http://daringfireball.net/projects/markdown/syntax
.. _`Python`:     https://www.python.org/
.. _`PyEnchant`:  http://pythonhosted.org/pyenchant/download.html
.. _`PythonTidy`: https://pypi.python.org/pypi/PythonTidy/
.. _`PyQt`:       http://www.riverbankcomputing.co.uk/software/pyqt/intro
.. _`PyQt4`:      http://www.riverbankcomputing.com/software/pyqt/download
.. _`PyQt5`:      http://www.riverbankcomputing.com/software/pyqt/download5
.. _`Sphinx`:     http://www.sphinx-doc.org/en/stable/

Leo 的最小依赖项是:

* `Python`_ 2.6 或更高版本, 包括所有 Python 3.x 版本. 
* `PyQt4`_ 或 `PyQt5`_ . 

下列安装包是可选的, 但建议:

* `Docutils`_ :rst3 命令和 viewrendered 插件所需的文件. 
* `Sphinx`_ :需要重新生成 Leo 的文档. 
* `PyEnchant`_ :拼写检查需要. 

插件可能需要其他软件包. 例如, 如果想要使用 markdown 渲染时, viewrendered 需要 `Markdown`_ , 但它是可选的. 没有 `feedparser`_ , rss.py 将不能正常工作等.

用 pip 安装 Leo
++++++++++++++++++

.. _`安装 pip`:      https://pip.pypa.io/en/stable/installing/               
.. _`安装 Python`:   http://python.org.
.. _`pip`:              https://pypi.python.org/pypi/pip

Python 的 `pip`_ 工具将自动下载 *并* 安装 Leo 和 Leo 的所有依赖项:

1. 如果需要的话, 先 `安装 Python` . 如果您是 Python 新手, 请安装 Python 3 , 而不是 Python 2. Python3 自动安装 pip. 

2. (仅限Python 2) 如果需要的话, `安装 pip` 本身. 要检查是否安装了 pip, 打开终端窗口并键入::

    pip --version
   
3. (仅限Python 2) 从终端, 安装 `PyQt`_ ::

    pip install pyqt

4. 安装 Leo::

    pip install leo
    
这将下载并安装所需的软件包(PyQt 除外).

安装软件包
+++++++++++++++

**Python**:Leo 可以在任何支持 Python2.6 或以上的平台工作, 包括 Python3.0 和以上版本. 要安装 Python , 请参阅 http://python.org.

**PyQt**:  `PyQt`_ 提供了 Leo 的小部件:

* 从 http://www.riverbankcomputing.com/software/pyqt/download 下载 PyQt4. 
* 从 http://www.riverbankcomputing.com/software/pyqt/download5 下载 PyQt5. 

**要点:** PyQt 版本必须与您安装的 Python 版本相匹配. 记住, Leo 需要 Python 2.6 或更高版本, 或者 Python 3.0 或更高版本. 

**PyEnchant:** 如果你想要使用 Leo 的拼音选项卡, 你必须安装 `PyEnchant`_ . 对于 Windows 用户, 有一个可执行的安装程序.

安装 Leo 本身
+++++++++++++++++



在 Windows 上安装 Leo
*************************

安装Python和Qt, 如上所述(`安装软件包`_).

现在你有一个选择. 你可以使用Leo的二进制 (single-click) 安装程序
或直接下载Leo的源文件.

使用单击安装程序
^^^^^^^^^^^^^^^^^^^^^^^^

.. _`SourceForge 下载页面`: http://sourceforge.net/projects/leo/files/Leo/
.. _`运行 Leo`: running.html

Leo 有一个用于 Windows 的二进制安装程序, 可以在 `SourceForge 下载页面`_ 找到. 二进制安装程序安装 Leo 并设置 Windows 文件关联. 现在, 请参阅 `运行 Leo`_ 在安装后如何运行 Leo.

从源安装 (Windows)
^^^^^^^^^^^^^^^^^^^^^^

.. _`Leo 的下载页面`: download.html

您可以用三种方式下载 Leo 的源文件, 正如 `Leo 的下载页面`_ 所描述的那样. 如果源文件被压缩, 则将其解压到临时文件夹. 您可以将源文件放在您喜欢的任何地方, 包括 Python 的 *site-packages* 文件夹, 例如  C:\\Python26\\Lib\\site-packages.

接下来, 您将发现为 .leo 文件创建 Windows 文件关联非常方便, 正如下一节所述.

创建 Windows 文件关联
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*要点*: Leo 的二进制 Windows 安装程序会自动设置文件关联, 所以只有当您从一个 .zip 文件或其他来源中安装 Leo 时, 才需要这个部分. 

有两种办法将 .leo 文件与 Leo 关联起来. 第一种使用的是 Windows 控制面板, 第二种是 Windows 控制台. 

**方法 1：使用 Windows 控制面板**

目标是您希望用以下命令关联 .leo 文件::

    "<path to python>\python.exe" "<path to launchLeo.py>\launchLeo.py" "%1"
    
在Windows 7之前, 你可以使用文件夹选项控制面板来完成这个操作. 在Windows 7中, 你可以使用默认程序控制面板来完成这个操作. 

*注意:* "%1" 只传递被点击的文件, 引用空格等. 需要使用引号来处理包含空格的文件路径. 

*警告:* 在批处理文件中, 1%只传递第一个命令行参数. 在批处理文件中, 期望 %* 为文件关联工作是合乎逻辑的. 唉, 它没有. 

**方法2：使用Windows控制台**

打开带有管理员权限的 Windows 控制台, 然后键入::

    ftype LeoFile="<path to python>\pythonw.exe" "<path to launchLeo.py>\launchLeo.py" "%1" %*
    assoc .leo=LeoFile

并把 leo.bat 放到 %PATH%::

    @start /b "Leo" "<path to python>\python.exe" "<path to launchLeo.py>\launchLeo.py" %*
    
如果你想要为 Leo 创建一个单独的控制台窗口, 你可以省略 /b 选项.

用 git 安装 Leo
******************

.. _`git`: https://git-scm.com/

**要点**: 本节讲述如何设置 `git`_ 以便您可以使用 ``git clone``获取最新的源文件. 

许多用户希望跟踪 Leo 的开发版本, 以保持最新的特性和 bug 修复. 运行开发版是相当安全和简单的, 而且如果您想要给 Leo 做贡献, 这也是一个要求. 

1. 首先, 你需要获得从 http://git-scm.com/ 获得 git. 
2. 从 Github 中获得 Leo::

        git clone https://github.com/leo-editor/leo-editor (http access)
    
   or::
   
        git clone git@github.com:leo-editor/leo-editor.git (ssh access)

就是这样! 你可以直接运行 launchLeo.py. 当你想要从 GitHub 上刷新最新修改的代码, 运行 git pull.

在 Linux 上安装 Leo
***********************

.. _`从 debian 软件包中安装 Leo`: installing.html#从-debian-软件包安装
.. _`从源文件中安装 Leo`: installing.html#从源安装-linux

如果你正在使用 Debian/Ubuntu, 最好 `从 debian 软件包中安装 Leo`_, 如下所述. 这提供了文件关联、图标、启动项等. 而且, 你可以 `从源文件中安装 Leo`_.

从 debian 软件包安装
^^^^^^^^^^^^^^^^^^^^^^^^^^

将这些文件添加到 `/etc/apt/sources.list`::

    deb http://ppa.launchpad.net/villemvainio/ppa/ubuntu jaunty main
    deb-src http://ppa.launchpad.net/villemvainio/ppa/ubuntu jaunty main

然后运行::

    sudo apt-get update
    sudo apt-get install leo

从源安装 (Linux)
^^^^^^^^^^^^^^^^^^^^

.. _`下载 Leo 源文件`: download.html

你可以通过以下三种方法之一 `下载 Leo 源文件`_ . 如果源文件压缩了, 将它们解压到主目录的文件夹中, 比如 ~/leo-5.7. 

您现在有几个选择. 

1. 您可以从主目录运行 Leo. 只需要将 ~/leo-5.7 添加到您的路径. 

2. 你可以使用以下命令将 leo 安装到 /usr/local/lib 和 /usr/local/bin 中:

    cd ~/leo-5.7
    sudo python setup.py install

请参阅 `运行 Leo`_ 了解如何在安装后运行 Leo.

在 MacOs 10.7 (Lion) 或更高版本上安装 Leo
**************************************************

.. .. http://groups.google.com/group/leo-editor/browse_thread/thread/92ae059cc5213ad3

非常感谢 Ludwig Schwardt 提供的以下安装指导. 使用 HomeBrew 方法比以前 *容易多了*. 

**EKR注意事项**: 升级 MacOS, 首先卸载 pyqt, sip 和 qt 可能是个好注意::

    brew remove pyqt sip qt
    brew install qt sip pyqt

我(Ludwig)最近收到了一台新的 MacBook Pro, 并对 Mac OS 10.7(Lion) 进行了全新升级. 然后我利用这个机会在一个干净系统上测试了各种软件的安装程序. 我主要的发现是, 优秀的 Homebrew(mxcl.github.com/homebrew/) 使事情容易多了. 

为什么选择 Homebrew？它并不会尝试用自己的版本, 比如 Macports 或 fink 来替换 Mac 上的每一个功能. 它尽可能重复使用现有的库. 例如, 无需重新安装 Python(当人们试图在 Mac 上安装新软件时, 是我的一个宠物抱怨, 以及许多混乱和痛苦的来源). 它安装到 /usr/local, 这是找到第三方库和标题的标准的位置, 而不是隐藏的 /opt 或 /sw. 使用和扩展都很简单. 

此处是我的安装记录:

- 阅读 http://brew.sh/ 上的 Homebrew 安装说明

- 确保您已经安装了 Xcode(通过确认"gcc"运行在终端来测试). 只需要较小的命令行工具；没有必要获得完整的 Xcode beast. 

- 在准备 Homebrew 时, 我认为最好的选择是通过以下方式删除 /usr/local ::

    sudo rm -rf /usr/local

  并通过 HomeBrew 代替安装任何软件. 
  
  HomeBrew 软件包管理器非常易于使用, 你会发现快速替换已删除的软件包. 
  
  如果删除 /usr/local 让您满意(您不希望失去您心爱的第三方软件), 次优选择是确保您已经通过以下方式为目录写了权限::

    sudo chown -R <your user name>:admin /usr/local

  如果您不知道自己的用户名, 请运行 "whoami".  :-) 这是很有用的, 因为 homebrew 实际上不鼓励你以超级用户的身份安装第三方软件(对于这种情况, 应用程序中的常用 Mac 应用程序也以普通的用户身份安装). 

-通过在终端中运行以下命令安装 Homebrew (http://mxcl.github.com/homebrew/)::
    
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- 运行 "brew doctor" 并检查任何进一步改善您的系统的建议. 

  EKR注意：我认为在安装 XCode 页面后已经安装了命令行工具. 我没有, 而 "brew doctor" 告诉我. 

- 运行 "brew update" 来获取最新的公式

- 安装 sip 并注意警告::

    brew install sip

  这会警告将本地 python 目录添加到您的 PYTHONPATH 中. 记下这是什么(特别是如果你不在 Lion 上! ).

- 将以下行添加到 ~/.bash_profile中
  (或 ~/.profile 在 Leopard 上).  这是 LION 的默认设置::

      export PATH=/usr/local/bin:$PATH
      # 这是由 Homebrew 所建议的 SIP(和PyQt)
      export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH

- 安装 PyQt::

    brew install pyqt
 
- 打开新的终端选项卡/窗口, 以使上述设置生效, 并安装 Leo. 我下载了 Leo-4.9-final-a.zip, 将其解压缩, 然后在 Leo 目录中运行 "python launchLeo.py". 

得到一个 Leo 公式适用于 Homebrew 真的很棒. 如前所述, 主要问题是将所有 Leo 文件放在 /usr/local 层次结构的何处.

用 Anaconda 或 Miniconda 安装任何东西
+++++++++++++++++++++++++++++++++++++++++++++

`Anaconda`_ 的科学计算环境包括 Python, NumPy, SciPy, PyQt 和其他上千种工具、软件包和库. 它下载后有 500 +MB, 但物有所值. 

要安装 Leo, 可以从控制台进行操作::

    pip install leo

`Miniconda`_ 环境仅包含 Python 和 `conda` 软件包管理工具. 从完整的 Anaconda 生态系统中挑选并选择. 

要安装Leo, 可以从控制台进行操作::

    conda install pyqt5
    pip install leo

