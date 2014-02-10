"""
A module that generates scatterplot type data for some curve types,
for use in testing any machine learning code we develope.

It also provides a evaluation metric, sum_squared_diff, which takes lists of
observed y values and predicted y values and returns goodness of fit.
This is the function to be maximized during hill-climb learning.
"""

import random

# Some curve functions

def line(c1,c0,x):
    return c1*x + c0

def parabola(c2,c1,c0,x):
    return c2*(x**2) + c1*x + c0

# Some functions that generate scatterplot data, i.e. [(x,y)] lists.

def line_data(c1,c0,minX,maxX,datapoints,noise):
    data = []
    for i in range (0, datapoints):
        x = (random.random() * (maxX - minX)) + minX
        error = (random.random() - 0.5) * noise
        data.append((x, line(c1,c0,x) + error))
    return data
    
def parabola_data(c2,c1,c0,minX,maxX,datapoints,noise):
    data = []
    for i in range (0, datapoints):
        x = (random.random() * (maxX - minX)) + minX
        error = (random.random() - 0.5) * noise
        data.append((x, parabola(c2,c1,c0,x) + error))
    return data

# An evaluation metric for curve fitting.
# Note that this takes as parameters lists of y-values, not (x,y) pairs.

def sum_squared_diff(list1, list2):
    assert len(list1) == len(list2)
    diff = 0
    for i in range (0, len(list1)):
        diff += (list1[i] - list2[i]) ** 2
    return diff
