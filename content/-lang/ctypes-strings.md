title: Ctypes Strings
date: 2007-05-28
tags: python, ctypes, prolog, pyswip

I've written bulk of [PySWIP](http://code.google.com/p/pyswip/) last summer, it is based on Nathan Denny's `proolog.py`.
This is the first project that I used [ctypes](http://starship.python.net/crew/theller/ctypes/), a fantastic package which allows calling C functions from dynamic libraries that I use to link `libpl.so` (*Linux*) or `libpl.dll` (*Windows*) of [SWI-Prolog](http://www.swi-prolog.org/).
One of the difficulties I had back then was finding the corresponding ctypes code for `PL_get_chars` which is defined at `SWI-Prolog.h` as follows:

    :::c
    PL_EXPORT(int) PL_get_chars(term_t t,
        char **s, unsigned int flags);

I use that function in `queryGenerator`:

    :::python
    answer = (c_char_p*maxsubresult)()
    while PL_get_list(swipl_list, swipl_head, swipl_list):
        PL_get_chars(swipl_head, answer,
            CVT_ALL | CVT_WRITE | BUF_RING)
        bindings.append(cstr2pystr(answer))

And, `cstr2pystr` is a home-madePython function to convert from a C-string to a Python string in an awful way ;)

That was until I've seen this [article](http://www.pererikstrandberg.se/blog/index.cgi?page=PythonCansiCombo) in the [blog](http://www.pererikstrandberg.se/blog/) of a good person called Erik Strandberg.
His article is about using ctypes, and especially using ctypes types which inspired me to write the code below (knowing that a function called `addressof` existed helped much!), thanks Erik :)

    :::python
    answer = c_char_p("\x00"*MAXSTR)
    while PL_get_list(swipl_list, swipl_head, swipl_list):
        PL_get_chars(swipl_head, addressof(answer),
            CVT_ALL | CVT_WRITE | BUF_RING)
        bindings.append(answer.value)
