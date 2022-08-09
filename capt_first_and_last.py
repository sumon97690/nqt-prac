a = input("Enter the string: ")
a = a.title()
a = a.split()

string = ""
for i in a:
    string = string + i[:-1]+i[-1].upper()+" "

print(string)