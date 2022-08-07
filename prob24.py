# Permutations in which N people can occupy R seats in a classroom 

# formula:- n!/(n-r)! 

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
z = n-r

product = 1
for i in range(1,n+1):
    product = product*i
# print(product)

prod = 1
for j in range(1,z+1):
    prod = prod*j
# print(prod)

answer= product/prod
print(answer)
