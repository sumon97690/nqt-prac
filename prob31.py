# to count the frequency
a= input("Enter the string: ")
for i in a:
    if (i>= "a" and i<="z" or i>="A"or i<="Z"):
        b=a.count(i)
    print(f"{i} is {b}")
