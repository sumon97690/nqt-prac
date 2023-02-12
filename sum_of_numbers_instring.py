# sum of a numbers in a string 

a= input("Enter a string : ")


def sum_of_no(a):
    sum = 0
    num = 0
    for i in a:
        if i.isdigit():
            num =num*10 + int(i)
        else:
            sum = sum +num
            num = 0
    return sum + num

print(sum_of_no(a))

