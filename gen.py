''' Several functions for generating subets of sigma star (in list form). Namely:
sigma_k, sigma_0k, sigma_1k each of which takes an alphabet and a value for k, and returns a list.
'''

def sigma_k(alphabet, k):
    '''returns words in sigma-k'''
    def helper(i):
        if i == 0:
            ilang = ['']
        else:
            ilang = []
            hlang = sigma_k(alphabet, k - 1)
            for word in hlang:
                ilang += [word + a for a in alphabet]
        return ilang
    return helper(k)

def sigma_0k(alphabet, k):
    '''Return all words in all sigma-n from n=1 to k.'''
    assert k >= 0
    def helper(i):
        language = []
        if i == 0:
            ilang = ['']
            language = ['']
        else:
            ilang = []
            hlang, language = helper(i - 1)
            for word in hlang:
                ilang += [word + a for a in alphabet]
                language += [word + a for a in alphabet]
        return (ilang, language)
    return helper(k)[1]

def sigma_1k(alphabet, k):
    '''Return all words in all sigma-n from n=1 to k.'''
    assert k > 0
    def helper(i):
        language = []
        if i == 0:
            ilang = ['']
            language = [] #Only difference for sigma 1k
        else:
            ilang = []
            hlang, language = helper(i - 1)
            for word in hlang:
                ilang += [word + a for a in alphabet]
                language += [word + a for a in alphabet]
        return (ilang, language)
    return helper(k)[1]

# Example alphabets
cv = ['C','V']
alpha = ['a','b','c','d','e','f','g']

# Example language
cv6 = sigma_0k(cv,6)
