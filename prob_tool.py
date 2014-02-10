"""
A script that can be run from the command line to calculate the probability of a data set.
When calling it, pass it two text files, one with data and one with weights, e.g.

> python prob_tool.py data.txt weights.txt
"""

import sys
import megatableau, data_prob

# Argument parsing
assert len(sys.argv)==3
tableau_file_name = sys.argv[1]
weights_file_name = sys.argv[2]

# Read in data
mt = megatableau.MegaTableau(tableau_file_name)
mt.read_weights_file(weights_file_name)

# Compute and print answer
print data_prob.probability(mt.weights, mt.tableau)
