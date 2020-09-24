#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------

def al(seq1, seq2):
    i = len(seq1)
    j = len(seq2)
    if i == 0:
        return 1
    elif j == 0:
        return 1
    else:
        return al(seq1[:i-1], seq2[:j]) + al(seq1[:i], seq2[:j-1]) + al(seq1[:i-1], seq2[:j-1])


def f(seq1, seq2, opt, k):
    i = len(seq1)
    j = len(seq2)

    q = opt[0]
    r = opt[1]

    if i == 0:
        k += -4*j
        opt[0] = j*'-' + q
        opt[1] = seq2 + r
        return {k: opt}
    if j == 0:
        k += -4*i
        opt[1] = i*'-' + r
        opt[0] = seq1 + q
        return {k: opt}

    y = {}

    if seq1[i-1] == seq2[j-1] == 'A':
        y.update(f(seq1[:i-1], seq2[:j-1], ['A' + q, 'A' + r], k + 3))
        y.update(f(seq1[:i], seq2[:j-1], ['-' + q, 'A' + r], k - 4))
        y.update(f(seq1[:i-1], seq2[:j], ['A' + q, '-' + r], k - 4))

    elif seq1[i-1] == seq2[j-1] == 'C':
        y.update(f(seq1[:i-1], seq2[:j-1], ['C' + q, 'C' + r], k + 2))
        y.update(f(seq1[:i], seq2[:j-1], ['-' + q, 'C' + r], k - 4))
        y.update(f(seq1[:i-1], seq2[:j], ['C' + q, '-' + r], k - 4))

    elif seq1[i-1] == seq2[j-1] == 'G':
        y.update(f(seq1[:i-1], seq2[:j-1], ['G' + q, 'G' + r], k + 1))
        y.update(f(seq1[:i], seq2[:j-1], ['-' + q, 'G' + r], k - 4))
        y.update(f(seq1[:i-1], seq2[:j], ['G' + q, '-' + r], k - 4))

    elif seq1[i-1] == seq2[j-1] == 'T':
        y.update(f(seq1[:i-1], seq2[:j-1], ['T' + q, 'T' + r], k + 2))
        y.update(f(seq1[:i], seq2[:j-1], ['-' + q, 'T' + r], k - 4))
        y.update(f(seq1[:i-1], seq2[:j], ['T' + q, '-' + r], k - 4))

    elif seq1[i-1] != seq2[j-1]:
        y.update(f(seq1[:i-1], seq2[:j-1], [seq1[i-1] + q, seq2[j-1] + r], k - 3))
        y.update(f(seq1[:i], seq2[:j-1], ['-' + q, seq2[j-1] + r], k - 4))
        y.update(f(seq1[:i-1], seq2[:j], [seq1[i-1] + q, '-' + r], k - 4))

    return y

# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Call any functions you need here, you can define them above.
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
# The number of alignments you have checked should be stored in a variable called num_alignments.


num_alignments = al(seq1, seq2)
x = f(seq1, seq2, ['',''], 0)
best_score = max(x)
best_alignment = x[best_score]


#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Alignments generated: '+str(num_alignments))
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------
