I used the Vietnamese puzzle to learn about multiprocessing programming.  It required me to come up with all possible permutations(combinations) of the digits 1-9 with no duplicate digits (i.e. 124536987 is OK, 122256978 is not).  Then I plugged those possible permutations (all 362880 [9!] of them) into the Vietnamese equation to see which ones solved it. I came up with possible 128 answers.

If I run the program all on one thread/process, it takes about 30 minutes on my 64-bit Linux Mint 17.3 Cinnamon box and Intel Core i5 CPU.  If I split it up into 4 processes, it takes about 8 minutes.

The program runs and then prints out all the permutations and answers to separate .txt files in the same directory.

The program requires Python 3 and the Multiprocessing package (usually already included) for python.

The ProcessAttempt.py file does not run I could not figure out how to get the Process class to work.  The puzzleSolver.py file does run and uses pools to do the multiprocessing.

The fastAsPossible.py uses python's built-in function itertools.permutations to find all the permutations for the digits 1-9.  It runs significantly faster than the brute force method and the entire program takes on average 2.827 seconds to run on my machine with the same specs as above.  It does not use multiprocessing.
