'''
Several functions for generating subets of sigma star (in list form). Namely:
sigma_k, sigma_0k, sigma_1k, each of which takes an alphabet and a value for k.
'''

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

# Example alphabet
cv = ['C','V']

# Example language
cv6 = sigma_1k(cv,6)
