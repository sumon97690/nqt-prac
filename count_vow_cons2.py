#another method to count 
# to count the number of vowels, consonants and spaces

a = input("Enter the string : ")
b = a.lower()
vowel = 0
cons= 0

for i in range(0,len(b)):
    if b[i]=="a" or b[i]=="e" or b[i]=="i" or b[i]=="o" or b[i]=="u":
        vowel = vowel + 1
    else:
        cons = cons+ 1
print(vowel)
print(cons)
        
    
    