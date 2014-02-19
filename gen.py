'''Several functions for generating subets of sigma star (in list form). Namely:
sigma_k, sigma_0k, sigma_1k each of which takes an alphabet and a value for k, and returns a list.
'''

def sigma_k(alphabet, k):
    '''Returns all words in sigma-k
    '''
    def helper(i):
        if i == 0:
            sigma_i = ['']
        else:
            sigma_i = []
            sigma_h = helper(i - 1)
            for word in sigma_h:
                sigma_i += [word + a for a in alphabet]
        return sigma_i
    return helper(k)

def sigma_0k(alphabet, k):
    '''Returns all words in all sigma-n from n = 0 to k.
    '''
    assert k >= 0
    def helper(i):
        language = ['']
        if i == 0:
            sigma_i = ['']
        else:
            sigma_i = []
            sigma_h, language = helper(i - 1)
            for word in sigma_h:
                new_stuff = [word + a for a in alphabet]
                sigma_i += new_stuff
                language += new_stuff
        return (sigma_i, language)
    return helper(k)[1]

def sigma_1k(alphabet, k):
    '''Return all words in all sigma-n from n = 1 to k.
    '''
    language = sigma_0k(alphabet, k)
    del language[0] # Get rid of empty string
    return language

# Example alphabet
cv = ['C','V']

# Example language
cv6 = sigma_1k(cv,6)
