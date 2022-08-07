# greatest of three numbers using functions
a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
c= int(input("Enter a number: "))
def greatest(num1,num2,num3):
    if(num1>num2) and (num1>num3):
        return num1
    elif(num2>num1) and (num2>num3):
        return num2
    else:
        return num3

great = greatest(a,b,c)
print("The greatest number is ", great)