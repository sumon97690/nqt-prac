# lcm of two nos
n1 = int(input("Enter a first number: "))
n2 = int(input("Enter a second number: "))

for i in range(1, min(n1, n2)+1):
    if(n1%i==0) and (n2%i==0):
        gcd=i

lcm1 =(n1*n2)
lcm2 = gcd
lcm=lcm1/lcm2
print(lcm)
      
        