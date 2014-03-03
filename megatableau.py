#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
import numpy
import optimizer

class MegaTableau(object):

    """
    A representation of tableaux for manipulation by the maxent learner.
    Derived from a file of tab-delimited tableaux.
    Contains the following attributes:
        self.constraints -------- list of constraint names
            this is found on the first line of the input file
        self.constraints_abbrev - list of abbreviated constraint names
            this is found on the second line of the input file
            *DO NOT PUT CANDIDATES ON THE SECOND LINE OF THE INPUT FILE*
        self.weights ------------ a list of weights for constraints
        self.tableau ------------ a dictionary of dictionaries:
            {input: {output: [freq, violVec, maxentScore]}}
            freq = float()
            violations = list of constraint violations (integers).
                Order is order of constraints in self.constraints, etc
            maxentScore = e**harmony. Initialized to zero (because harmony is undefined without weights).
    Contains the following methods:
        self.read_megt_file(megt_file) - moves the data from the .txt file to the attributes
            self.weights is not populated.
        self.read_weights_file(megt_file) - populates self.weights
    """
    
    def __init__(self, megt_file=None):
        """
        megt_file -- a tab-delimited file of tableaux
            follow the OTSoft guidelines for formatting.
            OTSoft guidelines are summarized in class descriptor too.
        """
        self.constraints = []
        #formerly self.constrainst_abbrev
        self.constraints_abbrev = []
        self.weights = []
        self.tableau = defaultdict(dict)
        if megt_file:
            self.read_megt_file(megt_file)

    def read_megt_file(self, megt_file):
        """
        Populates the following attributes with data from megt_file
            self.constraints -------- list of constraint names
            self.constraints_abbrev - list of abbreviations of constraint names
            self.tableau ------------ dictionary: {input: {output: [freq, violVec, maxentScore]}}
        megt_file: string representation of an OTSoft input file.
        """
        with open(megt_file) as f:
            #fstr = f.read().rstrip().split('\n') #making list of all rows
            self.constraints = f.readline().rstrip('\n').split('\t')[3:] #populating constraints
            self.constraints_abbrev = f.readline().rstrip('\n').split('\t')[3:]#populating constraint abbreviations
            self.weights = numpy.zeros(len(self.constraints)) # starting weights
            for line in f:
                splitline = line.rstrip('\n').split('\t')
                if len(splitline) > 3:
                    current_input = splitline[0] if splitline[0] else current_input
                    current_output = splitline[1]
                    freq = float(splitline[2])
                    violations = [float(v) if v else 0.0 for v in splitline[3:]]
                    for blank in range(len(self.constraints)-len(splitline[3:])): #in case the user doesn't add blank tabs
                        violations.append(0.0)
                    self.tableau[current_input][current_output] = [freq,violations,0] #frequency, violations, maxent_val

    def read_weights_file(self, weights_file):
        """
        Read in a file containing (potentially null) constraint weights.
        Each line in the file is either:
            (constraint name)\t(weight)
            or
            (weight)
        In the former case, weights can be in any order as long as the name-weight associations are right.
        In the latter case, the weights must be in the same order as in the MEGT input file.
        Files mixing the two conventions must be in the same order as in the MEGT input file.
        """
        with open(weights_file) as f:
            #to complain about not having all constraint names specified
            constraintFlags = []
            #to cope when constraint names are not specified
            counter = 0
            if len(self.weights) != len(self.constraints):
                print "please run self.read_megt_file() before self.read_weights_file()."
                return
            posDict = {constraint:pos for pos, constraint in enumerate(self.constraints)}
            for line in f:
                splitline = line.rstrip().split('\t')
                flag = False
                if len(splitline) == 1:
                    flag = True
                    if splitline[0]:
                        self.weights[counter] = float(splitline[0])
                if len(splitline) == 2:
                    if splitline[1]:
                        self.weights[posDict[splitline[0]]] = float(splitline[1])
                constraintFlags.append(flag)
                counter += 1
            if any(constraintFlags):
                for pos, conFlag in enumerate(constraintFlags):
                    if conFlag == True:
                        print "constraint", pos, "has no name in weight file, coping ..."

    def write_output(self, file_name):
        ''' Write a text file with the information in the megatableau object
        '''
        file = open(file_name,"w")

        # Add 1st line with constraint names
        file.write("\t\t\t\t\t")
        for constraint in self.constraints:
            file.write(constraint+"\t")
        file.write("\n")

        # Add 2nd line with constraint abbreviations
        file.write("\t\t\t\t\t")
        for constraint_abbrev in self.constraints_abbrev:
            file.write(constraint_abbrev+"\t")
        file.write("\n")

        # Add 3rd line with constraint weights, headers
        file.write("\t\tObs\tExp\tprob\t")
        for weight in self.weights:
            file.write(str(round(weight,3))+"\t")
        file.write("\n")

        # Add inputs, outputs, violations
        for inp in self.tableau:
            file.write(inp) # Add input
            zscore = optimizer.z_score(self.tableau,inp)
            total = 0
            for outp in self.tableau[inp]:          # Count total occurances of this UR
                total += self.tableau[inp][outp][0]
            for outp in self.tableau[inp]:
                obs  = self.tableau[inp][outp][0]
                prob = self.tableau[inp][outp][2] / zscore
                exp  = prob * total
                file.write("\t"+outp+"\t")              # Add output
                file.write(str(obs)+"\t")               # Add observed counts
                file.write(str(round(exp, 1))+"\t")     # Add expected counts
                file.write(str(round(prob, 4))+"\t")    # Add probability
                for viol in self.tableau[inp][outp][1]: # Add violations
                    file.write(str(viol)+"\t")
                file.write("\n")

        # Add data probability
        file.write("\nLog probability: ")
        file.write(str(-optimizer.neg_log_probability(self.weights, self.tableau)))

        # Done
        file.close()
