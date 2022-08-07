import math

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

D = (b*b) - (4*a*c) 
E = math.sqrt(b*b - 4*a*c)
F = -b/2*a

if(D>0):
    root1 = (-b + E) / 2*a
    root2 = (-b - E) / 2*a
    print(f"The value of root1 is {root1} and root2 is {root2}")
elif(D<0):
    print(f"the root1 is {F+(-E)/2*a}i")
    print(f"the root2 is {F-(-E)/2*a}i")
else:
    print(f"The root1 = root2 is {F}")