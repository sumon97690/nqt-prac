# Remove All Duplicates from a String
a= input("Enter the string: ")
str = ""
for i in a:
    if i not in str:
        str = str+i
        

print(str)