""" A module that generates executive functions that are simple parabolas, with
easy-to-determine global minima, so that we can see if optimization functions
are working properly.
"""

from __future__ import division
import random


### Functions for generating parabolas.

def get_parabola (c2, c1, c0):
    ''' get_parabola returns a parabolic function that takes a list with just one x-value, 
    and returns a tuple of a y-value, and a length 1 gradient vector.
    '''
    def parabola(xlist):
        x = xlist[0]
        y = (c2 * x**2 + c1 * x + c0)
        gradient = [2 * c2 * x + c1]
        return (y, gradient)
    return parabola

def get_hyper_parabola (c2_c1_tuples, c0):
    ''' get_hyper_parabola returns a parabolic function that takes a vector of n values
    and returns a tuple of a y-value, and a length-n gradient vector.
    '''
    def parabola(xlist):
        y = c0
        gradient = [0 for x in xlist]
        for i in range(0,len(c2_c1_tuples)):
            (c2,c1) = c2_c1_tuples[i]
            x = xlist[i]
            y += c2 * x**2 + c1 * x
            gradient[i] = 2 * c2 * x + c1
        return (y, gradient)
    return parabola


### Functions for determining the actual minima for parabolas, i.e. the "right" answer
### that should be found by a correctly working optimization function.

def correct_parab_min(c2, c1, c0):
    ''' returns the optimal x value for the parabola with the specified constants
    '''
    best_x = (- c1) / (2 * c2)
    return [best_x]

def correct_hyper_parab_min(c2_c1_tuples, c0):
    ''' returns the optimal input vector for the hyperparabola with the specified constants
    '''
    best = [0 for x in c2_c1_tuples]
    for i in range(0,len(c2_c1_tuples)):
        (c2,c1) = c2_c1_tuples[i]
        best[i] = - c1 / (2 * c2)
    return best


### EXAMPLE CALLS ###

parab1 = get_parabola(3,2,1)    # Returns the parabola y = 3x^2 + 2x + 1
parab1([4])                     # Returns y when x = 4, along with a gradient
correct_parab_min(3,2,1)        # Returns the actual x-value for which parab1 is minimized

c2_c1_vect = [(2,2),(3,0)]
c0 = 2

hyperparab1 = get_hyper_parabola(c2_c1_vect, c0)# Returns the hyperparabola y = 2x^2 + 2x + 3z^2 + 0z + 2
hyperparab1([4,5])                              # Returns y when x = 4, z = 5, along with a gradient
correct_hyper_parab_min(c2_c1_vect,c0)          # Returns the actual x-value and z-value for which hyperparab1 is minimized
