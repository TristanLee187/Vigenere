# Program to determine the frequency of each letter when the input text is split into x piles.
#
# To run:
# $python3 freqAnalysis.py text x
# where text is the plaintext or ciphertext and x is a possible length of the key, so also the number of piles to split
# the text into.
#
# Output:
# $Frequencies:
# $Pile 1  Pile 2  Pile 3  Pile 4
# $char: a char: b char: c char: d
# .
# .
# .
# where the column underneath "Pile N" represents the frequencies of letters in that pile. Letters are sorted by
# non-increasing frequency


import sys
# import time
# t1=time.time()


#Read the input string and an integer, x. The string will be split into x piles.
s=sys.argv[1]
x=int(sys.argv[2])

#init a list to hold lists of tuples, where each list of tuples is a pile of letters, and each tuple is a letter
#with its frequency
freqs=[]
for pile in range(x):
    #init a dict of letters
    d={chr(i+65):0 for i in range(26)}
    for i in range(len(s)):
        if i%x==pile:
            d[s[i]]+=1
    #convert the dict to list of tuples for easy operation later, and sort by non-increasing frequency
    d=sorted(d.items(), key=lambda entry: entry[1], reverse=True)
    freqs.append(d)

#create a tuple to string method for easy printing later
def tupleToString(t):
    return str(t[0]) + ': ' + str(t[1])

print("Frequencies: ")
#print the heading of each pile
for i in range(x):
    print('Pile ' + str(i+1), end='\t')
print()
#print the most frequent letter of each pile in the first row, the second most frequent letter of each pile in the
#second letter, etc.
for i in range(26):
    a=[freqs[j][i] for j in range(x)]
    a=[tupleToString(entry) for entry in a]
    print('\t'.join(a))