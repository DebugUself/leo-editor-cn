.. rst3: filename: docs/preface.html

.. |---| unicode:: U+02015 .. for quotes
   :trim:
   
.. |br| raw:: html

   <br />

   
########
Leo 简介
########

.. Use full links here so links are active in LeoDocs.leo

.. _`Emacs`: https://www.gnu.org/software/emacs/
.. _`Leo的教程`: tutorial.html
.. _`寻求帮助`:   https://groups.google.com/forum/#!forum/leo-editor
.. _`有向无环图`: https://en.wikipedia.org/wiki/Directed_acyclic_graph
.. _`开发人员和用户`: https://groups.google.com/forum/#!forum/leo-editor
.. _`Leonine`: leonine-world.html
.. _`Clones`: tutorial-pim.html
.. _`Python API`: tutorial-scripting.html
.. _`面向提纲的指令`: tutorial-basics.html#markup
.. _`Next`: testimonials.html

    "Word 提纲非常有用. 但是 Leo 让 Word 看起来像一个笨重的玩具"---Joe Orr

Leo 是使用和组织数据, 程序和脚本的根本不同的方法. Leo 积极的开发了 20 多年, 拥有一批活跃的 `开发人员和用户`_. 

**Leo 是:**

- 一个功能齐全的 IDE, 具有许多受 `Emacs`_ 影响的功能. 
- 一个提纲. 在 Leo 中的任何东西都是提纲. 
- 一个数据管理器和个人信息管理器. 
- 一个强大的脚本环境. 
- 一个组织和学习计算机代码的工具. 
- 通过简单的插件架构可扩展的. 
- 一个与 IPython, Vim 和 Emacs 一起使用的工具. 
- 用 100% 纯 Python 编写. 

**Leo的独特功能**

Leo *完全集成了* Python 脚本和提纲. 在 Vim, Emacs 或 Eclipse 中模拟以下功能是可能的, 正如可以用汇编语言模拟 Python 一样...

- 所有的命令和脚本都可以通过简单的 `Python API`_ 轻松访问提纲结构.  |br|
  例如, p.b 是所选提纲节点的正文.  |br|
  脚本有完全地访问权对Leo的所有来源 (sources).
- `Clones`_ 创建提纲的多个视图.  |br|
  Leo 的底层数据是一个 `有向无环图`_.  |br|
  因此, Leo 以全新的方式组织数据.
- 脚本和程序可使用 `面向提纲的指令`_ 从大纲中组成.
- Importer 将扁纯文本转换成提纲.
- @test 和 @suite 脚本自动创建单元测试.
- @button 脚本应用脚本到大纲数据.

这些功能结合起来, 创造了一种 `Leonine`_ 式的编程和组织的方法. 你不会在一两天内了解 Leo 的全部内容. `Leo的教程`_ 解释了基本的功能. 你可以稍后了解更多高级的功能. 如果你遇到困难, 请立即 `寻求帮助`_ .

