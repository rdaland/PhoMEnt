import megatableau
import data_prob
import gen
import calc_weights

def readDataOnly(dataFile):
    tableau = megatableau.MegaTableau()
    with open(dataFile) as fileIn:
        for line in fileIn:
            parsed = "\t".split(line)
            if len(parsed) < 2:
                print "lines need to at least have an ouput and a frequency"
                return
            elif len(parsed) == 2: #only outputs in file
                tableau.tableau["NEW-WORD"][parsed[0]] = [parsed[1], None, 0]
            elif len(parsed) == 3: #inputs, outputs, freq
                tableau.tableau[parsed[0]][parsed[1]] = [parsed[2], None, 0]
    return tableau

def applyMarkList(tableau, markList):
    """
    Apply markedness constraints to each SR in tableau
    """
    #only add constraint violations if you haven't already added these constraints to the tableau
    if all([con not in tableau.constraints for con in markList]):
        for UR in tableau:
            for SR in tableau[UR]:
                if not tableau[UR][SR][1]:
                    tableau[UR][SR][1] = [con(SR) for con in markList]
                else:
                    tableau[UR][SR][1].extend([con(SR) for con in markList])
        tableau.constraints.extend(markList)
        tableau.constrants_abbrev.extend(markList)
    return tableau
    
def applyFaithList(tableau, faithList):
    """
    Apply faith constraints to each SR in tableau
    """
    #only add constraint violations if you haven't already added these constraints to the tableau
    if all([con not in tableau.constraints for con in faithList]):
        for UR in tableau:
            for SR in tableau[UR]:
                if not tableau[UR][SR][1]:
                    tableau[UR][SR][1] = [con((UR, SR)) for con in faithList]
                else:
                    tableau[UR][SR][1].extend([con((UR, SR)) for con in faithList])
        tableau.constraints.extend(markList)
        tableau.constrants_abbrev.extend(markList)
    return tableau