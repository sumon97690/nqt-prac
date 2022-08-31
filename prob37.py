# to print all the duplicates in the string 
a= input("Enter the string: ")
char_str = {}

for i in a:
    if i in char_str.keys():
        char_str[i] = char_str[i] + 1
    else:
        char_str[i] = 1
    if char_str[i]>=2:
        print(char_str.keys())
