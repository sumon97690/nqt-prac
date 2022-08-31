# another method to count frequency

a= input("Enter the string: ")
char_dict = {}
for i in a:
    if i in char_dict.keys():
        char_dict[i]=char_dict[i]+1
    else:
        char_dict[i] = 1
        
print(char_dict)
print(max(char_dict,key=char_dict.get))
