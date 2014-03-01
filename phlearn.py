import argparse

import megatableau
import geneval
import optimizer

# Parse command line arguments
parser = argparse.ArgumentParser(description = 'Maximum entropy harmonic grammar')
parser.add_argument('attested_file_name', help='Name of input file')
parser.add_argument('constraint_file_name', help='Name of constraints file')
parser.add_argument('-a', '--alphabet_file_name', default=None, help='List of segments in alphabet; one per line')
parser.add_argument('-m', '--maxstrlen', default=6, help='Maximum string length in contrast set')

parser.add_argument('-l', '--L1', type=float, default=1.0, help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=None, help='Multiplier for L1 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, help='Precision for gradient search (see docs)')

args = parser.parse_args()


# Create and fill MegaTableau
mt = megatableau.MegaTableau()

# read in attested forms and add to MegaTableau
geneval.read_data_only(mt, args.attested_file_name) 

# get alphabet
if args.alphabet_file_name:
    alphabet = geneval.read_sigma(mt, args.alphabet_file_name)
else:
    alphabet = geneval.read_sigma(mt)

## # add non-attested forms to tableau
geneval.augment_sigma_k(mt, alphabet, args.maxstrlen) 
## TODO: read in constraints and turn them into a list of strings called `constraints`
geneval.apply_mark_list(mt, constraints)

# Write the final MegaTableau to file (optional?)
## TODO: this.

# Optimize weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision) # weights are now stored in mt.weights in the same order as mt.constraints

# Output file
## TODO: construct and output the augmented MEGT input file



"""
The plan for this file:

0) import megatableau.py, geneval.py, optimizer.py
1) parse args
2) make empty megatableau (megatableau.py)
3) using arg1 (training data) update mt (geneval.py)
4) using arg3 (alphabet) and arg4 (k), add non-attested forms to mt (geneval.py) *
5) using arg2 (constraints), add violations to mt (geneval.py)
6) (optionally write mt to file)
7) calculate weights (optimizer.py)
8) output stuff


* Beautiful world: if the user supplies an alphabet file, use it to agument tableau; otherwise, search training data for all segments and use those."""
