#sum of a numbers in a given range in the input

n1= int(input("enter no: "))
n2= int(input("enter no: "))

sum=0
for i in range(n1, n2+1):
    sum= sum+i
    
print(f"The sum of the range between {n1} and {n2} is {sum}")