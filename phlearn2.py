import argparse
import megatableau
import geneval
import optimizer
import time

'''phlearn2.py is just like phlearn, but prints out how long various steps take.
'''

    ### TIME
mark = time.time()

#####################################################################
## Parse command line arguments
#####################################################################
parser = argparse.ArgumentParser(description = 'Maximum entropy harmonic grammar')
parser.add_argument('attested_file_name', help='Name of input file')
parser.add_argument('constraint_file_name', help='Name of constraints file')
parser.add_argument('-a', '--alphabet_file_name', default=None, help='List of segments in alphabet; one per line')
parser.add_argument('-m', '--maxstrlen', type=int, default=5, help='Maximum string length in contrast set')
parser.add_argument('-o', '--outfile', help='Name of output file')

## weight-setting parameters
parser.add_argument('-l', '--L1', type=float, default=1.0, help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=None, help='Multiplier for L1 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, help='Precision for gradient search (see docs)')

args = parser.parse_args()

    ### TIME
print "Parsed arguments:\t", time.time() - mark, "sec"
mark = time.time()

#####################################################################
## Main code
#####################################################################

# Create and fill MegaTableau
mt = megatableau.MegaTableau()

# read in attested forms and add to MegaTableau
geneval.read_data_only(mt, args.attested_file_name)

    ### TIME
print "Filled the tableau:\t", time.time() - mark, "sec"
mark = time.time()

# get alphabet
if args.alphabet_file_name:
    alphabet = geneval.read_sigma(mt, args.alphabet_file_name)
else:
    alphabet = geneval.read_sigma(mt)

    ### TIME
print "Inferred alphabet:\t", time.time() - mark, "sec"
mark = time.time()

## read in constraints
constraints = geneval.read_constraints(mt, args.constraint_file_name)

    ### TIME
print "Read constraints:\t", time.time() - mark, "sec"
mark = time.time()

## add non-attested forms to tableau
geneval.augment_sigma_k(mt, alphabet, args.maxstrlen)

    ### TIME
print "Gen augmentation:\t", time.time() - mark, "sec"
mark = time.time()

## apply constraints (this is the costliest step...)
geneval.apply_mark_list(mt, constraints)

    ### TIME
print "Computed violations:\t", time.time() - mark, "sec"
mark = time.time()

# Optimize mt.weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision)

    ### TIME
print "Optimized weights:\t", time.time() - mark, "sec"
mark = time.time()

# Write the final MegaTableau to file
if args.outfile:
    mt.write_output(args.outfile)


