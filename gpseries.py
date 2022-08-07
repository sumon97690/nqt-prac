# sum of GP series

a= int(input("Enter the value of a: "))
r= int(input("Enter the value of r: "))
n= int(input("Enter the value of n2: "))
sum=0
i=1
while(i<=n):
    sum= sum+a
    a=a*r
    i = i+1
print(sum)