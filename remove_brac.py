# remove bracket from the string 
a = input("Enter the string: ")
b=  "()"
sum = ""
for i in a:
    if i not in b:
        sum =  sum+i

print(sum)