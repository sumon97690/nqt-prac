# armstrong number
n = int(input("Enter the number: "))
temp = n
digit = 0
while (n>0):
    arm  = n%10
    digit = digit+ arm**3
    n = n//10
    
if(temp==digit):
    print("It is an armstrong no")
else:
    print("It is not an armstrong")
