# check if a no is prime no or not

a= int(input("Enter a number: "))
temp = False
for i in range(2,a):
    if(a%i==0):
        temp = True
        
    break

if temp:
    print("not prime")
else:
    print("prime")
