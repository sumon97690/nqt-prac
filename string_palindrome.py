# to check if the given string is palindrome or not 

a= input("Enter the string: ")
b = a[-1::-1]

if(b==a):
    print("It is a palindrome")
else:
    print("It is not a palindrome")