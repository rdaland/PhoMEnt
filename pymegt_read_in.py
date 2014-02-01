#!/usr/bin/python
# -*- coding: utf-8 -*-

class AllTheThings:
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
        f = open(megt_file)
        fstr = f.read().rstrip().split('\n')
        self.constraints = fstr[0].split('\t')[3:]
        self.constrainst_abbrev = fstr[1].split('\t')[3:]

        current_i = -1
        i_violations = {}
        for line in fstr[2:]:
            splitline = line.split('\t')
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

        f.close()


att = AllTheThings('toy_input_1.txt')
print(att.constraints)
print(att.counts)
print(att.violations)