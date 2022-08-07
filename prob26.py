# replace 0's with 1's in the given no 

n = int(input("Enter the number: "))
ans = 0
while(n>0):
    
    digit = n%10
    if(digit==0):
        digit = 1
    ans = ans*10+ digit
    n = n//10
   
ans1 = 0 
while(ans>0):
    
    digit1 = ans%10
    ans1 = ans1*10+digit1
    ans = ans//10

print(ans1)