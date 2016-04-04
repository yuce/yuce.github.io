title: Infix to Postfix Converter Class in Marvin
date: 2005-04-16
tags: marvin, infix, postfix

Here is an object oriented version of the infix to postfix converter written in Marvin:


    :::text
    # infixoop.mar | Converts an infix expression into postfix

    # This implementation uses the object data as a hash-table
    #    for operator precedence.

    "listop forth dequeop" use

    @@Infix
        @new  # define the hash-table for operator precedence
            FALSE ^++ ^+- ^-+ ^-- ^*+ ^*- ^** ^*/ ^/+ ^/- ^/* ://
            TRUE ^+* ^+/ ^-* :-/ me ;

        @|> & pushfrom ;

        @string dfront NONE =
            { iftrue dpushf }
            { else
                dpopf 2dup me .|>
                { iftrue swap dpushf }
                { else dpushf dpushf }
            } ;

        @list NONE dpushf me .__topostfix_rec
            {
            dfront NONE =
            iffalse
                dpopf
                repeat
            } { else dpopf eat } ;

        @number ;

        @topostfix NONE dpushf me .__topostfix_rec dpopfall ;
        @__topostfix_rec [ dup type callme ] lmap ;
    ;;

    # try one of the examples:
    'Infix new :infix
    ( ( 2 '* ( ( 3 '/ 2 ) '+ 4 ) ) %infix .topostfix )

    dump  # display the stack
