title: Another Currying Example in Marvin
date: 2005-04-12
tags: marvin, currying

Please see my [previous post](/currying-in-marvin.html) before if you haven't done so.

I've quoted David Mertz's article [Charming Python](http://www-106.ibm.com/developerworks/linux/library/l-prog3.html) in my previous post.
In that article, (besides other things) a [Haskell](http://www.haskell.org/) function is curryied as:

    :::haskell
    computation a b c d = (a + b^2+ c^3 + d^4)

Then it is *filled* as follows:

    :::haskell
    fillOne   = computation 1
    fillTwo   = fillOne 2
    fillThree = fillTwo 3
    answer    = fillThree 5

and the answer is 657. The same thing can be done in Marvin:

    :::text
    [ swap 2 ** + swap 3 ** + swap 4 ** + ] :computation
    [ 1 \computation ] :fillOne
    [ 2 \fillOne ] :fillTwo
    [ 3 \fillTwo ] :fillThree
    5 \fillThree
