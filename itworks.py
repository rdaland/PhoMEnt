
import alt_input as ai
import calc_weights

mt = ai.read_data_only('phx_train.txt')

ai.augment_sigma_k(mt, ['c', 'v'], 6)

newCons = ['[cv]','^v','c$','c c','v v', '^c c', 'c c c$', 'c c c c']

ai.apply_mark_list(mt, newCons)

weights = calc_weights.learn_weights(mt)

print(weights)
