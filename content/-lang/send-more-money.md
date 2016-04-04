title: SEND + MORE = MONEY
date: 2007-05-27
tags: send more money, sendmory, constraint programming, prolog

Finding valid and distinct integers for digits S, E, N, D, M, O, R and Y in the equation SEND + MORE = MONEY is a classical constraint programming problem.
Here's the slightly modified version of the sample program at [Wikipedia constraint programming entry](http://en.wikipedia.org/wiki/Constraint_programming) for [SWI-Prolog](http://www.swi-prolog.org/) using clp library:

    :::prolog
    :- use_module(library('clp/bounds')).

    sendmore(Digits) :-
       Digits = [S,E,N,D,M,O,R,Y],
       Digits in 0..9,
       S #\= 0,
       M #\= 0,
       all_different(Digits),
                    1000*S + 100*E + 10*N + D
                  + 1000*M + 100*O + 10*R + E
       #= 10000*M + 1000*O + 100*N + 10*E + Y,
       label(Digits).

Here's what happens when we load the code and run `sendmore`:

    :::prolog
    ?- consult('money.pl').
    %   library(clp/clp_events) compiled into clp_events 0.00 sec, 2,948 bytes
    %  library(clp/bounds) compiled into bounds 0.03 sec, 90,992 bytes
    % money2.pl compiled 0.03 sec, 91,812 bytes

    Yes
    ?- sendmore(X).

    X = [9, 5, 6, 7, 1, 0, 8, 2] ;

    No

So, 9567 + 1085 = 10652.
AFAI remember, there was a similar question asked to Google's candidate software engineers, which was `WWW + DOT = COM`.
Well, you now know the answer ;)
I'll include both examples for my [PySWIP](http://code.google.com/p/pyswip/) Python package which enables to query SWI-Prolog from Python.
