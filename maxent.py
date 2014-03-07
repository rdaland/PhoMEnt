
import argparse
import megatableau
import optimizer

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
parser.add_argument('-L', '--L2', type=float, default=0.0, \
         help='Multiplier for L1 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, \
         help='Precision for gradient search (see docs)')
args = parser.parse_args()

#####################################################################
## Main code
#####################################################################

# Construct MegaTableau
mt = megatableau.MegaTableau(args.input_file_name)

# Optimize mt.weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision)

# Output file
if args.outfile:
    mt.write_output(args.outfile)

