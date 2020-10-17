import sys
s=sys.argv
string=s[1]
key=s[2]

def encodeLetter(plain,key):
    num=ord(plain)+ord(key)-130
    return chr(num%26+65)

def decodeLetter(cipher,key):
    num = ord(cipher) - ord(key)
    return chr(num % 26 + 65)

def decodeFull():
    ans=''
    for i in range(len(string)):
        ans+=decodeLetter(string[i],key[i%len(key)])
    return ans

print('Answer: ')
print(decodeFull())