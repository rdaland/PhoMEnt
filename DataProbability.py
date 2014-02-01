import math  # so we can do e-exponentiation

# DataProbability.py defines a set of functions for computing the 
# probability of a set of tableau, given three inputs. The main function 
# is "probability" (way at the bottom) which takes three arguments:

# weights:    a list of constraint weights
# violations: a dictionary {input : {output : violationVector}}
# counts:     a dictionary {(input-output): frequency}


### FUNCTIONS ###

# Compute harmonies by dot-producting violations and constraint weights
# for each input/output pair.
def computeHs(weights,violations):
    hs = {}
    for i in violations:
        hs[i] = {}
        for j in violations[i]:
            h = 0
            for c in range(0, len(weights)):
                h += weights[c] * violations[i][j][c]
            hs[i][j] = h
    return hs

# Compute z-values by summing the exp(harmony) of all outputs for
# each input, and return a dictionary {input : {output : harmony}}
def computeZs(harmonies):
    zs = {}
    for i in harmonies:
        z = 0.0
        for j in harmonies[i]:
             z += math.exp(harmonies[i][j])
        zs[i] = z
    return zs

# Compute input/output probabilities by dividing exp(harmony) by Z,
# and return a dictionary {(input-output): probability}
def computePrs(harmonies,zVals):
    probs = {}
    for i in harmonies:
        for j in harmonies[i]:
            probs[(i,j)] = math.exp(harmonies[i][j]) / zVals[i]
    return probs

# Compute the probability of the whole data set by taking the product
# of all the input/output probabilities raised to their counts
def computePrOfData(probs,counts):
    probDat = 1
    for (i,j) in counts:
        probDat *=  probs[(i,j)] ** counts[(i,j)]
    return probDat


### MAIN FUNCTION ###
def probability(weights,violations,counts):
    harmonies = computeHs(weights,violations)
    zVals = computeZs(harmonies)
    probs = computePrs(harmonies,zVals)
    return computePrOfData(probs,counts)


### EXAMPLE INPUTS / FUNCTION CALL ###

weights1 = [1.0,2.0,3.0]
violations1 = {1: {1:[0,1,0],2:[0,0,1]}, 2: {1:[1,0,0],2:[1,1,0]}}
counts1 = {(1,1):1, (1,2):0, (2,1):3, (2,2):3}

print probability(weights1,violations1,counts1)


