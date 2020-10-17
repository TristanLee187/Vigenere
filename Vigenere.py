#read the plain or cipher text and the key (converting to uppercase)
import sys
mode=sys.argv[1]
string=sys.argv[2].upper()
key=sys.argv[3].upper()

#encode one letter with one key character by adding their character-to-number values, and modding by 26.
#involves adding and subtracting 65 because ord('A') is 65.
def encodeLetter(plain,key):
    num=ord(plain)+ord(key)-130
    return chr(num%26+65)

#decode one letter with the same process as encodeLetter, but using subtraction instead of addition
def decodeLetter(cipher,key):
    num = ord(cipher) - ord(key)
    return chr(num % 26 + 65)

#encode the while text
def encodeFull():
    ans = ''
    for i in range(len(string)):
        ans += encodeLetter(string[i], key[i % len(key)])
    return ans

#decode the whole text
def decodeFull():
    ans=''
    for i in range(len(string)):
        ans+=decodeLetter(string[i],key[i%len(key)])
    return ans

print('Answer: ')
if mode=='encode':
    print(encodeFull())
else:
    print(decodeFull())