# Change every letter with next lexicographic alphabet
a= input("Enter the string: ")
newword = ""

for i in a:
    ascii = ord(i)
    if ascii==ord('z'):
        newword = newword+'a'
    else:
        newword = newword + chr(ascii+1)       
print(newword)