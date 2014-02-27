import megatableau
import geneval
import optimizer

# Parse command line arguments
## TODO: parse four arguments: `tableau_file_name`, `constraint_file_name`, `alphabet` (optional), `k` (optional?)

# Create and fill MegaTableau
mt = megatableau.MegaTableau()
geneval.read_data_only(mt, tableau_file_name) # read in attested forms and add to MegaTableau
## TODO: figure out alphabet if not provided, and/or get a default value for k if it's not provided
geneval.augment_sigma_k(mt, alphabet, k) # add non-attested forms to tableau
## TODO: read in constraints and turn them into a list of strings called `constraints`
geneval.apply_mark_list(mt, constraints)

# Write the final MegaTableau to file (optional?)
## TODO: this.

# Optimize weights
optimizer.learn_weights(mt) # weights are now stored in mt.weights in the same order as mt.constraints

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