a = input("Enter the string: ")
sum = ""
c="abcdefghijklmnopqrstuvwxyz"
d = c.lower()
for i  in a:
    if i in d:
        sum = sum+i

print(sum)