def sort_by_frequency(arr):
    # Create a dictionary to store the frequency of each element
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    # Sort the array by frequency and then by value
    sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
    
    return sorted_arr

arr = [4, 4, 2, 2, 8, 8, 8, 6, 6, 1]
sorted_arr = sort_by_frequency(arr)
print(sorted_arr)  # Output: [8, 8, 8, 4, 4, 6, 6, 2, 2, 1]