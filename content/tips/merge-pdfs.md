title: Merging PDF Files Using Ghostscript
date: 2009-10-14
tags: pdf, ghostscript, tips

If you have to merge PDF files, you need no other than Ghostscript (which is installed by default with many Linux distributions).
Here's the command line:

    :::text
    gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=firstANDsecond.pdf -dBATCH first.pdf second.pdf