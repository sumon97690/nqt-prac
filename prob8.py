# sum of AP series

a=int(input("Enter the value of a: "))
n=int(input("Enter the value of n: "))
d=int(input("Enter the value of d: "))
sum= 0
i = 1
while(i<=n):
    sum = sum+a
    a=a+d
    i= i+1
    
print(sum)
