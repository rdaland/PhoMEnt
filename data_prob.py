"""
data_prob.py defines functions for computing the probability of observed data.
The main function is called 'probability'. It takes arguments (tableau, weights).

tableau:    a dictionary of dictionaries of lists: {input: {output: [frequency, violation vector, maxent_value]}}
weights:    a list of numbers
"""

import math


### HELPER FUNCTIONS ###

# Compute harmony for a given i/o pair by taking the dot-product
# of its violations and the constraint weights.

def calc_harm(tableau, weights, i, j):
    harm = 0
    for c in range (0, len(weights)):
        harm += weights[c] * tableau[i][j][1][c]
    return harm

# Compute maxent value P* = exp(harmony) for a given i/o pair.

def compute_maxent_val(tableau, weights, i, j):
   return math.exp(calc_harm(tableau, weights, i, j))

# Compute maxent values P* = exp(harmony) for each i/o pair and
# stores it in the tableau in tableau[i][j][2].

def compute_maxent_vals(tableau, weights):
    for i in tableau:
        for j in tableau[i]:
            tableau[i][j][2] = compute_maxent_val(tableau, weights, i, j)

# Compute a Z-value by summing the P* values over all outputs for
# a given input. Must run compute_maxent_vals beforehand, or else
# you'll get the wrong number.

def compute_z_score(tableau, i):
    zScore = 0
    for j in tableau[i]:
        zScore += tableau[i][j][2]
    return zScore

# Compute the probability of a given i/o pair by taking P*
# and dividing by the zScore for the given input. Must run
# compute_maxent_vals beforehand.

def compute_prob(tableau, weights, i, j):
    return compute_maxent_val(tableau,weights,i,j)/compute_z_score(tableau,i)

# Compute the probability of the whole data set by taking the product
# of all the input/output probabilities raised to their counts.

def compute_prob_of_data(tableau, weights):
    probDat = 1
    for i in tableau:
        for j in tableau[i]:
            probDat *= compute_prob(tableau,weights,i,j)**tableau[i][j][0] 
    return probDat


### MAIN FUNCTION ###

def probability(tableau, weights):
    compute_maxent_vals(tableau, weights)
    return compute_prob_of_data(tableau, weights)


### EXAMPLE WEIGHTS, TABLEAU ###

ex_tab = {'x': {'a': [1.0, [0,1], 0], 'b': [0.0, [1,0], 0]},
               'y': {'c': [1.0, [1,0], 0], 'd': [0.0, [1,1], 0]}}

ex_weights = [-3.0,-1.0]  # Set all weights to be nonpositive


