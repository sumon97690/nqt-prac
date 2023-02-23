# find all non repeating array 

array = [1,2,4,5,8,8,2,1,6,7,9]
arr = []
for i in array:
    if i not in arr:
        if array.count(i)<2:
            arr.append(i)
            
print(arr)