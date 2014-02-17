'''
Several functions for generating subets of sigma star (in list form). Namely:
sigma_k, sigma_0k, sigma_1k, each of which takes an alphabet and a value for k.
'''

import itertools

def sigma_k(alphabet, k):
    """Return words in sigma-k. May be necessary to 
    have this function return a generator rather than a list eventually if 
    memory usage becomes a problem.
    """
    return [''.join(tuple) for tuple in itertools.product(alphabet, repeat=k)]

def sigma_0k(alphabet, k):
    """Return all words in all sigma-n from n=1 to k.
    """
    language = []
    for i in range(0, k+1):
        language += sigma_k(alphabet,i)
    return language

def sigma_1k(alphabet, k):
    """Return all words in all sigma-n from n=1 to k.
    """
    language = []
    for i in range(1, k+1):
        language += sigma_k(alphabet,i)
    return language

# Example alphabet
cv = ['C','V']

# Example language
cv6 = sigma_1k(cv,6)
