# check if the given no is harshad no or not
n = int(input("Enter a first number: "))
temp = n
sum = 0
while(n>0):
    
    a= n%10
    sum = sum + a
    n = n//10
    
if(temp%sum==0):
    print("It is an harshad number")
else:
    print("It is not an harshad number")