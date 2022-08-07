# Reverse a number 

n= int(input("Enter the number:"))
temp = n
a = 0
while(n>0):

    a= a*10 + n%10
    n = n//10

print(a)