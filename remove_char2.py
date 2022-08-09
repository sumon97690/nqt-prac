a = input("Enter the string: ")
sum = ""
for i in range(0,len(a)):
    if a[i]>="a" and a[i]<="z":
        sum = sum + a[i]

print(sum)