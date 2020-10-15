def encodeLetter(plain,key):
    num=ord(plain)+ord(key)-130
    return chr(num%26+65)

a,b=input().upper().split()
print(encodeLetter(a,b))