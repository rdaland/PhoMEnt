import sys
import megatableau, data_prob
import scipy, scipy.optimize

# Argument parsing
assert len(sys.argv)==2
tableau_file_name = sys.argv[1]

# Read in data
mt = megatableau.MegaTableau(tableau_file_name)
w_0 = -scipy.rand(len(mt.weights))
nonpos_reals = [(-25,0) for wt in mt.weights]

def one_minus_probability(weights, tableau):
    return 1.0-data_prob.probability(weights, tableau)

def negative_probability(weights, tableau):
    return -data_prob.probability(weights, tableau)

learned_weights = scipy.optimize.fmin_tnc(data_prob.probability, w_0, args = (mt.tableau,), bounds=nonpos_reals, approx_grad=True)

print(learned_weights)

# print("Probability given weights found by the original MEGT:")
# print(data_prob.probability([-2.19,-0.43], mt.tableau))