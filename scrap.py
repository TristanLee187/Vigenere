import sys
import time
t1=time.time()
#Read the input string and an integer, x. Repititions of words of length x will be looked for.
s=sys.argv[1]
x=int(sys.argv[2])

#imitialize a list of words
words=[]
for i in range(0,len(s)-x):
    word=s[i:i+x]
    a=s.count(word)
    if a>1:
        words.append(word)
#print(words)
spaces=[]
for word in words:
    a=[]
    for i in range(0,len(s)-x):
        if s[i:i+x]==word:
            a.append(i)
    diff=[]
    for i in range(1,len(a)):
        diff.append(a[i]-a[i-1])
    spaces += diff

t2=time.time()
print('Time: ' + str(t2-t1))
print(spaces)
