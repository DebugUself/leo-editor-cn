.. rst3: filename: docs\tutorial-rst3.html

   :trim:
   
.. |br| raw:: html

   <br />

########################################
使用提纲创建文档
########################################

.. _`LaTeX`:    http://www.latex-project.org/
.. _`Python`: http://www.python.org/
.. _`Sphinx`:   http://sphinx-doc.org/
.. _`Sphinx 文档`: http://sphinx-doc.org/contents.html
.. _`docutils`: http://docutils.sourceforge.net
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`rST 入门`: http://sphinx-doc.org/rest.html
.. _`第一篇教程`: tutorial-basics.html

..  "I am a huge fan of Leo. I think it's quite possibly the most
..  revolutionary programming tool I have ever used and it (along with the
..  Python language) has utterly changed my view of programming (indeed of
..  writing) forever."---Shakeeb Alireza
    
Leo 的 rst3 命令, 可将包含 `reStructuredText`_ (rST) 或 `Sphinx`_ 标记的 Leo 树转化为 HTML, PDF, `LaTeX`_ 以及其他输出文件格式. 本教程提供了使用 rst3 命令的分步指导.

**前提条件**: 请确保你已提前阅读 `第一篇教程`_. 如果你初次接触 rST, 请阅读 `rST 入门`_. 关于 Sphinx 的全部信息, 请阅读 `Sphinx 文档`_.

rst3 命令, 可自动创建 rST 部分的下划线, *极大* 简化 rST 或 Sphinx 的使用. 想重新组织一个文档, 只需重新组织 Leo 的对应提纲: 你无需手动修改下划线字符.

本教程仅包含 rst3 命令的基本特性. 这足以生成所有 Leo 文档! 

CheatSheet.leo 包含本教程示例的拓展版本. 你可以从 Leo 的帮助菜单打开 CheatSheet.leo.

.. contents:: 目录
    :depth: 3
    :local:

安装 docutils 和 (可选) sphinx
+++++++++++++++++++++++++++++++++++

rst3 命令需要 `docutils`_ Python 包. 如果你使用 sphinx 标记, 你必须同样安装 `Sphinx`_ 包. Sphinx 给予 Leo 和 `Python`_ 网站独特的外观和特性. 安装 docutils 或 sphinx 后, 你必须重启 Leo, 以使新安装生效.

创建 @rst 节点
++++++++++++++++++

.. index::
    pair: @rst Node; Tutorial
    
1. 在你的提纲中创建一个节点.

2. 输入标题::

        @rst myDocument.html

@rst 节点及其后代(descendants)节点, 代表了你的文档.

输出文件和中间文件
+++++++++++++++++++++++++++

用于::

    @rst myDocument.html
    
的 rst3 命令, 将从这个节点和它的子节点, 孙节点等, 生成一个 **输出文件 (output file)**, myDocument.html. 由于 .leo 文件包含 @rst 节点, 所以 rst3 命令将在同一文件夹中创建输出文件. 你可以使用绝对或相对路径, 指定其他文件夹. 例如::

    @rst myDocument.html        # 与 .leo 文件在同一文件夹
    @rst docs/myDocument.html   # 在子文件夹
    @rst ~/docs/myDocument.html # 文件夹的绝对路径
    
rst3 命令在输出文件的同一目录下生成 **中间文件 (intermediate file)**, 其包含由 rst3 命令生成的 reStructuredText 标记, 为 .txt 后缀::

    myDocument.html.txt

选择 docutils 或 sphinx
++++++++++++++++++++++++++

在包含 @rst 节点的 .leo 文件的 @settings 树中, 设置 rst3_call_docutils, 以决定是使用纯 rST 标记, 还是全部 sphinx 标记. 

使用纯 reStructuredText 标记::

    @bool rst3_call_docutils = True
    
使用 sphinx 标记::
    
    @bool rst3_call_docutils = False

设置 sphinx 的 conf.py
*************************

使用 sphinx, 你必须配置 sphinx 的 conf.py 文件, 以发现由 rst3 命令创建的中间文件.
例如, Leo 文档的 conf.py 包含如下内容::

    source_suffix = '.html.txt'
    
其 "匹配" 中间文件的形式. 例如, 提供::

    @rst myDocument.html
    
设置 rst3_intermediate_extension 的默认取值::

    @string rst3_write_intermediate_extension = .txt
    
中间文件的名称将是::

    myDocument.html.txt

myDocument.html.txt 是 shpinx 的 **输入** 文件.

在 @rst 节点输入标题
+++++++++++++++++++++++++++

在 @rst 节点的内容文本中, 输入::

    #############
    战争与和平
    #############
    
rST 标记使用 上/下划线(over/underlining) 表示单元标题. 在标题(战争与和平)上, 输入井号组成的 **上划线**, 在其下方输入同样 的 **下划线**. rST 对单元标题的标记有点麻烦. 

- 上/下划线必须包含 4 个字符
- 上/下划线所含字符数, 必须不少于标题所含字符数
- 上划线符号与下划线符号必须相同

另外, rst3 命令要求单元标题的上/下划线使用 "#" 字符.

开始单元(chapter)
+++++++++++++++++++++

在 @rst 节点本身的正文中, 输入开篇语:

    "Well, Prince, so Genoa and Lucca are now just family estates of the
    Buonapartes. But I warn you, if you don't tell me that this means war,
    if you still try to defend the infamies and horrors perpetrated by that
    Antichrist--I really believe he is Antichrist--I will have nothing more
    to do with you and you are no longer my friend, no longer my 'faithful
    slave,' as you call yourself! But how do you do? I see I have
    frightened you--sit down and tell me all the news."
    
    It was in July, 1805, and the speaker was the well-known Anna Pavlovna
    Scherer, maid of honor and favorite of the Empress Marya Fedorovna.
    With these words she greeted Prince Vasili Kuragin, a man of high rank
    and importance, who was the first to arrive at her reception. Anna
    Pavlovna had had a cough for some days. She was, as she said, suffering
    from la grippe; grippe being then a new word in St. Petersburg, used
    only by the elite.

