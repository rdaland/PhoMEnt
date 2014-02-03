import math  # so we can do e-exponentiation

# DataProbability.py defines a set of functions for computing the 
# probability of a set of tableau, given three inputs. The main function 
# is "probability" (way at the bottom) which takes three arguments:

# weights:    a list of constraint weights
# violations: a dictionary {input : {output : violationVector}}
# counts:     a dictionary {(input-output): frequency}


### HELPER FUNCTIONS ###

# Compute maxent values P* = exp(harmony) for each i/o pair by taking the
# dot-product of its violations * constraint weights, and exponentiating.
def compute_maxent_vals(weights,violations):
    maxVals = {}
    for i in violations:
        maxVals[i] = {}
        for j in violations[i]:
            harm = 0
            for c in range(0, len(weights)):
                harm += weights[c] * violations[i][j][c]
            maxVals[i][j] = math.exp(harm)
    return maxVals

# Compute Z-values by summing the P* values of all outputs for a
# given input, and return a dictionary {input : {output : harmony}}
def compute_z_scores(maxVals):
    zScores = {}
    for i in maxVals:
        z = 0.0
        for j in maxVals[i]:
             z += maxVals[i][j]
        zScores[i] = z
    return zScores

# Compute input/output probabilities by dividing P* by Z,
# and return a dictionary {(input-output): probability}
def compute_probs(maxVals,zScores):
    probs = {}
    for i in maxVals:
        for j in maxVals[i]:
            probs[(i,j)] = maxVals[i][j] / zScores[i]
    return probs

# Compute the probability of the whole data set by taking the product
# of all the input/output probabilities raised to their counts
def compute_prob_of_data(probs,counts):
    probDat = 1
    for (i,j) in probs:
        probDat *=  probs[(i,j)] ** counts[(i,j)]
    return probDat


### VERIFY INPUT IS LEGAL ###
def input_is_ok(weights,violations,counts):
    numberOfCons = len(weights)
    stillOkay = True
    for i in violations:
        for j in violations[i]:
            if not len(violations[i][j]) == numberOfCons:
                stillOkay = False
                print "Error: i/o pair",i,j,"has the wrong number of violations."
            if not ((i,j) in counts.keys()):
                stillOkay = False
                print "Error: counts has no key for i/o pair",(i,j)
    return stillOkay


### MAIN FUNCTION ###
def probability(weights,violations,counts):
    if input_is_ok(weights,violations,counts):
        maxVals = compute_maxent_vals(weights,violations)
        zScores = compute_z_scores(maxVals)
        probs = compute_probs(maxVals,zScores)
        return compute_prob_of_data(probs,counts)
    else: return 0


### EXAMPLE INPUTS / FUNCTION CALL ###

# weights1 = [1.0,2.0,3.0]
# violations1 = {1: {1:[0,1,0],2:[0,0,1]}, 2: {1:[1,0,0],2:[1,1,0]}}
# counts1 = {(1,1):1, (1,2):0, (2,1):3, (2,2):3}

# print probability(weights1,violations1,counts1)
