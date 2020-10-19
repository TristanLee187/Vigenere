# Program to generate possible lengths by considering factors of the differences of indeces of repeated words.
# The factors are checked using a sieve of eratonsthenes style algorithm.
#
# To run:
# $python3 findLenKey.py text x
# where text is the plaintext or ciphertext, and x is the length of repeated words to be considered
#
# Output:
# $Try more common factors as key lengths
# $The frequencies of each possible factor:
# $n1's frequency: f1
# $n2's frequency: f2
# .
# .
# .
# where n is the factor and f1 is its frequency, or the number of differences that have n as a factor.
# The values of n are sorted by non-increasing frequency


import sys
# import time
# t1=time.time()


#Read the input string and an integer, x. Repititions of words of length x will be looked for.
s=sys.argv[1]
x=int(sys.argv[2])

#init a dicitonary of words; they will store the indices of the word
words={}

for i in range(len(s)-x):
    #get the word of length x
    word=s[i:i+x]
    if word in words:
        #record the next index of the word
        words[word].append(i)
    else:
        #or init a new list with the first index of the word
        words[word]=[i]

#create list to store every difference between repeated words
spaces=[]

for word in words:
    #get the indices of every word
    l=words[word]
    #create a difference array to store the differences in the indices
    diff=[]
    for i in range(1,len(l)):
        diff.append(l[i]-l[i-1])
    spaces+=diff



# find the frequencies of all the possible factors of the differences; find the value n for every possible factor m,
# where n is the number of differences that have m as a factor. Does this with the style of the sieve of eratosthenes

#init the sieve array, where sieve[i] counts the frequency of the difference i
sieve=[]
for diff in spaces:
    #extend the length of the sieve if too small; extending by a negative number does nothing; add 1 to take care of
    #0 indexing (sieve[diff] will correspond to diff rather than diff+1]
    sieve.extend((diff-len(sieve)+1)*[0])
    sieve[diff]+=1

#record the frequencies of each factor in a 2-D array
freqs=[]
#start counting factors with 2, end with the square root of the length of the sieve array (so not every possible factor
#is checked, but this is a reasonable cutoff)
for i in range(2,int(len(sieve)**0.5)):
    #the factor i gets a value equal to the sum of the elements of sieve where its index as a multiple of i.
    #append [i,sum] to the freqs array
    freqs.append([i,sum([sieve[j] for j in range(0,len(sieve),i)])])

#Runtime: O(log(n)); each factor contributes 1/x to the runtime. So the total runtime is close to the harmonic series,
#which is close to log(n).

#sort the freqs array by non-increasing frequency (which is the second element of each row in the list)
freqs.sort(key=lambda entry: entry[1], reverse=True)

#The result is an array of arrays of the form [factors, frequency] sorted by frequency in non-increasing order.
#Therefore, the most common factors of differences in indeces of repeated letters appears earlier in the list.

#print the array in human readable format
print('Try more common factors as key lengths')
print('The frequencies of each possible factor: ')
for entry in freqs:
    print(str(entry[0])+'\'s frequency: ' + str(entry[1]))


# t2=time.time()
# print('Time: ' + str(t2-t1))
# should be O(n) time, where n is the length of s