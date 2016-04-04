title: Freeeze for Marvin3
date: 2005-10-17
tags: marvin3

Today, I added a keyword called *freeze* to Marvin3.
Basically, when called inside a routine, it pops the top element from the stack and replaces routine's code with a word that pushes that value onto the stack.
This way we can create a *write-once* routine, which is similar to C#'s `readonly` modifier (*value is allowed to be set once*).
Consider the following example:

    :::text
    :YOUR-NUMBER input int freeze ;

    "Enter a number:" prints YOUR-NUMBER
    YOUR-NUMBER " is a nice number!" cat println


Notice that, although `YOUR-NUMBER` is a routine, when called, it just pushes the same value determined when it is first called.

Here is a more complex one. The following set of class and routines implement a generator that returns subsequent numbers starting from 1 (*then 2, 3, ...*):

    :::text
    @__generate 0 !n [%n incr ^n] dup ;
    :_generate __generate freeze ;
    :generate _generate call ;

The Python equivalent is (although using generators would be better):

    :::python
    class _generate:
        def __init__(self):
            self.n = 0
        def __call__(self):
            self.n += 1
            return self.n

    generate = _generate()
