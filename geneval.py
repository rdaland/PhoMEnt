import megatableau
import re

def read_data_only(mt, dataFile):
    """
    update megatableau with io pairs, frequency from user input.
    """
    with open(dataFile) as fileIn:
        for line in fileIn:
            parsed = line.rstrip().split('\t')
            if len(parsed) < 2:
                print "lines need to at least have an ouput and a frequency"
                return
            elif len(parsed) == 2: #only outputs in file
                mt.tableau["NEW-WORD"][parsed[0]] = [float(parsed[1]), None, 0]
            elif len(parsed) == 3: #inputs, outputs, freq
                mt.tableau[parsed[0]][parsed[1]] = [float(parsed[2]), None, 0]

## read in constraints and turn them into a list of strings called `constraints`
def read_constraints(mt, constraintFile):
    """
    update mt.constraints, mt.constraints_abbrev, mt.weights with user input
    """
    with open(constraintFile) as f:
        for line in f:
            splitline = line.rstrip().split('\t')
            if len(splitline) == 1:
                print "we need constraint, weight pairs. Ignoring", splitline
            if len(splitline) == 2:
                if splitline[1]:
                    mt.weights.append(float(splitline[1]))
                else:
                    mt.weights.append(0.0)
                mt.constraints.append(splitline[0])
                mt.constraints_abbrev.append(splitline[0])
    mt.weights = numpy.array(mt.weights)
    #return mt.constraints


def read_sigma(mt, sigmaFile = False):
    'Rip sigma out of a megatableau or a file containing sigma.'
    sigma = []
    if sigmaFile:
        with open(sigmaFile) as fileIn:
            for line in fileIn:
                parsed = line.strip()
                if parsed not in sigma:
                    sigma.append(parsed)
    else:
        for UR in mt.tableau:
            if UR != "NEW-WORD":
                for phone in UR.split():
                    if phone not in sigma:
                        sigma.append(phone)
            for SR in mt.tableau[UR]:
                for phone in SR.split():
                    if phone not in sigma:
                        sigma.append(phone)
    return sigma

def augment_sigma_k(mt, sigma, k):
    'Add all unnatested strings of sigma* up to length k to mt.tableau'
    if len(mt.tableau) > 1:
        print("Can't handle multiple inputs.")
        return False
    possible = sigma_1k(sigma, k)
    for word in possible:
        if word not in mt.tableau["NEW-WORD"]:
            mt.tableau["NEW-WORD"][word] = [0.0, None, 0]

def violations(constraint,word):
    return len(constraint.findall(word))#, overlapped = True))

def apply_mark_list(mt, markList):
    'Apply markedness constraints to each SR in tableau'
    #only add constraint violations if you haven't already added these constraints to the tableau
    if all([con not in mt.constraints for con in markList]):
        for UR in mt.tableau:
            for SR in mt.tableau[UR]:
                if not mt.tableau[UR][SR][1]:
                    mt.tableau[UR][SR][1] = [violations(re.compile(con),SR) for con in markList]
                else:
                    mt.tableau[UR][SR][1].extend([violations(re.compile(con),SR) for con in markList])
        mt.constraints.extend(markList)
        mt.constraints_abbrev.extend(markList)
        mt.weights.extend([0.0 for constraint in markList])


## Below are several functions for generating subets of sigma star (list).
## sigma_k, sigma_0k, sigma_1k: takes an alphabet and a k, return a list.

def sigma_k(alphabet, k):
    'Returns all words in sigma-k'
    def helper(i):
        if i == 0:
            sigma_i = ['']
        else:
            sigma_i = []
            sigma_h = helper(i - 1)
            for word in sigma_h:
                if i > 1:
                    word += ' '
                sigma_i += [word + a for a in alphabet]
        return sigma_i
    return helper(k)

def sigma_0k(alphabet, k):
    'Returns all words in all sigma-n from n = 0 to k.'
    assert k >= 0
    def helper(i):
        language = ['']
        if i == 0:
            sigma_i = ['']
        else:
            sigma_i = []
            sigma_h, language = helper(i - 1)
            for word in sigma_h:
                if i > 1:
                    word += ' '
                new_stuff = [word + a for a in alphabet]
                sigma_i += new_stuff
                language += new_stuff
        return (sigma_i, language)
    return helper(k)[1]

def sigma_1k(alphabet, k):
    'Return all words in all sigma-n from n = 1 to k.'
    language = sigma_0k(alphabet, k)
    del language[0] # Get rid of empty string
    return language




sampleMarkList = ['[cv]','^v','c$','c c','v v', '^c c', 'c c c$', 'c c c c']
