#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

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
        self.tableau = {}
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
                output_violations = {}
                for index, item in enumerate(splitline):
                    if index == 2: #stores freq as floats
                        freq = float(item)
                    elif index > 2: #sets output_violations = {constraint index: number of violations} with integers for values
                        if item:
                            output_violations[self.constraints[index-3]] = int(item)
                if splitline[0]:
                    current_input = splitline[0]
                    self.tableau[current_input] = {} #sets tableau = {input:{input dictionary}}
                self.tableau[current_input][splitline[1]] = [] # sets input dictionary = {output:[output list]}
                self.tableau[current_input][splitline[1]].extend([freq,output_violations,0]) #sets output list = [freq, output_violations]
