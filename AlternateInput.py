import megatableau
import data_prob
import gen
import calc_weights
import re

def readDataOnly(dataFile):
    tableau = megatableau.MegaTableau()
    with open(dataFile) as fileIn:
        for line in fileIn:
            parsed = line.rstrip().split('\t')
            if len(parsed) < 2:
                print "lines need to at least have an ouput and a frequency"
                return
            elif len(parsed) == 2: #only outputs in file
                tableau.tableau["NEW-WORD"][parsed[0]] = [float(parsed[1]), None, 0]
            elif len(parsed) == 3: #inputs, outputs, freq
                tableau.tableau[parsed[0]][parsed[1]] = [float(parsed[2]), None, 0]
    return tableau

def augment_sigmak(mt, sigma, k):
    if len(mt.tableau) > 1:
        print("Can't handle multiple inputs.")
        return False
    possible = gen.sigma_1k(sigma, k)
    for word in possible:
        if word not in mt.tableau["NEW-WORD"]:
            mt.tableau["NEW-WORD"][word] = [0.0, None, 0]

def violations(constraint,word):
    return len(constraint.findall(word))#, overlapped = True))

def applyMarkList(mt, markList):
    """
    Apply markedness constraints to each SR in tableau
    """
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
    return mt
    
def applyFaithList(mt, faithList):
    """
    Apply faith constraints to each SR in tableau
    """
    #only add constraint violations if you haven't already added these constraints to the tableau
    if all([con not in mt.constraints for con in faithList]):
        for UR in mt.tableau:
            for SR in mt.tableau[UR]:
                if not mt.tableau[UR][SR][1]:
                    mt.tableau[UR][SR][1] = [con((UR, SR)) for con in faithList]
                else:
                    mt.tableau[UR][SR][1].extend([con((UR, SR)) for con in faithList])
        mt.constraints.extend(markList)
        mt.constrants_abbrev.extend(markList)
    return mt

samplemarklist = ['[cv]','^v','c$','c c','v v']

samplemarklist2 = ['^c c', 'c c c$', 'c c c c']