title: Infix Comparison in Marvin
date: 2005-04-16
tags: marvin, infix

Here is a sample Marvin code that converts an infix expression into postfix.
I have also posted this one to the [InfixComparison](http://factor.sourceforge.net/wiki/index.php?InfixComparison) page of [Concatenative Languages Wiki](http://factor.sourceforge.net/wiki/index.php).
(*Note from the future: Sadly, these links are broken.*)

    :::text
    # infix.mar | Converts an infix expression into postfix

    # This implementation uses the global variable space as a hash-table
    # for operator precedence.

    "listop forth dequeop" use

    @|> globs & pushfrom ;

    @string dfront NONE =
        { iftrue dpushf }
        { else
            dpopf 2dup |>
            { iftrue swap dpushf }
            { else dpushf dpushf }
        } ;

    @list NONE dpushf __postfix_rec
        {
        dfront NONE =
        iffalse
            dpopf
            repeat
        } { else dpopf eat } ;

    @number ;

    @postfix NONE dpushf __postfix_rec dpopfall ;
    @__postfix_rec [ dup type call ] lmap ;


    # define the hash-table for operator precedence
    FALSE ^++ ^+- ^-+ ^-- ^*+ ^*- ^** ^*/ ^/+ ^/- ^/* ://
    TRUE ^+* ^+/ ^-* :-/

    # try one of the examples:
    ( ( 2 '* ( ( 3 '/ 2 ) '+ 4 ) ) postfix )
    dump  # display the stack

