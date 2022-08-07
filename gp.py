# sum of gp series with the help of the formula
a= int(input("Enter the value of a: "))
r= int(input("Enter the value of r: "))
n= int(input("Enter the value of n2: "))

s1 = a
s2 = ((r**n)-1)/(r-1)

s= s1*s2
print(s)