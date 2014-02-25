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

def neg_log_probability_with_gradient(weights, tableau):
    """ Returns the negative log probability of the data AND a gradient vector.
    """
    update_maxent_values(weights, tableau)
    logProbDat = 0
    observed = [0 for i in range(len(weights))] # Vector of observed violations
    expected = [0 for i in range(len(weights))] # Vector of expected violations
    data_size = 0 # Number of total data points: the sum of all counts.
    for ur in tableau:
        z = z_score(tableau, ur)
        for sr in tableau[ur]:
            data_size += tableau[ur][sr][0]
            prob = tableau[ur][sr][2] / z
            logProbDat += math.log(prob) * tableau[ur][sr][0]
            for c in range(len(tableau[ur][sr][1])):
                observed[c] += tableau[ur][sr][1][c] * tableau[ur][sr][0]
                expected[c] += tableau[ur][sr][1][c] * prob
    expected[:] = [x * data_size for x in expected] # multiply expected values by size of data
    #print observed
    #print expected
    gradient = [x - y for x, y in zip(observed, expected)] # i.e. observed minus expected
    return (-logProbDat, gradient)

nlpwg = neg_log_probability_with_gradient # So you don't get carpal tunnel syndrome.

def neg_log_probability(weights, tableau):
    """ Returns the negative log probability of the data.
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
    """ Returns the probability of the data.
    This function just makes a call to neg_log_probability, and
    transforms the results out of the log space.
    """
    return math.exp(- neg_log_probability(weights, tableau))


### EXAMPLE WEIGHTS, TABLEAU ###

'''
ex_tab is a tableau that looks like this:

      #   C1 C2 
x a | 1 | 0  1
  b | 0 | 1  0
y c | 1 | 1  0
  d | 0 | 1  1
'''

ex_tab = {'x': {'a': [1.0, [0,1], 0], 'b': [0.0, [1,0], 0]},
          'y': {'c': [1.0, [1,0], 0], 'd': [0.0, [1,1], 0]}}

ex_weights = [-3.0,-1.0]
