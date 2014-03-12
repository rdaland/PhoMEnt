PhoMEnt
=======

Maximum Entropy Phonotactic Learner

Contributors:  Robert Daland, Michael Lefkowitz, Blake Allen, Jesse Zymet, Dustin Bowers, Yun Kim, and Paige Fox

Welcome to PhoMEnt!

CONTENTS:
	1) Command line tool for learning weights in a maximum entropy harmonic grammar (maxent.py)
	2) Command line tool for basic phonotactic learner following Hayes and Wilson 2008 (phlearn.py)
	3) Source code that supports 1 and 2 above (megatableau.py, optimizer.py, geneval.py)
	4) Example files (*.txt)

PREREQS:
	To use PhoMEnt, you will need Python 2.7, and the Python module scipy.
	These can be acquired from:
		http://python.org/download/
		http://www.scipy.org/install.html
		NOTE: installing scipy can be a major headache.
			We highly recommend using a distribution like Enthought Canopy 
			(https://www.enthought.com/products/canopy/).
			Canopy is free for users with a .edu email address.
			Be warned: other Python installations may not see packages installed by Canopy.

HIGH-LEVEL SUMMARY OF FUNCTIONALITY:
	maxent.py
		Reads in a user-defined tableau file.
		Weights the constraints to maximize the probability of the data in the tableaux.
		The tableau file must follow the format of OTSoft 
			EXAMPLES: maxent_tableau1.txt, maxent_tableau2.txt
			(http://www.linguistics.ucla.edu/people/hayes/otsoft/)
			See also "MAKING USER-DEFINED FILES" below.
			Excel files are not accepted.
				You must convert such files to tab-separated .txt files.
				This can be done by selecting the filled in parts of your excel sheet,
				And copy-paste to a text editor window.
					Mac users ... TextEdit makes .rtf files by default
					You will need to convert to .txt by pressing "apple-shift-T"
				Save this file.
			Mac/other *nix users rejoice, this program won't complain about your newlines.
	phlearn.py
		Reads in user-defined surface forms and user-defined constraints.
			EXAMPLE: phlearn_train1.txt / phlearn_cons1.txt
			EXAMPLE: phlearn_train2.txt / phlearn_cons2.txt
		Weights the constraints to maximize the probability of the data 
			The candidate set is all possible words up to length 5 by default.
		Constraints must follow regular expression syntax

COMMAND LINE HOW-TO:
	Open up your favorite command line interpreter.
		On a Mac, the default is "Terminal". 
			It can be found in Applications/Utilities
		On Windows, the default is "Command Prompt".
			In Windows 8.1, it can be found in "Start Menu\Programs\System Tools
		On Linux, I assume you know what the command line is.
	cd to the PhoMEnt folder
		(Google "cd command line YOUR OPERATING SYTEM HERE" if you don't know what this means) 
	Depending on what you want to do, type one of the following:
		
		python maxent.py tableau.txt
		python phlearn.py training_data.txt constraints.txt
		
			(where tableau.txt, training_data.txt, constraints.txt stand for actual names of files)
			If you store your files outside of PhoMEnt, you need to write the full file path
	Hit the "Enter" key
	
ACCESSING MORE OPTIONS:
	To see how to use extra options, type:

		python maxent.py -h
		python phlearn.py -h
	
	If you want to write your results to a file (rather than to the terminal window), type one of:

		python maxent.py tableau.txt -o output.txt
		python phlearn.py observed.txt constraint.txt -o output.txt
	
	Be warned, this will overwrite any file with the same name in this location.
	
	All other options can be specified using similar syntax (-letter optionSpecification)
	Currently, priors and precision can be changed in both maxent.py and phlearn.py
	For phlearn.py, you can also modify the maximum string length for possible words and the alphabet of segments for possible words.

MAKING USER-DEFINED FILES:
	maxent.py needs an OTSoft-style file. Format a .txt file as follows:
	Line 1:
		3 empty columns (tabs), followed by tab-separated constraint names
	Line 2:
		3 empty columns (tabs), followed by tab-separated constraint names
		*DO NOT PUT CANDIDATES ON THE SECOND LINE OF THE INPUT FILE*
	Line 3...Line n:
		UR, SR, frequency, constraint violations (tab delimited)
		*Constraint violations must be whole numbers*
		*Zero violations can be left unspecified.*
		*Zero frequencies can be left unspecified.*
		*To avoid trouble, make sure the total number of tabs (columns) is consistent between lines*
		*After the first specification of a UR on line n, lines n+m do not need to be specified.*
	Unlike the java version of the MaxEnt grammar tool, constraint files are not necessary here.


	phlearn.py needs a file with observed outputs + frequencies, and a file with constraints
	Format the outputs file as follows:
	Line 1 ... Line n:
		observed form, real number frequency (tab separated)
			each phone in the observed form must be separated from adjacent phones by a space.
			e.g.: sh i n
	All frequencies must be specified
	Format the constraints file as follows:
	Line 1 ... Line n:
		regular expression
			Make sure each regular expression will not be thrown off by spaces in outputs.
	Unlike the java version of the MaxEnt grammar tool, constraint files only contain the constraints.
	Note that there is currently no way to specify mu and sigma for a constraint.
	While there is a way to specify starting weights, this is not available on the command line.
	Default starting weights can be changed from 0, but not through the command line tools

