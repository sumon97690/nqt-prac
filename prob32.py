# find the non repeating characters 
a= input("Enter the string: ")

for i in a:
    if a.count(i)<2:
        print(i, end=" ")