import sys
# import time
# t1=time.time()


#Read the input string and an integer, x. The string will be split into x piles.
s=sys.argv[1]
x=int(sys.argv[2])

freqs=[]
for pile in range(x):
    d={chr(i+65):0 for i in range(26)}
    for i in range(len(s)):
        if i%x==pile:
            d[s[i]]+=1
    #sort by non-increasing order; convert to list of tuples for easy operation later
    d=sorted(d.items(), key=lambda entry: entry[1], reverse=True)
    freqs.append(d)



def tupleToString(t):
    return str(t[0]) + ': ' + str(t[1])

print("Frequencies: ")
for i in range(x):
    print('Pile ' + str(i+1), end='\t')
print()
for i in range(26):
    a=[freqs[j][i] for j in range(x)]
    a=[tupleToString(entry) for entry in a]
    print('\t'.join(a))