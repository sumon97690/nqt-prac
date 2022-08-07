# greatest of two numbers using functions
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))

def greatest(num1,num2):
    if(num1>num2):
        return num1
    else:
        return num2

great = greatest(a,b)
print("The greatest number is ", great)

