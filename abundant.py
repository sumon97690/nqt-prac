num = int(input("Enter a number: "))
temp = num
sum= 0
for i in range(1,num):
    if(num%i==0):
        sum = sum + i
print(sum)

if(sum>temp):
    print("It is an abundant number")
else:
    print("it is not an abundant number")