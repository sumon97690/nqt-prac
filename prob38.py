# to print all the duplicates in the string another method
a= input("Enter the string: ")
dupli=[]

for i in a:
    if a.count(i)>1:
        if i not in dupli:
            dupli.append(i)
            
print(dupli)
