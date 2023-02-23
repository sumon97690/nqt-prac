# average of all elements in an array 
arr = [1,2,3,4,5,6,7]

def avgArray(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum = sum + arr[i]
        b = sum/len(arr)
    return b

average = avgArray(arr)
print(average)