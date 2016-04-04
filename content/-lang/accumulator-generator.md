title: Accumulator Generator
date: 2005-04-26
tags: marvin, accumulator generator, Paul Graham

In his [accumulator generator](http://www.paulgraham.com/accgen.html) page, Paul Graham compares several languages to solve a particular problem that is quoted below
(apparently, he has chosen this example in favor of his new Lisp-like language [Arc](http://www.paulgraham.com/arc.html)):

> The problem: Write a function foo that takes a number n and returns a function that takes a number i, and returns n incremented by i.
>
> Note: (a) that's number, not integer, (b) that's incremented by, not plus.

My trial with Marvin was a failure, and could not satisfy all the 5 requirements given [here](http://www.paulgraham.com/accgensub.html).
But now with Marvin2 (a rewrite of the language) this can be accomplished with the following line:

    :::text
    @foo !n [ %n + ^n ] ;

Nice... You can then run the sample code like this:

    :::text
    1 'foo new !x
    5 \x
    3 'foo new
    2.3 \x println

And the result is 8.3, as expected.