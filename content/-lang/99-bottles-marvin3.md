title: 99 Bottles of Beer in Marvin3
date: 2005-09-29
tags: marvin3, marvin, 99 bottles

How to write 99 bottles of beer in Marvin3?

    :::text
    :bottles dup dup 1 > [" bottles"] [" bottle"] ifte cat ;

    :sing
        bottles dup " of beer on the wall," cat println
        " of beer. " cat println
        "Take one down, pass it around." println ;

    :theend  "No more beer left." println ;

    :beers  [dup 0 >] [sing decr] while theend eat ;

    # start singing
    99 beers

Also you may check [a previous post](/99-bottles-of-beer-on-the-wall.html) for *the original* Marvin.
Other languages? [99 Bottles of Beer on the Wall](http://www.westnet.com/mirrors/99bottles/beer.html) lists many.
See [99 Bottles of Beer on Wikipedia](http://en.wikipedia.org/wiki/99_Bottles_of_Beer).