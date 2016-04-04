title: 99 Bottles of Beer on the Wall
date: 2005-04-16
tags: marvin, 99 bottles

The following is one of the ways to do *99 bottles of beer* in Marvin.
If you don't know what I mean, check [99 Bottles of Beer on the Wall](http://www.westnet.com/mirrors/99bottles/beer.html).

    :::text
    99 ^beers
    {
    %beers 0 >
    iftrue
        " bottle(s) of beer" & dup " on the wall," & println
        "." & println
        "Take one down, pass it around," println
        %beers -- ^beers
        repeat
    }

    "No more beers left." println
