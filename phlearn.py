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
parser.add_argument('-t', '--timed', help='Print how much time various parts of the algorithm take.', action="store_true")

## weight-setting parameters
parser.add_argument('-l', '--L1', type=float, default=0.0, help='Multiplier for L1 regularizer')
parser.add_argument('-L', '--L2', type=float, default=1.0, help='Multiplier for L2 regularizer')
parser.add_argument('-p', '--precision', type=float, default=10000000, help='Precision for gradient search (see docs)')
parser.add_argument('-g', '--gaussian_priors_file', type=str, default=None, \
         help='Gaussian priors file name. If specified, maxent.py \
                uses the mu and sigma values in the file instead of \
                standard L1 and L2 priors to learn weights.')

args = parser.parse_args()

### TIMER - keep track of how long each step takes
mark = time.time()

def timer(task):
    print task, "\t", round(time.time() - mark, 4), "sec"
    return time.time()


#####################################################################
## Main code
#####################################################################

# Create and fill MegaTableau
mt = megatableau.MegaTableau()

# read in attested forms and add to MegaTableau
geneval.read_data_only(mt, args.attested_file_name)

if args.timed:
    mark = timer("\n Parsed arguments in")

# get alphabet
if args.alphabet_file_name:
    alphabet = geneval.read_sigma(mt, args.alphabet_file_name)
else:
    alphabet = geneval.read_sigma(mt)

if args.timed:
    mark = timer(" Inferred alphabet in")

## read in constraints
constraints = geneval.read_constraints(mt, args.constraint_file_name)

if args.timed:
    mark = timer(" Read constraints in")

## add non-attested forms to tableau
geneval.augment_sigma_k(mt, alphabet, args.maxstrlen)

if args.timed:
    mark = timer(" Augmented with GEN in")

## apply constraints (this is the costliest step...)
geneval.apply_mark_list(mt, constraints)

if args.timed:
    mark = timer(" Added violations in")

# If Gaussian priors file is provided, read in to a list
if args.gaussian_priors_file:
    mt.read_priors_file(args.gaussian_priors_file)

# Optimize mt.weights
optimizer.learn_weights(mt, args.L1, args.L2, args.precision)

if args.timed:
    mark = timer(" Optimized weights in")

# Write the final MegaTableau to file
if args.outfile:
    mt.write_output(args.outfile)


