PhoMEnt
=======
PhoMEnt can 
Maximum entropy phonotactic learner ##I left the name as it is for now (but our program is not a phonotactic learner...)##

Contributors: Dustin Bowers, Robert Daland, Michael Lefkowitz, Jesse Zymet, Yun Kim, Blake Allen, and Paige Fox

Welcome!
This program computes weights & probability of the observed data for constraint-based maxent grammars. 
You make up a grammar consisting of constraints then train it using the program to match a corpus of data. 

1. What You have to do.
Using an input file, you feed the program:
	1) underlying representations with  (see "phx_test.txt" - sample)
	2) possible surface representations for each underlying representation (see "toy_input_#" - sample)
	3) a list of constraints 
		Constraints need to be listed inside the itworks.py script 
		Line #9 newCons = [LIST YOUR CONSTRAINTS HERE]

2. What the program does (script that is used)
	1) it calculates number of violations of each constraint for each candidate  (applyMarkList.py)
	2) it generates a tableau that has underlying representations, surface candidates, their frequencies and violation marks (megatableau.py)
	3) it computes the probability of the observed data (data_prob.py)
	4) it calculates constraint weights (calc_weights)

3. How to run the program
3.1. Required programs
    	1) scipy 
		Download Scipy Stack at
		http://www.scipy.org/install.html
	2) Python
		Download python at
		http://python.org/download/

3.2 Make an input file 
	Make a file that has underlying representations with observed frequencies. Please look at the sample "phx_test.txt". The format is ordinary text, tap-delimited.

3.3 Put constraints in the itworks.py 
	Make constraints and put them in line #9 as a list. Please look at the "ltworks.py" line 9. 
	
3.4 Run itworks.py in python 
	It will give you the probability of the observed data and constraint weights.

THIS README IS ALMOST TOTALLY INFORMATIVE AS TO THE INTERNAL STRUCTURE OF THE REPO. FOR EXAMPLE, IT DOES NOT LIST THE FILES IN THE REPO, OR WHAT ANY OF THEM IS SUPPOSED TO DO, IN EVEN THE MOST GENERAL TERMS. 
