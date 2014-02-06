#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

class MegaTableau(object):

    """
    Reads in a file of tab-delimited tableaux.
    Contains the following attributes:
        self.constraints -------- list of constraint names
            this is found on the first line of the input file
        self.constraints_abbrev - list of abbreviated constraint names
            this is found on the second line of the input file
            *DO NOT PUT CANDIDATES ON THE SECOND LINE OF THE INPUT FILE*
        self.weights ------------ a list of weights for constraints
        self.tableau ------------ a dictionary of dictionaries:
           {input: {output: [count, {constraint: number of violations}, P*]}}
    Contains the following method:
        self.read_megt_file(megt_file) - moves the data from the .txt file to the attributes
            self.weights is not populated, as that is the learning people's job.
    """
    def __init__(self, megt_file=None):
        self.constraints = []
        self.constrainst_abbrev = []
        self.weights = []
        self.tableau = defaultdict(dict)
        if megt_file:
            self.read_megt_file(megt_file)

    def read_megt_file(self, megt_file):
        """(** formatting conventions **)"""
        with open(megt_file) as f:
            fstr = f.read().rstrip().split('\n') #making list of all rows
            self.constraints = fstr[0].split('\t')[3:] #populating constraints
            self.constrainst_abbrev = fstr[1].split('\t')[3:] #populating constraint abbreviations

            for line in fstr[2:]:
                splitline = line.split('\t')
                current_input = splitline[0] if splitline[0] else current_input
                current_output = splitline[1]
                freq = float(splitline[2])
                violations = [int(v) if v else 0 for v in splitline[3:]]
                self.tableau[current_input][current_output] = [freq,violations,0] #frequency, violations, maxent_val

    def read_weights_file(self, weights_file):
        """Read in a file containing constraint weights.
        Each line in the file is either:
            (constraint name)\t(weight)
            or
            (weight)
        In the former case, weights can be in any order as long as the name-weight associations are right.
        In the latter case, the weights must be in the same order as in the MEGT input file.
        Files mixing the two conventions will throw an exception.
        """
        with open(weights_file) as f:
            slines = [line.split('\t') for line in f.read().rstrip().split('\n')]
            try:
                self.weights = [float(sline[0]) for sline in slines]
            except ValueError:
                try:
                    weights_dict = {constraint: float(weight) for constraint,weight in slines}
                    self.weights = [weights_dict[constraint] for constraint in self.constraints]
                except:
                    raise Exception("Input file not in one of the standard formats.")

