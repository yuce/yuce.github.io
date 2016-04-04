title: Installing Flash on Open Solaris snv_132
date: 2010-02-16
tags: open solaris, flash, firefox

1. Install `SUNWmlib` package.
2. Save `flash_player_10_solaris.x86.tar.gz` from [http://get.adobe.com/flashplayer/](http://get.adobe.com/flashplayer/) to `~/Downloads`.
3. Open a terminal and execute the following:

        :::text
        cd ~/Downloads
        tar xjvf flash_player_10_solaris_x86.tar.bz2
        pfexec cp ~/Downloads/flash_player_10_solaris_r42_34_x86/libflashplayer.so /usr/lib/firefox/plugins

4. Restart Firefox

  