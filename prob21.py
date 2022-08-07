# gcd
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))

for i in range(1, min(n1, n2)+1):
    if(n1%i==0) and (n2%i==0):
        a=i
print(a)
      
        