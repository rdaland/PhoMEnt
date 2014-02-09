"""
data_prob.py defines functions for computing the probability of observed data.
The main function is called 'probability'. It takes arguments (tableau, weights).

tableau:    a dictionary of dictionaries of lists: {input: {output: [frequency, violation vector, maxent_value]}}
weights:    a list of numbers
"""

import math

# in the interest of perspicuity, we might want to remove the calc_ and compute_ prefixes from all these function names.

### HELPER FUNCTIONS ###

def calc_harm(tableau, weights, i, j):
    """
    Compute harmony for a given i/o pair by taking the dot-product
    of its violations and the constraint weights.
    tableau - dictionary of input - output pairs and their constraint violation vectors
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - list of floats corresponding to the strength of each constraint
    i ------- input
    j ------- output
    """
    harm = 0
    for c in range (0, len(weights)):
        harm += weights[c] * tableau[i][j][1][c]
    return harm

def compute_maxent_val(tableau, weights, i, j):
    """
    Compute maxent value P* = exp(harmony) for a given i/o pair.
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - vector of floats corresponding to the strength of each constraint
    i ------- input
    j ------- output
    """
   return math.exp(calc_harm(tableau, weights, i, j))

# I strongly recommend we make this function name be more distinct from the above
# maxent_val_repeated()?

def compute_maxent_vals(tableau, weights):
    """
    Compute maxent value P* = exp(harmony) for all i/o pairs in tableau
    Store this in the "maxent value" field for the relevant i/o pair
        i.e. in tableau[i][j][2].
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - vector of floats corresponding to the strength of each constraint
    """
    for i in tableau:
        for j in tableau[i]:
            tableau[i][j][2] = compute_maxent_val(tableau, weights, i, j)

def compute_z_score(tableau, i):
    """
    Compute a Z-value by summing the maxent values over all outputs for
        a given input. 
    Must run compute_maxent_vals() beforehand, or else you'll get the wrong number.
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    i -- input
    """
    zScore = 0
    for j in tableau[i]:
        zScore += tableau[i][j][2]
    return zScore

def compute_prob(tableau, weights, i, j):
    """
    Compute the probability of a given i/o pair by taking P*
        and dividing by the zScore for the given input.
    Must run compute_maxent_vals() beforehand.
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - vector of floats corresponding to the strength of each constraint
    i ------- input
    j ------- output

    """
    return compute_maxent_val(tableau,weights,i,j)/compute_z_score(tableau,i)

#shouldn't we move this to the log-domain?
# aka logProb = sum([tableau[i][j][0]*math.ln(compute_prob(tableau, weights, i, j)) for i in tableau for j in tableau[i]])
# my comprehension of list comprehensions gets bad pretty fast, so I meant to say:
# <in the most nested part of the for-loop> 
# logProb += [tableau[i][j][0]*math.ln(compute_prob(tableau, weights, i, j)

def compute_prob_of_data(tableau, weights):
    """
    Compute the probability of all the data in the tableau.
    Take the product of all the input/output probabilities raised to their counts.
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - vector of floats corresponding to the strength of each constraint    
    """
    probDat = 1
    for i in tableau:
        for j in tableau[i]:
            probDat *= compute_prob(tableau,weights,i,j)**tableau[i][j][0] 
    return probDat


### MAIN FUNCTION ###

def probability(tableau, weights):
    """
    Convenience function.
    First updates the maxent values in the tableau 
        with compute_maxent_vals(),
    Then returns the probability of all the data in the tableau given those maxent values
        with compute_prob_of_data()
    tableau - dictionary of input - output pairs and their constraint violation vectors.
        tableau = {input: {output: [fields]]}}
        fields is defined in docstring at top
    weights - vector of floats corresponding to the strength of each constraint    
    """
    compute_maxent_vals(tableau, weights)
    return compute_prob_of_data(tableau, weights)


### EXAMPLE WEIGHTS, TABLEAU ###

ex_tab = {'x': {'a': [1.0, [0,1], 0], 'b': [0.0, [1,0], 0]},
               'y': {'c': [1.0, [1,0], 0], 'd': [0.0, [1,1], 0]}}

ex_weights = [-3.0,-1.0]  # Set all weights to be nonpositive


