a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))

arr= [a,b,c,d,e]

max = arr[0]

for i in range(0,len(arr)):
    if arr[i] > arr[0]:
        max = arr[i]
        maxi = arr[i+1]
        
print(maxi)