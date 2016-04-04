title: Getting the Currently Playing Song Info on Amarok via DCOP
date: 2009-08-13
tags: python, DCOP, amarok, KDE

Here's a sample application for using DCOP with Python.
Needed to install [python-dcop](http://packages.debian.org/search?keywords=python-dcop) on Debian.
It works on KDE 3.5 with Amarok 1.4 (*won't work on KDE 4*)

    :::python
    import pydcop

    playerService = pydcop.DCOPObject('amarok', 'player')

    d = dict(
       title=playerService.title(),
       artist=playerService.artist(),
       album=playerService.album()
    )
    print '%(artist)s - %(title)s (%(album)s)' % d

**kdcop** is a great application to discover DCOP services.

I've posted a slightly extended version of this entry to [Active State Python Cookbook](http://code.activestate.com/recipes/576878/).