# remove all vowels from the string 

a = input("Enter the string: ")
b = a.lower()
c =  "aeiou"
sum = ""
for i in b:
    if i not in c:
        sum = sum+i

print(sum)