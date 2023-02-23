array = [1,2,3,4,5]
insertLast = int(input("Enter last no to insert:"))
insertFirst = int(input("Enter first no to insert:"))
array.append(insertLast)
array.append(insertFirst)
print(array)

# now right shift by 1
shift = 1

for i in range(0,shift):
    temp = array[len(array)-1]
    for j in range(len(array)-1,0,-1):
        array[j] = array[j-1]
    array[0] = temp

print(array)
array.insert(4,10)
print(array)