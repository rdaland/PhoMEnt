#!/usr/bin/python
# -*- coding: utf-8 -*-

class AllTheThings(object):

    """
    Reads in a file of tab-delimited tableaux.
    Contains the following attributes:
        self.constraints -------- list of constraint names
            this is found on the first line of the input file
        self.constraints_abbrev - list of abbreviated constraint names
            this is found on the second line of the input file
            *DO NOT PUT CANDIDATES ON THE SECOND LINE OF THE INPUT FILE*
        self.weights ------------ a list of weights for constraints
        self.counts ------------- a dictionary {(input-output): frequency}
        self.violations --------- a dictionary {input : {output : violationVector}}
    Contains the following method:
        self.read_megt_file(megt_file) - moves the data from the .txt file to the attributes
            self.weights is not populated, as that is the learning people's job.
    """
    def __init__(self, megt_file=None):
        self.constraints = []
        self.constrainst_abbrev = []
        self.weights = []
        self.counts = {}
        self.violations = {}
        if megt_file:
            self.read_megt_file(megt_file)

    def read_megt_file(self, megt_file):
        """(** formatting conventions **)"""
        with open(megt_file) as f:
            fstr = f.read().rstrip().split('\n') #making list of all rows
            self.constraints = fstr[0].split('\t')[3:] #populating constraints
            self.constrainst_abbrev = fstr[1].split('\t')[3:] #populating constraint abbreviations

            current_i = -1 #wouldn't we want to actually use the phonological form of the input-output pairs?
            i_violations = {}
            for line in fstr[2:]:
                splitline = line.split('\t')
                for index, item in enumerate(splitline):
                    if not item: #enter missing values
                        splitline[index] = 0
                    elif index == 2: #freq to float()
                        splitline[index] = float(item)
                    elif index > 2: #viol to int()
                        splitline[index] = int(item)
                if splitline[0]:
                    if current_i >= 0:
                        self.violations[current_i] = i_violations
                    current_i += 1
                    current_j = 0
                    i_violations = {}
                else:
                    current_j += 1
                self.counts[(current_i,current_j)] = splitline[2]
                i_violations[current_j] = splitline[3:]
            self.violations[current_i] = i_violations
            #I'm worried that a maliciously inept user will duplicate an i-o mapping somewhere else
            #Because candidates are converted into indices by position in the file, this duplication will go unnoticed
            #Potentially problematic if the i-o mapping isn't precisely duplicated.
            #This can be mitigated by using phonological forms of input-output pairs
            #and checking to see if the input is already present in the violation dictionary

            #Wasn't there some discussion between Michael and Robert about removing zero-valued somethings at readin?
att = AllTheThings('toy_input_2.txt')
print(att.constraints)
print(att.counts)
print(att.violations)
