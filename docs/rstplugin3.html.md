.. rst3: filename: docs/rstplugin3.html

######################
rst3 Command Reference
######################

.. _`rst3 tutorial`: tutorial-rst3.html

Please read the `rst3 tutorial`_ before reading this chapter.

This chapter covers advanced settings and features of the rst3 command. It is for power users only.

*Are you sure you want to read this chapter?* The tutorial covers everything most people need to know about the rst3 command. Leo's own documentation uses none of the features discussed here.

.. contents:: Contents
    :depth: 4
    :local:

Options
+++++++

This section discusses options--what they are, how to set them and how to set their defaults.

General options
***************

Here is a complete list of options for the rst3 and code-to-rst commands:

.. glossary::
    :sorted:

``call_docutils (default: True)``
    Call docutils to process the intermediate file.

``default_path (default: '')``
    The path to be prepended to filenames given in root nodes.

``default_encoding (default: utf-8)``
    The default encoding to be used for non-ascii (unicode characters).

``generate_rst (default: True)``
    A master switch. **True**: generate rST markup for rST sections and rST code-blocks. **False**: generate plain text and ignore ``@ @rst-markup`` doc parts.

``generate_rst_header_comment (default: True)``
    **True**: Leo writes a comment line of the form ``.. rst3: filename: <filename>`` at the start of intermediate files. This option has effect only if the ``generate_rst`` and ``write_intermediate_file`` options are both True.

``publish-argv-for-missing-stylesheets (Default: '')``
    The arguments to be passed to ``docutils.core.Publisher().publish()`` when no stylesheet is in effect. This is a string that represents a comma-separated list of strings: For example, the option::

        publish-argv-for-missing-stylesheets=--language=de,--documentclass=report,--use-latex-toc

    results in the call::

        publish(['--language=de','--documentclass=report','--use-latex-toc'])

``show_headlines (default: True)``
    **True**: automatically generate rST sections from headlines. **False**: ignore headlines.
    
    **Note**: The level of the node in the outline determines the level of the section underlining in the rST markup. Higher-level headlines in the outline correspond to higher-level section headings; lower-level headlines in the outline correspond to lower-level section headings.

``show_organizer_nodes (default: True)``
    **True**: generate rST sections for nodes that do not contain body text. *This option has no effect unless the rST section would otherwise be written*.

``show_sections (default: True)``
    **True**: generate rST sections corresponding to headlines. **False**: Generate lines of the form ``headline`` instead of sections.
    
``silent (default: False)``
    Write only the number of files written and the time taken to the log and console.

``strip_at_file_prefixes (default: True)``
    **True**: remove ``@auto``, ``@file``, ``@clean``, and ``@thin`` from the start of headlines.

``stylesheet_name (default: 'default.css')``
    The name of the stylesheet passed to docutils.

``stylesheet_path (default: '')``
    The directory containing the stylesheet passed to docutils.
    
    **Note**: If the ``stylesheet_embed`` option is True, specify a path relative to the location of the Leo file. If the ``stylesheet_embed`` option is False, specify a path relative to the location of the HTML file.

``stylesheet_embed (default: True)``
    **True**: The content of the stylesheet file will be embedded in the HTML file. **False**: The HTML file will link to an external stylesheet file.

