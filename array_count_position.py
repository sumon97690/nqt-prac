def replace_elements_with_rank(arr):
    """
    This function replaces the elements in an array with their respective rank.
    """
    # Create a copy of the original array
    sorted_arr = sorted(arr)
    
    # Replace each element in the original array with its rank
    for i in range(len(arr)):
        arr[i] = sorted_arr.index(arr[i]) + 1
    
    return arr

arr = [85,78,45,96,54,52,1,3,4]

sumon = replace_elements_with_rank(arr)
print(sumon)