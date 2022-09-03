# count no of words in the given string 
a= input("Enter the string: ")

spaces= 0
for i in a:
    if(i==" "):
        spaces = spaces + 1

print("the no of words in the string is ", + spaces+1)
