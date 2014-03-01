import argparse

import megatableau
import geneval
import optimizer

#####################################################################
## Parse command line arguments
#####################################################################
parser = argparse.ArgumentParser(description = 'Maximum entropy harmonic grammar')
parser.add_argument('attested_file_name', help='Name of input file')
parser.add_argument('constraint_file_name', help='Name of constraints file')
parser.add_argument('-a', '--alphabet_file_name', default=None, help='List of segments in alphabet; one per line')
parser.add_argument('-m', '--maxstrlen', default=6, help='Maximum string length in contrast set')
parser.add_argument('-o', '--outfile', help='Name of output file')

## weight-setting parameters
parser.add_argument('-l', '--L1', type=float, default=1.0, help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=None, help='Multiplier for L1 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, help='Precision for gradient search (see docs)')

args = parser.parse_args()

#####################################################################
## Main code
#####################################################################

# Create and fill MegaTableau
mt = megatableau.MegaTableau()

# read in attested forms and add to MegaTableau
geneval.read_data_only(mt, args.attested_file_name) 

# get alphabet
if args.alphabet_file_name:
    alphabet = geneval.read_sigma(mt, args.alphabet_file_name)
else:
    alphabet = geneval.read_sigma(mt)

## read in constraints
constraints = geneval.read_constraints(mt, args.constraint_file_name)

## add non-attested forms to tableau
geneval.augment_sigma_k(mt, alphabet, args.maxstrlen) 

## apply constraints (this is the costliest step...)
geneval.apply_mark_list(mt, constraints)

# Optimize mt.weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision)

# Write the final MegaTableau to file
if args.outfile:
    mt.write_output(args.outfile)