创建章节(sections) 和子章节(subsections)
++++++++++++++++++++++++++++++++++++++++++++++++

要想创建一个新的章节, 子章节等, 需在输出文件中:

1. 创建一个新的提纲节点, 作为 @rst 节点的后代.

2. **新节点的标题成为章节的标题.**

3. 在节点的正文中, 输入章节的内容.

这就是全部:

- **rst3 命令自动生成 rST 下划线**.

- **你通过重组节点, 重组你的文档.**

重组文档时, *没有* 必要修改标记, 相比编写 "原始" rST, 这是一个巨大的进步.

书写你的文档
++++++++++++++++++

现在你写了小说, 短小故事, 文档等. 总是这样组织你的工作:

| **节点创建章节, 子章节, 子子章节等.**
| **依赖它们在提纲中的位置.**

运行 rst3 命令
++++++++++++++++++

.. index::
    pair: rst3 Command; Tutorial

``<Alt-X>rst3<Return>`` 运行 rst3 命令.

- 如果当前节点是一个 @rst 节点, 或 @rst 节点的后代节点, rst3 命令适用于最近的祖先(ancestor) @rst 节点.

- 否则, rst3 命令应用于所有后代 @rst 树.

如果 @bool rst_call_docutils 为 True, rst3 命令将自动调用 doctils 生成输出文件. 更多关于 Leo 设置, 请见 `此章 <tutorial-basics.html#configuring-leo>`_.

使用 sphinx 时, 在运行 rst3 命令后, 运行 sphinx 的 "make" 工具, 创建最后的输出文件.

**错误和警告**:   
 
1. 安装 docutils 时, 如果看见下面错误, 重启 Leo::

    writeToDocutils: docutils not present
    
2. Leo 有一个默认的样式表, 可以居中, 并加大加粗标题, 所以你可以忽视如下信息::
    
    stylesheet not found <path-to>default.css

其他主题
++++++++++++



\@rst-no-head 覆盖章节
**************************

有时, 你想组织文本, 而无需创建章节:

1. 创建一个提纲节点, 组织你的文本.

2. 输入标题::

    @rst-no-head <任意文本: 将被忽视>
    
rst3 命令会在之前的章节, 增加这个节点的正文:

- 标题会被忽视
- @rst-no-head 节点怎么都不会改变 rST 的章节结构

\@rst-ignore & @rst-ignore-tree 忽视内容
********************************************

有时将参考资料放在你的 @rst 树中也很有用, 其 *不会* 出现在实际的输出中. 要想让 rst3 命令忽略单个节点, 可在节点标题输入::

    @rst-ignore <ignored-text>
    
如此, 标题和正文均不会出现在输出文件中.

要想让 rst3 命令忽略一个节点及它的所有后代, 可在标题输入::

    @rst-ignore-tree <ignored-text>

插入原始标记
******************

`rST 手册 <http://docutils.sourceforge.net/docs/user/rst/quickref.html#directives>`_ 介绍了如何将 "原始" 标记插入至输出中. 例如, Leo 的文档定义如下::
    
    .. |---| unicode:: U+02015 .. for quotes
       :trim:

现在, ``---`` 插入了 ---, unicode "引号" 表明引用的作者. 注意 rST 自动转换 `--` 为 --.


rST ``|`` 标记分拆文本为指定行, 但是有些场景无法使用. 在文本中插入行结束符的方式如下::


    .. |br| raw:: html
    
       <br />

总结
++++++

- rst3 命令会转换 @rst 树为一个输出文件和中间文件.
  
- docutils 使用输出文件; sphinx 使用中间文件.

- 以 "rst3" 开头的设置, 控制 rst3 命令的运行.

- 在 @rst 树中, 标题将成为 rST 的章节.

- 生成的 rST 的章节层级, 对应 Leo 中的提纲层级.

- 你只需要通过重组对应的 @rst 树来重组你 rST 文档.

- rst3 命令作用于最近的祖先 @rst 节点, 如果有的话, 或所有 @rst 节点的所有后代.

- @rst-no-head 节点插入文本(或标记) , 无需 rST 标题.

- rst3 命令将忽视 @rst-ignore 节点和 @rst-ignore-tree 树.

- LeoDocs.leo 中的 @button make-sphinx 节点, 自动调用 sphinx.

- CheatSheet.leo 包含了教程示例的扩展版本. 你可以从 Leo 的帮助菜单打开 CheatSheet.leo

- rst3 命令提供了 *很多* 其他功能. 具体细节, 请见 `rst3 单元 <rstplugin3.html>`_.

进阶学习
++++++++++++

现在你已具备足够知识, 可开始使用 rst3 命令. 可能的下一步行动:

- 在 LeoDocs.leo 中, 阅读 Leo 自己的文档. 探索树中的节点, 与你面前的网页文档如何对应.

- LeoDocs.leo 有一个 @button make-sphinx 脚本, 可自动调用 sphinx.

- 创建你自己的 @rst 节点. 运行 rst3 命令, 观察结果.

- 如果你遇到问题, 可求助于 https://groups.google.com/forum/#!forum/leo-editor.

翻译贡献者: `OMlalala <https://github.com/OMlalala>`_
 
校对贡献者: `hetao <https://github.com/livingworld>`_

