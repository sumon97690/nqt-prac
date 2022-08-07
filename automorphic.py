n = int(input("Enter a number: "))
temp=n
a = n*n
b= a%100
if(b==temp):
    print("it is an automorphic") 
else:
    print("it is not an automorphic")