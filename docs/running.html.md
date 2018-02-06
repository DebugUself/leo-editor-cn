.. rst3: filename: docs/running.html

##############
Running Leo
##############

.. index:: Running Leo

This chapter tells how to run Leo and discusses Leo's command-line options.

.. contents:: Contents
    :depth: 3
    :local:

Running Leo
+++++++++++

You can run Leo from a Python interpreter as follows::

    import leo
    leo.run() # runs Leo, opening a new outline or,
    leo.run(fileName=aFileName) # runs Leo, opening the given file name.

Another way to run Leo is as follows::

    cd <path-to-launchLeo.py>
    python launchLeo.py %*

Here are some tips that may make running Leo easier:

**Linux**
    
The following shell script will allow you to open foo.leo files by typing leo foo::

    #!/bin/sh 
    python <leopath>launchLeo.py $1

where <leopath> is the path to the directory containing the leo directory. 

**Windows**

You can associate Leo with .leo files using a batch file. Put the
following .bat file in c:\\Windows::

    <path-to-python>/python <path-to-leo>/launchLeo.py %*

Here <path-to-leo> is the path to the directory *containing* the leo directory,
that is, the directory containing launchLeo.py.

Running Leo the first time
**************************

The first time you start Leo, a dialog will ask you for a unique identifier. If
you are using a source code control system such as git, use your git login name.
Otherwise your initials will do.

Leo stores this identifier in the file .leoID.txt. Leo attempts to create
leoID.txt in the .leo sub-directory of your home directory, then in Leo's config
directory, and finally in Leo's core directory. You can change this identifier
at any time by editing .leoID.txt.

Running Leo in batch mode
*************************

On startup, Leo looks for two arguments of the form::

    --script scriptFile

If found, Leo enters batch mode. In batch mode Leo does not show any windows.
Leo assumes the scriptFile contains a Python script and executes the contents of
that file using Leo's Execute Script command. By default, Leo sends all
output to the console window. Scripts in the scriptFile may disable or enable
this output by calling app.log.disable or app.log.enable

Scripts in the scriptFile may execute any of Leo's commands except the Edit Body
and Edit Headline commands. Those commands require interaction with the user.
For example, the following batch script reads a Leo file and prints all the
headlines in that file::

    path = r"<path-to-folder-containing-the-leo-folder>\\leo\\test\\test.leo"

    g.app.log.disable() # disable reading messages while opening the file
    flag,newFrame = g.openWithFileName(path,None)
    g.app.log.enable() # re-enable the log.

    for p in newFrame.c.all_positions():
        g.es(g.toEncodedString(p.h,"utf-8"))

Running Leo from a console window
*********************************

.. _`associating .leo files with python.exe`: installing.html#creating-windows-file-associations

Leo sends more detailed error messages to stderr,
the output stream that goes to the console window. In Linux and MacOS
environments, python programs normally execute with the console window visible.

On Windows, you can run Leo with the console window visible by `associating .leo files with python.exe`_ *not* pythonw.exe.

The .leo directory
******************

Leo uses os.expanduser('~') to determine the HOME directory if no HOME environment variable exists.

Leo puts several files in your HOME/.leo directory: .leoID.txt, .leoRecentFiles.txt, and myLeoSettings.leo.

Leo's command-line options
++++++++++++++++++++++++++

Leo supports the following command-line options. As usual, you can see the list by typing the following in a console window::

    leo -h

or::

    leo --help

You will get something like the following::

    Usage: launchLeo.py [options] file1, file2, ...

    Options:
      -h, --help            show this help message and exit
      --debug               enable debug mode
      --diff                use Leo as an external git diff
      --fullscreen          start fullscreen
      --ipython             enable ipython support
      --fail-fast           stop unit tests after the first failure
      --gui=GUI             gui to use (qt/qttabs/console/null)
      --listen-to-log       start log_listener.py on startup
      --load-type=LOAD_TYPE @<file> type for loading non-outlines from command line
      --maximized           start maximized
      --minimized           start minimized
      --no-cache            disable reading of cached files
      --no-plugins          disable all plugins
      --no-splash           disable the splash screen
      --screen-shot=SCREENSHOT_FN
                            take a screen shot and then exit
      --script=SCRIPT       execute a script and then exit
      --script-window=SCRIPT_WINDOW
                            open a window for scripts
      --select=SELECT       headline or gnx of node to select
      --session-restore     restore previously saved session tabs at startup
      --session-save        save session tabs on exit
      --silent              disable all log messages
      --trace-binding=BINDING
                            trace key bindings
      --trace-focus         trace changes of focus
      --trace-plugins       trace imports of plugins
      --trace-setting=SETTING
                            trace where setting is set
      --trace-shutdown      trace shutdown logic
      -v, --version         print version number and exit
      --window-size=WINDOW_SIZE
                            initial window size (height x width)

Leo's workbook file
+++++++++++++++++++

If you give no file arguments on the command line Leo will open ``~/.leo/workbook.leo``.  Initially, this file contains Leo's cheat sheet and an example from the rst3 tutorial.

Using sessions
++++++++++++++

A **session** specifies a list of .leo files that Leo opens automatically when Leo first starts. Like this::

    leo --session-save --session-restore <list of .leo files>
    
When Leo closes, it stores session state in ``~/.leo/leo.session``. Session state consists of the list of open files and the selected node in each file. The next time Leo starts with those options, Leo will open these files and will select the appropriate nodes.

