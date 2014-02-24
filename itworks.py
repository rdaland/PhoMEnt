
import AlternateInput as ai
import calc_weights

mt = ai.readDataOnly('phx_train.txt')

ai.augment_sigmak(mt, ['c', 'v'], 6)

newCons = ['[cv]','^v','c$','c c','v v', '^c c', 'c c c$', 'c c c c']

ai.applyMarkList(mt, newCons)

weights = calc_weights.learn_weights(mt)

print(weights)