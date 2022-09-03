# print the maximum words in the string 
a= input("enter the string: ")
b =a.split()

max = 0
for i in b:
    if(len(i)>max):
        max = len(i)
        max_word = i
    else:
        pass

print(max_word)