``underline_characters (default: #=+*^~"'\`-:>\_)``
    The underlining characters to be used to specify rST sections. The first character is reserved so you can specify the top-level section explicitly.

``verbose (default: True)``
    **True**: write informational messages to the log as well as the console.

``write_intermediate_file (default: False)``
    Tells whether to write an intermediate file.
    
    **True**: writes the intermediate file to the external file system. The name of the intermediate file has the name of the output file with ``.txt`` appended. This option has effect only if the ``generate_rst option`` is True.

Headline commands
*****************

Any headline that starts with @rst- controls the rst3 command.

.. glossary::
    :sorted:

..  @rst-code <section> 
..      Enter code mode. (Code mode is covered in the advanced topics sections)
..      Create a section if the show_headlines option is True.

``@rst-ignore <ignored-text>``
    Ignore the node, but *not* its descendants.

``@rst-ignore-node <ignored-text>``
    Same as `@rst-ignore`.

``@rst-ignore-tree <ignored-text>``
    Ignore the node and its descendants.

``@rst-no-head <ignored-text>``
    Ignore the headline but not the body text of this node. *This option has no effect on descendant nodes*.

``@rst-no-headlines <ignored-text>``
    Ignore the headline of this node and descendant nodes.
    
``@rst-table <ignored text>``
    Ignore headlines and write exactly one newline at the end of this node and all descendant nodes. Very useful for creating rST tables.

``@rst-option <option> = <value>``
    Set a single option to the given value. The default value is True.

``@rst-options <ignored-text>``
    Set options from body text. The body text should contain nothing but
    lines of the form ``<option>=<value>``

``@rst-preformat <ignored-text>``
    Format the body text of the node as computer source code. In effect, this option adds a line containing '::' at the start of the body text. The option then indents all following lines. *This option has no effect on descendant nodes*.

..  @rst-rst
..      Enter rst mode. (Rst mode is the mode of operation discussed in the tutorial.)
..      Create a section if the show_headlines option is True.

Option doc parts
****************

**Option doc parts** set rst3 options. Option doc parts start with ``@ @rst-options`` followed by lines of the form ``name=value``. Comment lines starting with ``..`` are allowed. For example::

    @ @rst-options
    .. This comment line is ignored.
    show_headlines=False
    show_leo_directives=False
    verbose=True
    @c

This is a real Leo doc part. Like all other doc parts an option doc part starts with ``@`` and continues until the end of body text or until the next ``@c``.

Settings give defaults for options
**********************************

Settings in leoSettings.leo or myLeoSettings.leo specify the defaults to be used for all rst3 options.  The form of these settings is::

    @bool rst3_<option name> = True/False
    @string rst3_<option name> = aString

That is, to create a default value for an rst3 setting, you must prefix the option name with ``rst3_``.  For example::

    @bool rst3_write_intermediate_file = True

Http plugin options
*******************

The following options are for the use of Bernhard Mulder's http plugin. The http plugin creates an http server running on a local port, typically 8130. When the http plugin is running you will see a purple message in the log window that looks something like this::

    http serving enabled on port 8130...

To use the http plugin, start a web browser and enter this url::

    http://localhost:8130/

You will see a a top level page containing one link for every open .leo file. Clicking on a link will cause the http server to pass a new page to the browser. You can use the browser's refresh button to update the top-level view in the browser after you have opened or closed files.

**Important**: See the docstring for the http plugin for information on configuring the plugin. Some of the following rst3 settings must match values of settings for the http plugin.

Here are the rst3 options that support the http plugin:

.. glossary::

``http_server_support (default: False)``
    A master switch: none of the following options have any effect unless this option is True. If True, the rst3 command does the following:

- Writes **node markers** in the rst output for use by the http plugin. Node markers are rst named hyperlink targets. By default they look like: ``.. _http-node-marker-N``, where N is a unique node number.

- Adds additional information to all nodes of the tree being formatted using Leo's unknownAttributes mechanism.

``http_attributename (default: rst_http_attribute)``
    The name of the attribute name written to the ``unknownAttributes`` attribute of each outline node in the rst root tree. The default is ``rst_http_attribute``. It should match this setting: ``@string rst_http_attributename = rst_http_attribute``.

``clear_http_attributes (default: False)``
    **True**: the rst3 command initially clears the fields specified by `http_attributename`.  

``node_begin_marker (default: http-node-marker-)``
    The string used for node markers.

Section expansion options
*************************

The following options allow you to expand noweb section references, much like Leo itself does. The rst3 command ensures that unbounded expansions can not happen. While expanding any section, the rst3 will not expand again any sections that have already occurred in the expansion.

``expand_noweb_references``
   True: Replace references by definitions. Definitions must be descendants of the referencing node.

``ignore_noweb_definitions``
    True: ignore section definition nodes.

``expand_noweb_recursively``
    True: recursively expand definitions by expanding any references found in definitions.
        
**Note**: This is an experimental feature: all aspects might changed. The defaults for all these options ensure that the rst3 command works as it has always.

Other topics
++++++++++++



Markup doc parts
****************

**Markup doc parts** have the following form::

    @ @rst-markup
    any rST markup
    @c

Markup doc parts inserts the markup directly into the output. Markup doc parts are most useful when formatting an outline as code using the code-to-rst command.

Required cascading style sheets
*******************************

HTML files generated by the rst3 command assume that three .css (cascading style sheet) files exist in the same directory. For the HTML output to look good the following .css files should exist:

- default.css is the default style sheet that docutils expects to exist.

- leo_rst.css contains some style improvements based on Gunnar Schwant's DocFactory.

.. - silver_city.css is the style sheet that controls the syntax highlighting generated by SilverCity.

The latter two style sheets are imported at the end of the default.css.

**Important:** You can use cascading style sheets to do things that otherwise wouldn't be possible with "plain" rST. For instance, the background color of this page was specified in a body style.

Controlling the rst3 command from scripts
*****************************************

A new method has been added to make it more easily to write rST code from scripts::

    c.rstCommands.writeNodeToString(p)

``writeNodeToString`` scans p's tree (p defaults to presently selected node) looking for @rst nodes. When the first @rst node is found, writeNodeToString processes the node as usual, with the following changes:

- @rst need not be followed by a filename; any filename and its extension are *ignored*.

- Only the ext argument to writeNodeToString determines the type of output produced. The valid values for the ext argument are None (for rst output), '.html', '.pdf', and '.tex'.

- Instead of writing the result to a file, writeNodeToString returns the tuple (p,s), where p is the node whose tree produced the output, and s is the output itself.

- writeNodeToString returns after processing at most one @rst node.

Scripts can easily use writeNodeToString to convert @rst trees into various kinds of output. For example::

    p,s = c.rstCommands.writeNodeToString(p,ext='html')

Notes:

- This script scans the presently selected tree for @rst nodes. In particular, if the presently selected tree does not contain an @rst node the search continues in parent trees. When an @rst node is found, it converts the node (and descendants) to html and returns p, the found @rst node and s, the html itself.

- Valid values for the ext argument are ".html", ".tex" or None (specifies rst output)

- There is some support for ext=".pdf", but this is experimental code.  Expect crashes.

Further study
+++++++++++++

.. _ListManagerDocs.html: http://leoeditor.com/ListManagerDocs.html
.. _wxListManager.leo:    http://leoeditor.com/wxListManager.leo

The file `ListManagerDocs.html`_ is an impressive example of the kind of output that can be generated relatively easily using the rst3 command.

The source for ListManagerDocs.html is `wxListManager.leo`_. **Important**: wxListManager.leo was written for the old rst2 plugin; it could be greatly simplified if adapted for the rst3 command.

This documentation was created using the rst3 command. The source code for this documentation is in LeoDocs.leo. The source code for the rst3 command is in leoRst.py in leoPy.leo.

Theory of operation
+++++++++++++++++++

Leo 5.1 substantially simplifies the code in leoRst.py. The only rules:

- All top-level commands must call rst.initSettings, which calls rst.preprocessTree.
- Code that writes body text must call rst.init_write.

``rst.d0``
    This dictionary contains the defaults for each option. Keys are the option name, *not* including the ``rst3_`` prefix. Settings in @settings trees update its entries.
    
``rst.dd``
    A dictionary of dictionaries. Keys are vnodes. Values are a dictionary of settings set in that *particular* vnode.

``rst.getOption(p,name)``
    Searches the ``rst.dd`` and ``rst.d0`` dicts, starting at ``p``, looking for an entry for ``name``. This greatly simplifies the code that creates ``rst.dd``. Surprisingly, this search makes the code about 50% faster.

Advanced topics
+++++++++++++++

The section covers complex options arising from two equivalent problems:

- How to generate documentation from computer source code in a Leo outline.
- How to embed documentation in computer source code in a Leo outline.

*Please stop reading now if these problems don't interest you!*

Modes
*****

The rst3 command supports three different modes.

``rst mode``
    The default mode, as discussed in the Tutorial. The rst3 command treats body text as rST (or Sphinx) markup.
    
``code mode``
    The rst3 command treats body text as computer source code, generating the appropriate rST or Sphinx markup. Code mode is inherently complex. It supports *many* options.
    
``doc-only mode``
    The rst3 command outputs only regular doc parts and @ @rst-markup doc parts. Headlines create section in doc_only mode only if:

1. The node contains a doc part or

2. The show_organizer_nodes option is in effect.

The code_mode and doc_only_mode options determine the mode as follows:

``code_mode=False; doc_only_mode=False (the default)``
    Enters rst mode.
    
``code_mode=False; doc_only_mode=True``
    Enters doc_only mode.

``code_mode=True; (doc_only_mode ignored)``
    Enters code mode.

Code mode options
*****************

The following options have effect only in code mode.

.. glossary::
    :sorted:

``number_code_lines (default: True)``
    Controls whether to number code lines in code mode. *This option has no effect in rst mode*.

``show_leo_directives (default: True)``
    True: include Leo directives False: ignore Leo directives.

``show_markup_doc_parts (default: False)``
    True: include markup doc parts. False: ignore markup doc parts.

``show_options_doc_parts (default: False)``
    True: include options doc parts. False: ignore options doc parts.

``show_doc_parts_as_paragraphs (default: False)``
    True: Move doc parts outside of the code-block directive. False: Show doc parts in the code-block directive.
    
    **Cool**: Any rST markup in doc parts included as the result of this option will be rendered properly.

``show_options_nodes (default: False)``
    True: show @rst-options nodes. False: Ignore @

Rst mode options
****************

The following option has effect only in rst mode.

.. glossary::

``show_doc_parts_in_rst_mode [True,False or class names] (default: True)``
    This option is most useful for rst documents which are not computer code. It allows you to use doc parts to make comments on the draft document which are either excluded from the output or formatted in a way that highlights their nature as comments rather than content. For example, you're writing a book, and you want to use a doc part at the top of a section to remind yourself "need to explain how Ted got to Sally's". Note: you may need to add CSS to have them formatted differently.

    The option can be `True`, `False`, or one or more class names.
    
    **True**: Treat the entire doc part from the opening '@' to the closing '@c
    as normal markup.
    
    **False**: Remove the doc part.

    **class names**: Process the contents of the doc part as it if were in an rst `container` directive. For example::

         @ @rst-options
         show_doc_parts_in_rst_mode = notes literal
         @c

This would wrap the doc part contents in the output in a div with classes "container notes literal". Furthermore, if one of the class names is ``literal``, then the doc part content will be output as a literal block wrapped in a container as described above. This allows you to use text which is not valid rst as rough notes for annotating a draft document.

The code-block directive
************************

The rst3 command defines a code-block rST directive. The primary purpose of this directive is to show formatted source code.

In rst mode you can insert the code-block directive like any other rST markup. The rst3 command generates code-block directives automatically in code mode. This directive takes one argument, a language name.  Like this::

    .. code-block:: Python

        import leo.core.leoPlugins as leoPlugins
        import leo.core.leoGlobals as g

The output looks like this::

    import leo.core.leoPlugins as leoPlugins
    import leo.core.leoGlobals as g

.. _`Scripting Tutorial`:   tutorial-scripting.html

See the `Scripting Tutorial`_ for many examples of how to use code-blocks.

Acknowledgements
++++++++++++++++

Josef Dalcolmo wrote the initial rst plugin. Timo Honkasalo, Bernhard Mulder, Paul Paterson, Kent Tenney and Steve Zatz made contributions to the rst and rst2 plugins.

