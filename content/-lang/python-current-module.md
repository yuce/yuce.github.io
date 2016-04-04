title: Getting the Current Module in Python
date: 2009-10-15
tags: python, tips

Say, you want to insert a function, class or any other object into the current module dynamically.
How can you do that? Of course, you start with getting the module name:

    :::python
    myName = globals()['__name__']

Then, get the module itself:

    :::python
    import sys
    me = sys.modules[myName]

OK, you got the module, now insert something in it:

    :::python
    setattr(me, 'hello', lambda x: 'Hello %s'%x)

We can call hello in our module from now on:

    :::python
    print hello('World')