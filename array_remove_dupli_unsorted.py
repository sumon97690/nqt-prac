arr = [2,5,4,8,7,5,2,4]

array = []

for i in arr:
    if i not in array:
        if arr.count(i)>=1:
            ans = array.append(i)
            
print(array)