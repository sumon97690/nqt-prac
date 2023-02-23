# remove duplicates from array 
arr = [1,1,2,2,3,3,4,5]

array = []

for i in arr:
    if arr.count(i)>=1:
        if i not in array:
            array.append(i)
print(array)
        
        
        