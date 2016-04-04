title: Generating All Strings of a Given Alphabet
date: 2005-06-10
tags: python, strings, combination

For a recent research project, I had to write a function that generates all the strings of a given alphabet.
It was (as always) very easy to figure it out in Python, only 5 minutes; below is the code (with modifications, I've polished the idea a bit):

    :::python
    def allstrings(alphabet, length):
        """Find the list of all strings of 'alphabet' of length 'length'"""

        if length == 0: return []

        c = [[a] for a in alphabet[:]]
        if length == 1: return c

        c = [[x,y] for x in alphabet for y in alphabet]
        if length == 2: return c

        for l in range(2, length):
            c = [[x]+y for x in alphabet for y in c]

        return c

Then, suppose you want the possible strings of length 4 of alphabet {1,2,3}; then just write:

    :::python
    allstrings([1,2,3], 4)

And here is the Haskell version:

    :::haskell
    allstrings alphabet n
     | n == 0 = []
     | n == 1 = [alphabet]
     | n == 2 = [[a,b] | a<-alphabet, b<-alphabet]
     | otherwise =
       [[a] ++ b | a<-alphabet, b<-(allstrings alphabet (n - 1))]
