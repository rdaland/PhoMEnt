import megatableau
import geneval as ai
import optimizer

mt = megatableau.MegaTableau()

ai.read_data_only(mt, 'phx_train.txt')

constraints = ai.read_constraints(mt, 'toy_constraints.txt')

ai.augment_sigma_k(mt, ['c', 'v'], 6)

##newCons = ['[cv]','^v','c$','c c','v v', '^c c', 'c c c$', 'c c c c']
##
ai.apply_mark_list(mt, constraints)

weights = optimizer.learn_weights(mt)

print(weights)
