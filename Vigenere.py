def encodeLetter(plain,key):
    num=ord(plain)+ord(key)-130
    return chr(num%26+65)
print(encodeLetter('B','C'))