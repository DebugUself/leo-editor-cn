.. rst3: filename: docs\tutorial-tips.html

#############################
Useful Tips
#############################

One of these tips appears on startup, by default.

You can disable these tips by setting @bool show-tips = False.

.. contents:: Contents
    :depth: 3
    :local:

The most important tips
+++++++++++++++++++++++



You don't have to remember command names
****************************************

.. _`commands tutorial`: tutorial-basics.html#commands

To execute a command, type `Alt-X` followed by the first few characters of command name, followed by `Tab`. The list of commands matching what you have typed appears.
For more details, see the `commands tutorial`_.

Learn to use clones
*******************

.. _`clones tutorial`: tutorial-pim.html#clones

Clones are "live" copies of the node itself and all its descendants.
See the `clones tutorial`_ for more details.

Learning to use Leo
+++++++++++++++++++



Leo's most important plugins
****************************

Become familiar with Leo's most important plugins:
    
- bookmarks.py manages bookmarks.
- contextmenu.py shows a menu when when right-clicking.
- mod_scripting.py supports @button and @command nodes.
- quicksearch.py adds a Nav tab for searching.
- todo.py handles to-do lists and is a project manager.
- valuespace.py creates an outline-oriented spreadsheet.
- viewrendered.py renders content in the rendering pane.

Move clones to the last top-level node
**************************************

.. _`cloning nodes`: tutorial-pim.html#clones

Focus your attention of the task at hand by `cloning nodes`, including
\@file nodes, then moving those clones so they are the last top-level nodes
in the outline. This allows you to work on nodes scattered throughout an
outline without altering the structure of @file nodes.

Put personal settings myLeoSettings.leo
***************************************

.. _`personal settings`: customizing.html#specifying-settings

Put your `personal settings`_ in myLeoSettings.leo, not leoSettings.leo.

- The leo-settings-leo command opens leoSettings.leo.
- The my-leo-settings-leo command opens myLeoSettings.leo.
- Copy the desired settings nodes from leoSettings.leo to myLeoSettings.leo.

Search for settings in leoSettings.leo
**************************************

leoSettings.leo contains the defaults for all of Leo's
settings, with documentation for each. Searching
leoSettings.leo is thus a good way to find settings.

Use abbreviations
*****************

.. _`abbreviations tutorial`: tutorial-pim.html#using-abbreviations-and-templates

Leo's abbreviations can correct spelling mistakes, expand to multiple lines
or even trees of nodes. Abbreviations can execute scripts and can prompt
for values to be substituted within the abbreviation.
See the `abbreviations tutorial`_ for more details.

Useful commands
+++++++++++++++



The beautify command & @nobeautify directive
********************************************

The @nobeautify directive suppresses beautification of the node in which it appears.

The find-quick-selected command
*******************************

The find-quick-selected (Ctrl-Shift-F) command finds all nodes containing the selected text.

The parse-body command
**********************

The parse-body command parses p.b (the body text of the selected node) into separate nodes.

The pyflakes command
********************

.. _`pyflakes`: https://pypi.python.org/pypi/pyflakes

`pyflakes`_ is a superb programming tool. It checks python files almost instantly.

These settings cause Leo to run pyflakes whenever saving a .py file and to raise a dialog if any errors are found::

    @bool run-pyflakes-on-write = True
    @bool syntax-error-popup = True

The pylint command
******************

.. _`pylint`: https://www.pylint.org/

Leo's pylint command runs `pylint`_ on all `@<file>` nodes in the selected trees.
Pylint runs in the background, so you can continue to use Leo while pylint runs.

The rst3 command
****************

.. _`rst3 command`: tutorial-rst3.html

The `rst3 command`_ converts an @rst tree to a document file.

The sort-siblings command
*************************

The sort-siblings (Alt-A) command sorts all the child nodes of their parent, or all top-level nodes.

Use Alt-N (goto-next-clone) to find "primary" clones
****************************************************

Use Alt-N to cycle through the clones of the present cloned node.
This is a fast way of finding the clone whose ancestor is an @<file> node.

Use cffm to gather outline nodes
********************************

The cff command (aka clone-find-flattened-marked) clones all marked nodes
as a children of a new node, created as the last top-level node. Use this
to gather nodes throughout an outline.

Use Ctrl-P (repeat-complex-command) to avoid key bindings
*********************************************************

Ctrl-P re-executes the last command made from the minibuffer.
You can use this to avoid having to define key bindings.

For example, instead of pressing an @button button, execute
its command from the minibuffer. Now you can re-execute the
button using Ctrl-P.

Scripting tips
++++++++++++++

.. _`launch Leo from a console window`: running.html#running-leo-from-a-console-window

Clearing the Log window
***********************

When developing scripts that use Log window to display results, it is
sometimes useful to clear Log window by inserting the following two lines
at the beginning of your script::

    c.frame.log.selectTab('Log')
    c.frame.log.clearLog()

g.callers() returns a list of callers
*************************************

g.callers() returns the last n callers (default 4) callers of a function or
method. The verbose option shows each caller on a separate line. For
example::
    
    g.trace(g.callers())

You must `launch Leo from a console window`_.

The @button make-md-toc script in LeoDocs.leo
*********************************************

The @button make-md-toc script in LeoDocs.leo writes a markdown table of
contents to the console. You can then copy the text from the console to
your document. The selected outline node should be an `@auto-md` node.

Use @button nodes
*****************

.. _`@button nodes`: tutorial-basics.html#button-and-command-nodes

`@button nodes`_ create commands. For example, `@button my-command` creates
the `my-command` button and the `my-command` command. Within `@button`
scripts, c.p is the presently selected outline node.
**@button nodes bring scripts to data**.

Use @test nodes
***************

.. _`@test nodes`: tutorial-basics.html#test-nodes

`@test nodes`_ create unit tests. They automatically convert the body to a
subclass of unittest.TestCase. Leo's run-* commands execute unit tests.

Use a universal shortcut for your scripts
*****************************************

You can have a personal shortcut to run script while developing it. For
example: put `@key=Alt-4` in headline. If your script grows to several
subnodes, you won't have to select top node every time you wish to run
script. It would be enough to just press your universal shortcut.

Use cff to gather nodes matching a pattern
******************************************

The cff command (aka clone-find-flattened) prompts for a search pattern,
then clones all matching nodes so they are the children of a new last
top-level node. This is a great way to study code.

Use g.pdb from the console
**************************

.. _`Python's pdb debugger`: https://docs.python.org/3/library/pdb.html

g.pdb launches `Python's pdb debugger`_, adapted for Leo.
You must `launch Leo from a console window`_ to use the pdb debugger.

Use g.trace to debug scripts
****************************

The g.trace function prints all its arguments to the console. It's great
for seeing patterns in running code.
You must `launch Leo from a console window`_ to see the output of g.trace.

Use section references sparingly
********************************

Within scripts, use section references only when code must be placed
exactly. Here is a common pattern for @file nodes for python files::

    @first # -*- coding: utf-8 -*-
    <<imports>>
    @others

