title: Shameful Past
date: 2005-10-24
tags: python, shame on you, nearest neighbor

A few hours ago, when I was dealing with my thesis, I've come up with a Python function that constructs a tour for a given [TSP](http://www.tsp.gatech.edu/) instance using the [nearest neighbor heuristic](http://en.wikipedia.org/wiki/Nearest_neighbour_algorithm):

    :::python
    def nearestneighbor(size, dists):
       tour = [0]*size
       candy = [True]*size
       candy[0] = False

       for i in range(1, size):
           prev = tour[i - 1]
           tour[i] = min([(dists[prev][c], c)
               for c in range(size) if candy[c] and  c != prev])[1]
           candy[tour[i]] = False

       return tour

Not too bad...
Then I dig into old Python code that I wrote last year, the times when I was quitting C++ and beginning to use Python; and find this piece of code that consists of a class named `Nearestneighbor` doing (almost) the same thing as the function above:

    :::python
    class Nearestneighbor:
       def __init__(self, dists):
           self.__dists = dists
           self.dimension = dists.shape[0]

       def construct(self, startcity = None):
           if startcity is None:
               self.startcity = rnd.randint(self.dimension)
           else: self.startcity = startcity

           self.tour = [self.startcity]
           cities = range(self.dimension)
           del cities[self.startcity]

            while cities:
                ndist = sys.maxint  # nearest :) distance
                nindex = 0  # nearest city's index
                pcity = self.tour[-1]  # previous city
                ndist = self.__dists[pcity,cities[nindex]]

                for i in range(1, len(cities)):
                    dist = self.__dists[pcity,cities[i]]
                    if dist < ndist:
                        nindex = i
                        ndist = dist

                self.tour.append(cities[nindex])
                del cities[nindex]

Well, this is definitely not my favorite piece of Python code ;-)
