''' A moduled used by maxent.py and phlearn.py to find the ideal weights for a tableau.
'''

import megatableau
import scipy, scipy.optimize
import math
import numpy as np

### HELPER FUNCTIONS FOR CALCULATING PROBABILITY ###

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


### OBJECTIVE FUNCTION(S) ###

def neg_log_probability_with_gradient(weights, tableau, l1_prior=1.0, l2_prior=0.0):
    """ Returns the negative log probability of the data AND a gradient vector.
    This is the objective function used in learn_weights().
    """
    update_maxent_values(weights, tableau)
    logProbDat = 0
    observed = [0 for i in range(len(weights))] # Vector of observed violations
    expected = [0 for i in range(len(weights))] # Vector of expected violations
    data_size = 0 # Number of total data points: the sum of all counts.

    prob_prior = sum([(l1_prior*w) + (l2_prior*(w**2)) for w in weights])
    grad_prior = [(l1_prior) + (2*l2_prior) for w in weights]

    for ur in tableau:
        z = z_score(tableau, ur)
        for sr in tableau[ur]:
            data_size += tableau[ur][sr][0]
            prob = tableau[ur][sr][2] / z
            logProbDat += math.log(prob) * tableau[ur][sr][0]
            for c in range(len(tableau[ur][sr][1])):
                observed[c] += tableau[ur][sr][1][c] * tableau[ur][sr][0]
                expected[c] += tableau[ur][sr][1][c] * prob
    logProbDat += prob_prior

    expected[:] = [x * data_size for x in expected] # multiply expected values by size of data
    gradient = [e-o-p for e, o, p  in zip(expected, observed, grad_prior)] # i.e. -(observed minus expected)

    return (-logProbDat, np.array(gradient))

nlpwg = neg_log_probability_with_gradient # So you don't get carpal tunnel syndrome.

def neg_log_probability(weights, tableau, l1_prior=1.0, l2_prior=0.0):
    """ Returns just the negative log probability of the data.
    This function isn't currently used, it's just here in case you want it.
    """
    return (nlpwg(weights, tableau, l1_prior))[0]

def probability(weights, tableau):
    """ Returns just the probability of the data.
    This function isn't currently used, it's just here in case you want it.
    """
    return math.exp(-(nlpwg(weights, tableau))[0])


### OPTIMIZATION FUNCTION

def learn_weights(mt, L1 = 1.0, L2 = 0.0, precision = 10000000):
    """ Given a filled-in megatableau, return the optimal weight vector.
    """
    # Set up the initial weights and weight bounds (nonpositive reals)
    w_0 = -scipy.rand(len(mt.weights))
    nonpos_reals = [(-25,0) for wt in mt.weights]

    # optimization parameters
    l1_reg = L1 or 1.0        # TODO: logPrior = -l1_reg * sum(weights)
                              # TODO: logPriorGradient = l1_reg * scipy.ones(len(weights))
    l2_reg = L2 or 0.0        # TODO: logPrior -= l2_reg * sum(weights*weights)
                              # TODO: logPriorGradient -= 2*l2_reg * scipy.array(weights)
    prec = precision or 10000000 # TODO: plus prec into optimize call

    # Find the best weights
    learned_weights, fneval, rc = scipy.optimize.fmin_l_bfgs_b(nlpwg, w_0, args = (mt.tableau,l1_reg,l2_reg), bounds=nonpos_reals)

    # Update the mt in place with the new weights
    mt.weights = learned_weights

    # Be sociable
    print "\nBoom! Weights have been updated:"
    for i in range(0,len(learned_weights)):
        print mt.constraints_abbrev[i],"\t",learned_weights[i]
    print "\nLog probability of data:", -(nlpwg(learned_weights, mt.tableau))[0]
    print ""

    # Return
    return learned_weights
