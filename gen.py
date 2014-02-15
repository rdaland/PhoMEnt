'''
Several functions for generating subets of sigma star (in list form).
'''

import copy

# python's "append" updates lists in place rather than returning a new list,
# which means code like this doesn't work in Python:

# for word in sublanguage:
#     for letter in alphabet:
#         new_word = word.append(letter)
#         language.append(new_word)

# Anyone know of a better alternative than using copy.copy? 

def sigma_k(alphabet, k):
    '''returns the words in sigma k'''
    if k == 0:
        return [[]]
    else:
        language = []
        sublang = sigma_k(alphabet, k - 1)
        for word in sublang:
            for letter in alphabet:
                new_word = copy.copy(word)
                new_word.append(letter)
                language.append(new_word)
        return language

def sigma_0k(alphabet, k):
    '''returns the words in sigma n for all n from 0 to k'''
    if k == 0:
        return [[]]
    else:
        language = []
        sublang = sigma_0k(alphabet, k - 1)
        for word in sublang:
            language.append(word)
            for letter in alphabet:
                new_word = copy.copy(word)
                new_word.append(letter)
                language.append(new_word)
        return language

def sigma_1k(alphabet, k):
    '''returns the words in sigma n for all n from 1 to k'''
    language = sigma_0k(alphabet, k)
    language.remove([])
    return language
