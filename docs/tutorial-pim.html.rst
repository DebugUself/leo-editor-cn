.. rst3: filename: docs\tutorial-pim.html

.. |---| unicode:: U+02015 .. for quotes
   :trim:
   
###########################################
使用 Leo 作为个人信息管理器
###########################################

..  "克隆是纯粹的天才!"---Michael Manti
..  "如果你像我一样, 你有一种随着时间的推移收集到的
..  基础知识库.而且你有项目, 在那里使用这些信息.  
..  现在, 用传统的提纲, 你开始将这些信息加倍,
..  因为你希望为项目提供项目所需的信息.
..  你也可以用 Leo 做这个, 但是如果你在一个地方更改文本,
..  **它也会在其它地方更新!** 这是我在其它提纲
..  从没有看到的功能 (我尝试过一些). 太神了! 
..  Leo 直接支持我工作的方式!"---F. Geiger

本章讲述如何使用 Leo 作为个人信息管理器. 它介绍 `克隆`_: Leo 组织数据最独特和强大的功能之一.

.. contents:: Contents
    :depth: 2
    :local:

克隆
++++++

.. index::
    pair: Clone; Tutorial
    
**克隆** 是出现在 Leo 提纲中多个位置的节点. 克隆在其图标框内中标记有一个小的红色箭头. 节点的所有克隆实际上是 **相同的节点**:

- 任何一个克隆的更改都会影响所有克隆.
- 插入, 移动或删除任何克隆的子节点将会改变屏幕中的所有其他的克隆.

克隆允许将数据存储在提纲中的多个位置.

``Ctrl-` (clone-node)``
    克隆节点 A. 快捷键是一个沉音符, *不是* 单引号. 这通常与波浪号 ``~`` 字符同键.

请花点时间试验克隆:

- 创建一个标题为 A 的克隆.
- 用 ``clone-node`` 命令克隆节点 A.
- 将一些文本输入到 A 的正文中.
- A 的所有克隆现在具有相同的正文.
- 插入一个节点, 比如说 B, 作为任一 A 节点的子节点.
- 注意, *所有的* A 节点现在都有一个 B 子节点.
- 如果你克隆 B, 看看会发生什么.
- 如果你插入, 删除或移动 A 节点的子节点, 看看会发生什么.
- 当你删除节点的倒数第二个克隆时, 该节点再次成为常规节点.

克隆通过创建视图加速工作流
+++++++++++++++++++++++++++++++++++++++

克隆可以大大加速你的工作流程. 要启动一个项目, 请克隆与项目相关的节点, 并将它们拖放至顶层或接近顶层, 以便轻松获取它们. 项目完成后, 只需要删除克隆. 这个工作流程出奇的有效:

- 原始节点从不移动, 但是它们随克隆而变.

- 当你完成任务时, 没有什么可以 "放回原位". 只是删除克隆.
  
用这种方式, **克隆创建视图**: 当你为一个项目收集克隆节点时, 实现上是创建了一个面向项目的提纲视图. 该视图 **只关注** 那些与手头任务相关的节点.

使用缩写和模板
+++++++++++++++++++++

.. index::
    pair: Abbreviation; Tutorial

在你输入时, Leo 可以选择性地扩展缩写. 缩写通常以 ``;;`` 结尾, 所以它们不会意外触发.

要使用缩写, 你必须在 myLeoSettings.leo 中启用它们::

    @bool enable-abbreviations = True

你可以在 ``@data abbreviations`` 节点或 ``@data global-abbreviations`` 节点中定义缩写. 没有预定义, 但是 ``leo/config/exampleSettings.leo`` 包含 ``@data abbreviations examples`` 节点中的示例缩写.

缩写可以简单地作为快捷键::

    ncn;;=@nocolor
    
缩写可以跨越多行. 以 ``\:`` 作为连续行的开头, 像这样::

    form;;=<form action="main_submit" method="get" accept-charset="utf-8">
    \:<p><input type="submit" value="Continue &rarr;"></p>
    \:</form>\n

缩写可以定义模板, 其中 ``<|a-field-name|>`` 表示要填写的字段::

    input;;=<input type="text/submit/hidden/button"
    \:name="<|name|>"
    \:value="" id="<|id|>">\n

插入模板后, 输入 ``,,`` 选择下一个区域.

缩写可以执行 **缩写脚本**, 用``{|{`` 和 ``}|}`` 分割::

    date;;={|{import time ; x=time.asctime()}|}
    ts;;={|{import time ; x=time.strftime("%Y%m%d%H%M%S")}|}
    
要使用缩写脚本, 请在 myLeoSettings.leo 中启用它们, 如下所示::

    @bool scripting-abbreviations = True

在启用缩写脚本的情况下, 输入 ``ts;;`` 给出::

    20131009171117
    
甚至可以定义缩写脚本执行的上下文. 详情请参阅 leoSettings.leo.

使用 URLs
+++++++++++

.. index::
    pair: URL; Tutorial
    pair: @url; Tutorial

只要启用了语法着色, Leo 就会突出显示 URL.

``Ctrl-Left-Click (open-url-under-cursor)``
    打开光标下的 URL.
``open-url``
    打开显示在标题或正文第一行的 URL. 如果标题以 ``@url`` 开头, 那么标题的其余部分就是 url.
    
**注意**:

- Leo 使用 os.startfile 打开看起来像文件名的 URL.
- Leo 使用你的默认网络浏览器打开所有其他 URL.
- 你的浏览器支持的任何方案 (http, mailto, ftp, file 等.) 均有效.
- URL 不应包含空格: 使用 ``%20`` 代替空格.

`请参阅附录 <appendices.html#valid-url-s>`_ 以获取有效 URL 的完整说明.

使用章节
++++++++++++

.. index::
    pair: Chapter; Tutorial
    pair: @chapter; Tutorial

@chapter 树表示 **章节**. 你可以从图标区域或使用 chapter-select 命令 **激活** 章节. 激活章节只会使章节中的那些节点可见. ``main`` 章节代表了整个提纲. 激活 ``main``章节显示所有的提纲节点. 

``chapter-select-main``
    选择 main 章节.
    
``chapter-select-<chapter-name>``
    按名称选择章节.

概要
++++++

克隆是出现在提纲中多个位置的节点.

- 对一个克隆的更改会影响所有其他克隆.
- 节点的所有克隆都是 **完全相同的节点**

视图允许数据的多个视图存在于单个提纲中.

- 视图只是节点的集合.
- 由于克隆, 一个节点可能同时存在于许多视图中.
- 视图关注任务并减少对节点的搜索.

在你输入时, Leo 拓展缩写.

- 缩写范围从简单的快捷键到包含字段的多行模板.
- 输入 ``,,`` 移动到下一个字段.
- 缩写还可以插入执行代码的结果.

Ctrl 加鼠标左键点击任何的 URL 打开 URL.

@chapter 树表示章节. 激活章节只会显示该章节中的节点.

