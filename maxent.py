
import argparse

import megatableau
import optimizer

# Parse command line arguments
parser = argparse.ArgumentParser(description = 'Maximum entropy harmonic grammar')
parser.add_argument('input_file_name', help='Name of input file')

## the following are parameters for the weight-setting step
parser.add_argument('-l', '--L1', type=float, default=1.0, help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=None, help='Multiplier for L1 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, help='Precision for gradient search (see docs)')

args = parser.parse_args()




# Construct MegaTableau
mt = megatableau.MegaTableau(args.input_file_name)

# Optimize weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision) # weights are now stored in mt.weights in the same order as mt.constraints

# Output file
## TODO: construct and output the augmented MEGT input file




"""
The plan for this file:

0) import megatableau.py, optimizer.py
1) parse arguments
2) construct megatableau from arg1 (megatableau.py)
3) calculate weights (optimizer.py)
4) output stuff"""
