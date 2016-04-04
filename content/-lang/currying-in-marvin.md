title: Currying in Marvin
date: 2005-04-12
tags: marvin, currying

Yesterday, I figured out a way (which was very obvious) to curry a routine in *Marvin*.
First of all, what's currying?

> Currying is named after the logician Haskell Curry. (...)
> The underlying insight of "currying" is that it is possible to treat (almost) every function as a partial function of just one argument.
> All that is necessary for currying to work is to allow the return value of functions to themselves be functions, but with the returned functions *narrowed* or *closer to completion*.
> (...) each successive call to a curried return function *fills in* more of the data involved in a final computation (data attached to a procedure).
>
> [Charming Python, Part 3 by David Mertz](http://www-106.ibm.com/developerworks/linux/library/l-prog3.html)

OK! So we now know what's currying, how to do it in Marvin?
First, an example in [Scheme](http://www.swiss.ai.mit.edu/projects/scheme/) taken from the article [Function Currying in Scheme](http://www.engr.uconn.edu/%7Ejeffm/Papers/curry.html).
The following defines a *curryied* multiplication:

    :::scheme
    (define (times y) (lambda (x) (* y x)))

We can then use this to define a function that doubles its argument.

    :::scheme
    (define (double x) ((times 2) x))

Then we can use "double" just like any other function:

    :::scheme
    (double 5)

Simple, isn't it? But currying is a real headache for non-functional languages; even for Python in some extent. Below is how to do it Marvin:

    :::text
    [ * ] :times
    [ 2 \times ] :double

To call double, just write:

    :::text
    5 \double

How elegant and natural, isn't it?