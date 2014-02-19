"""
data_prob.py defines functions for computing the probability of observed data.
The main functions are called 'probability' and 'neg_log_probability'. Each takes
arguments (weights, tableau).

tableau:    a dictionary of dictionaries of lists: {input: {output: [frequency, violation vector, maxent_value]}}
weights:    a list of numbers
"""

import math


### HELPER FUNCTIONS ###

def maxent_value(weights, tableau, ur, sr):
    """ Compute maxent value P* = exp(harmony) for a particular UR/SR pair.
    """
    harmony = 0
    for c in range (0, len(weights)):
        harmony += weights[c] * tableau[ur][sr][1][c]
    return math.exp(harmony)

def z_score(tableau, ur):
    """ Compute the Z-score for a particular UR, using current maxent values.
    """
    zScore = 0
    for j in tableau[ur]:
        zScore += tableau[ur][j][2]
    return zScore

def update_maxent_values(weights, tableau):
    """ Computes maxent value P* = exp(harmony) for all UR/SR pairs
    in a supplied tableau, and updates the tableau with these values.
    """
    for ur in tableau:
        for sr in tableau[ur]:
            tableau[ur][sr][2] = maxent_value(weights, tableau, ur, sr)


### OBJECTIVE FUNCTIONS ###

def neg_log_probability(weights, tableau):
    """ Returns negative log probability of the data.
    """
    update_maxent_values(weights, tableau)
    logProbDat = 0
    for ur in tableau:
        z = z_score(tableau, ur)
        for sr in tableau[ur]:
            prob = tableau[ur][sr][2] / z
            logProbDat += math.log(prob) * tableau[ur][sr][0] 
    return - logProbDat

def probability(weights, tableau):
    """ Returns probability of the data.
    """
    return math.exp(- neg_log_probability(weights, tableau))


### EXAMPLE WEIGHTS, TABLEAU ###

ex_tab = {'x': {'a': [1.0, [0,1], 0], 'b': [0.0, [1,0], 0]},
               'y': {'c': [1.0, [1,0], 0], 'd': [0.0, [1,1], 0]}}

ex_weights = [-3.0,-1.0]
