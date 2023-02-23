# def find_symmetric_pairs(arr):
#     symmetric_pairs = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]:
#                 symmetric_pairs.append(arr[i])
#                 symmetric_pairs.append(arr[j])
#                 break
#     return symmetric_pairs

# arr = [(1, 2), (3, 4), (2, 1), (5, 6), (7, 8), (8, 7)]
# symmetric_pairs = find_symmetric_pairs(arr)
# print(symmetric_pairs)

nums = [(1, 2), (3, 4), (2, 1), (5, 6), (7, 8), (8, 7)]
