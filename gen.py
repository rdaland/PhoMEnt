'''
Several functions for generating subets of sigma star (in list form). Namely:
sigma_k, sigma_0k, sigma_1k, each of which takes an alphabet and a value for k.
'''

import itertools

def sigma_k(alphabet, k):
    '''returns words in sigma-k'''
    if k == 0:
        return ['']
    else:
        language = []
        sublang = sigma_k(alphabet, k - 1)
        for word in sublang:
            language += [word + a for a in alphabet]
        return language

# These two functions call sigma_k lots of times, and as a result,
# lots of values are calcuated redundantly. The efficiency could be
# improved from O(|sigma|*k^3) to O(|sigma|*k^2), and probably should be
# when we move to alphabets bigger than {C,V} or words longer than 6.

def sigma_0k(alphabet, k):
    '''returns words in all sigma-n from n = 0 to k'''
    language = []
    for i in range(0,k+1):
        language += sigma_k(alphabet, i)
    return language

def sigma_1k(alphabet, k):
    '''returns words in all sigma-n from n = 1 to k'''
    language = []
    for i in range(1,k+1):
        language += sigma_k(alphabet, i)
    return language


# These two functions do the same job as sigma_k and sigma_1k, respectively,
# but make use of a function from itertools to do so more efficiently.

def it_sigma_k(alphabet, k):
    """Return words in sigma-k. May be necessary to 
    have this function return a generator rather than a list eventually if 
    memory usage becomes a problem.
    """
    return [''.join(tuple) for tuple in itertools.product(['C', 'V'], repeat=k)]

def it_sigma_1k(alphabet, k):
    """Return all words in all sigma-n from n=1 to k.
    """
    language = []
    for i in range(1, k+1):
        language += it_sigma_k(alphabet,i)
    return language


# Example alphabet
cv = ['C','V']

# Example language
cv6 = sigma_1k(cv,6)


"""
Text below shows some efficiency comparisons of the sigma functions versus it_sigma functions.
Take-away: it_sigma outperforms sigma significantly when the alphabet becomes larger,
but the advantage of it_sigma over sigma lessens as k increases.

>>> timeit("sigma_1k(['C','V'],6)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
0.06314206123352051
>>> timeit("it_sigma_1k(['C','V'],6)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
0.037229061126708984
>>> timeit("sigma_1k(['C','V'],8)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
0.17891502380371094
>>> timeit("it_sigma_1k(['C','V'],8)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
0.14221501350402832
>>> timeit("sigma_1k(['C','V'],12)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
2.4878041744232178
>>> timeit("it_sigma_1k(['C','V'],12)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
2.331766128540039
>>> timeit("sigma_1k(['C','V','X','Y','Z','A','B'],6)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
21.212828874588013
>>> timeit("it_sigma_1k(['C','V','X','Y','Z','A','B'],6)", number=1000, setup="from __main__ import sigma_1k,it_sigma_1k")
0.05199599266052246
"""
