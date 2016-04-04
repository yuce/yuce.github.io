title: ReportLab on OSX
date: 2012-11-03
tags: python, reportlab, freetype2, osx, tip

It's easy to compile [ReportLab](http://www.reportlab.com/) on OSX (*in my case, 10.8*). The only problem is, you'll get the following warning:

    # installing without freetype no ttf, sorry!
    # You need to install a static library version of the freetype2 software

Don't try to ``brew`` it yet. OSX already has freetype2 installed. We just need to help ReportLab installer to help find it.

Download ReportLab, and insert the following lines around after line 104 (after ``# attempt to make sure we pick freetype2 over other versions``):

    :::plain
    aDir(I, "/usr/X11/include") 
    aDir(L, "/usr/X11/lib")

Remove the ``build`` directory (*if it already exists*) and do ``python setup.py build`` as usual. It should work.


