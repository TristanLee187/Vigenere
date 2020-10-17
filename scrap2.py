import sys
# import time
# t1=time.time()


#Read the input string and an integer, x. The string will be split into x piles.
s=sys.argv[1]
x=int(sys.argv[2])

d={}
for i in range(len(s)):
    if i%x==3:
        if s[i] in d:
            d[s[i]]+=1
        else:
            d[s[i]]=1
for i in d:
    print(i+': '+str(d[i]))