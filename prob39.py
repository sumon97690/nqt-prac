# Remove Characters from first String present in the Second String
a= input("Enter the string: ")
b= input("Enter the second string: ")
str = ""
for i in a:
    if i not in b:
        str = str+i
        
print(str)
