import sys
import megatableau, data_prob
import scipy, scipy.optimize

# Argument parsing
assert len(sys.argv)==2
tableau_file_name = sys.argv[1]

# Read in data
mt = megatableau.MegaTableau(tableau_file_name)

learned_weights = scipy.optimize.fmin_tnc(data_prob.probability, -scipy.rand(len(mt.weights)), args = (mt.tableau))
# TypeError: probability() takes exactly 2 arguments (3 given)

print(learned_weights)