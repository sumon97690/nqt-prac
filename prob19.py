# to check if the number is strong number or not
# eg 145 = 1! +4! +5! = 145

n = int(input("Enter a number: "))
temp = n
sum = 0
while(n>0):
    strong = n%10
    
    product = 1
    for i in range(1,strong+1):
        product = product*i
    
    sum= sum+product
    if(temp==sum):
        print(sum)
    n = n//10
    
    
        