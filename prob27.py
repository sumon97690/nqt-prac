# Express given number as Sum of Two Prime Numbers
n = int(input("Enter the number: "))

temp = False
for i in range(2,n):
    if(n%i==0):
        temp = True