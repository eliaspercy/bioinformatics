#!/usr/bin/python
import time
import sys
import numpy
#sys.setrecursionlimit(15000)

# YOUR FUNCTIONS GO HERE -------------------------------------


def c(i,j):
    if i == j == 'A':
        return 3
    elif i == j == 'C':
        return 2
    elif i == j == 'G':
        return 1
    elif i == j == 'T':
        return 2


def mat(seq1, seq2):
    M1 = numpy.zeros((len(seq1) + 1, len(seq2) + 1), numpy.int)
    M2 = numpy.zeros((len(seq1) + 1, len(seq2) + 1), numpy.int)
    for i in range(1, M1.shape[0]):
        for j in range(1, M1.shape[1]):
            diag = M1[i - 1, j - 1] + (c(seq1[i-1],seq2[j-1]) if seq1[i - 1] == seq2[j - 1] else - 3)
            up = M1[i - 1, j] - 4
            left = M1[i, j - 1] - 4
            M1[i, j] = max(diag, up, left, 0)
            # 1 = diagonal [D], 2 = up [U], 3 = left [L], 0 = end [E]
            if max(diag, left, up, 0) == diag:
                M2[i, j] = 1
            if max(diag, left, up, 0) == up:
                M2[i, j] = 2
            if max(diag, left, up, 0) == left:
                M2[i, j] = 3
            if max(diag, left, up, 0) == 0:
                M2[i, j] = 0

    return [M1, M2]


def traceback(i, j, seq1, seq2, M2):
    x = ['', '']
    while i >= 0:
        if M2[i,j] == 1:
            x = [seq1[i-1]+x[0],seq2[j-1]+x[1]]
            i -= 1
            j -= 1

        elif M2[i,j] == 2:
            x = [seq1[i-1]+x[0],'-'+x[1]]
            i -= 1

        elif M2[i,j] == 3:
            x = ['-'+x[0],seq2[j-1]+x[1]]
            j -= 1

        elif M2[i,j] == 0:
            return x
    

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
# To work with the printing functions below the best local alignment should be called best_alignment and its score should be called best_score. 


matrices = mat(seq1, seq2)

M1 = matrices[0]
M2 = matrices[1]

best_score = numpy.amax(M1)

result = numpy.where(M1 == best_score)
listOfCordinates = list(zip(result[0], result[1]))
for cord in listOfCordinates:
    position = (cord)

i = position[0]
j = position[1]


best_alignment = traceback(i, j, seq1, seq2, M2)


#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

