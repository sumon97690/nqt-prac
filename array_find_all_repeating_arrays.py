array = [1,1,2,2,3,4,5,5,7,6]
arr = []
for i in array:
    if i not in arr:
        if array.count(i)>1:
            arr.append(i)
            
print(arr)
