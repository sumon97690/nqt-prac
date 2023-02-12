a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))

arr= [a,b,c,d,e]

min = arr[0]

for i in range(0,len(arr)):
    if arr[i] < arr[0]:
        min = arr[i]
        
print(min)