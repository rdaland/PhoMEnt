import math  # so we can do e-exponentiation

# DataProbability.py defines a set of functions for computing the 
# probability of a set of outputs  given some number of inputs.

# weights:    a list of constraint weights
# tableau:    a dictionary of dictionaries of lists {input: {output: [frequency, violations, maxent_value]}}

# since violation vectors are oftentimes sparse, we encode them as dictionaries 
# whose keys are all and only the constraints that a given input-output pair violates.
# pymegt would then fill in the zeroes later.

# violations: a dictionary of positive integers {constraint: violation_count}

### HELPER FUNCTIONS ###

# Computes harmony for a given i/o pair by taking the dot-product
# of its violations and constraint weights.

def calc_harm(tableau, weights, i, j):
    harm = 0
    for v in tableau[i][j][1]:
        harm += weights[v]*tableau[i][j][1][v]
    return harm

# Computes maxent value P* = exp(harmony) for a given i/o pair.

def compute_maxent_val(tableau, weights, i, j):
   return math.exp(calc_harm(tableau, weights, i, j))

# Computes maxent values P* = exp(harmony) for each i/o pair and
# stores it in the tableau in tableau[i][j][2].
   
def compute_maxent_vals(tableau, weights):
    for i in tableau:
        for j in tableau[i]:
            tableau[i][j][2] = compute_maxent_val(tableau, weights, i, j)

# Compute a Z-value by summing the P* values over all outputs for
# a given input. Must run compute_maxent_vals beforehand, or else
# you get the wrong number. tableau[i][j][2] is always initialized
# to 0 for various mechanical reasons....

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

### EXAMPLE WEIGHTS ###
# Set weights to be nonpositive: formula for P* is P* = exp(harm).

weights = {"*VC":0,"*#V":0}
