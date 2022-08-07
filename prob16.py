# factorial of a number using a recursive function 
n= int(input("Enter the number: "))

def recursive_func(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recursive_func(n-1)
    
rec = recursive_func(n)
print(rec)