title: Compiling Python Extension Modules on Mac OSX 10.6
date: 2011-05-27
tags: python, mac, osx 10.6, tricks

If you get the following error when you are compiling a Python C extension module in Mac OSX 10.6:

    /gcc/darwin/ppc/as or /usr/bin/../local/libexec/gcc/darwin/ppc/as) for architecture ppc not installed
    Installed assemblers are:
    /usr/bin/../libexec/gcc/darwin/x86_64/as for architecture x86_64
    /usr/bin/../libexec/gcc/darwin/i386/as for architecture i386
    spammodule.c:63: fatal error: error writing to -: Broken pipe compilation terminated.

Run setup.py as follows:

    ARCHFLAGS="-arch i386 -arch x86_64" python setup.py build
