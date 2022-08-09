# to count the number of vowels, consonants and spaces

a = input("Enter the string : ")
b = a.lower()
c = "aeiou"
vowel = 0
cons= 0

for i in b:
    if i in c:
        vowel = vowel+ 1
    else:
        cons= cons+1

print("The count of the vowel are ", vowel)
print("The count of the consonants are",cons)
d = b.count(" ")
print("The spaces are ", d)