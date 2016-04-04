title: PySWIP: Facts and Rules
date: 2009-10-08
tags: python, prolog, pyswip

[PySWIP](http://code.google.com/p/pyswip/) is a Python module which enables accessing [SWI-Prolog](http://www.swi-prolog.org/)'s foreign language interface using our beloved computer language.
Here's a small tutorial on adding facts and rules to prolog knowledgebase.

First, adding facts and rules, based on examples in a [Prolog tutorial](http://www.doc.gold.ac.uk/~mas02gw/prolog_tutorial/prologpages/rules.html).


    :::python
    from pyswip import Prolog
    p = Prolog()

    # something is fun if it is a car and it is red.
    p.assertz('(fun(X) :- red(X), car(X))')

    # facts...
    p.assertz('car(vw_beatle)')
    p.assertz('car(ferrari)')
    p.assertz('car(hyundai)')
    p.assertz('bike(harley_davidson)')
    p.assertz('red(ferrari)')
    p.assertz('red(vw_beatle)')
    p.assertz('blue(hyundai)')

Find all cars in the knowledgebase:

    :::python
    print list(p.query('car(Which)'))

Outputs:

    :::python
    [{'Which':'vw_beatle'}, {'Which':'ferrari'}, {'Which':'hyundai'}]

Find all fun things:

    :::python
    print list(p.query('fun(What)'))

Outputs:

    :::python
    [{'What':'vw_beatle'}, {'What':'ferrari'}]

Pretty easy, huh? ;) There are more complex Prolog examples in [PySWIP source distribution](http://code.google.com/p/pyswip/downloads/list), including a sudoku solver.