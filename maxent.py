import megatableau
import optimizer

# Parse command line argument
## TODO: parse one argument: `input_file_name` is the name of the MEGT input file

# Construct MegaTableau
mt = megatableau.MegaTableau(input_file_name)

# Optimize weights
optimizer.learn_weights(mt) # weights are now stored in mt.weights in the same order as mt.constraints

# Output file
## TODO: construct and output the augmented MEGT input file




"""
The plan for this file:

0) import megatableau.py, optimizer.py
1) parse arguments
2) construct megatableau from arg1 (megatableau.py)
3) calculate weights (optimizer.py)
4) output stuff"""