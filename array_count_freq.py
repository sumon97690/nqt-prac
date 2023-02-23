arr = [10,20,50,10,50,20,8,5,4]

count_dict = {}

for i in arr:
    if i in count_dict.keys():
        count_dict[i] = count_dict[i] + 1
    else:
        count_dict[i] = 1
        
print(f"the frequency are {count_dict.keys()}: {count_dict.values()}")
print(f"The frequency are {count_dict}")
