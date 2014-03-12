
import argparse
import megatableau
import optimizer
import sys

#####################################################################
## Parse command line arguments
#####################################################################
parser = argparse.ArgumentParser(description = \
         'Maximum entropy harmonic grammar')
parser.add_argument('input_file_name', help='Name of input file')
parser.add_argument('-o', '--outfile', help='Name of output file')

## weight-setting parameters
parser.add_argument('-l', '--L1', type=float, default=0.0, \
         help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=1.0, \
         help='Multiplier for L2 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, \
         help='Precision for gradient search (see docs)')
parser.add_argument('-w', '--weights_file', type=str, default=None, \
         help='Weight file name. If specified, maxent.py calculates the \
                probability of the data using them, and does not \
                attempt to learn weights.')
parser.add_argument('-g', '--gaussian_priors_file', type=str, default=None, \
         help='Gaussian priors file name. If specified, maxent.py \
                uses the mu and sigma values in the file instead of \
                standard L1 and L2 priors to learn weights.')
args = parser.parse_args()

#####################################################################
## Main code
#####################################################################

# Construct MegaTableau
mt = megatableau.MegaTableau(args.input_file_name)

# If weights are provided, return the probability of the tableau
if args.weights_file:
    mt.read_weights_file(args.weights_file)
    print('Probability: '+str(optimizer.probability(mt.weights, \
            mt.tableau, args.L1, args.L2)))
    sys.exit()

# If Gaussian priors file is provided, read in to a list
if args.gaussian_priors_file:
    mt.read_priors_file(args.gaussian_priors_file)

# Optimize mt.weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision)

# Output file
if args.outfile:
    mt.write_output(args.outfile)

