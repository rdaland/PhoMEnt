""" A test module that verifies everything is working as intended. """

import megatableau
import data_prob

# Test using toy_input_1 and toy_weights_1

megatab1 = megatableau.MegaTableau('toy_input_1.txt')
megatab1.read_weights_file('toy_weights_1.txt')

print data_prob.probability(megatab1.tableau,megatab1.weights)

# Test using toy_input_2 (which is missing 0s) and toy_weights_2 (which has no constraint names)

megatab2 = megatableau.MegaTableau('toy_input_2.txt')
megatab2.read_weights_file('toy_weights_2.txt')

print data_prob.probability(megatab2.tableau,megatab2.weights) 
