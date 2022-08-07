# perfect number
# 6 is a perfect no bcoz 2,3,1 is divisible by 6 and if we add 2+3+1=6 therefore it is a perfect no
# armstrong number
a = int(input("Enter the number: "))
temp = a
sum=0
for i in range(1,a):
    if(a%i==0):
        sum = sum +i
if(temp==sum):
    print("it is a perfect no")
else:
    print("It is not a perfect no")
        
