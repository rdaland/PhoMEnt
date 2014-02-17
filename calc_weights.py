import sys
import megatableau, data_prob
import scipy, scipy.optimize

# Argument parsing
assert len(sys.argv)==2
tableau_file_name = sys.argv[1]

# Read in data
mt = megatableau.MegaTableau(tableau_file_name)

# Set up the initial weights and weight bounds (nonpositive reals)
w_0 = -scipy.rand(len(mt.weights))
nonpos_reals = [(-25,0) for wt in mt.weights]

# Learn
learned_weights, fneval, rc = scipy.optimize.fmin_tnc(data_prob.neg_log_probability, w_0, args = (mt.tableau,), bounds=nonpos_reals, approx_grad=True)

print(learned_weights)

# print("Probability given weights found by the original MEGT:")
# print(data_prob.probability([-2.19,-0.43], mt.tableau))