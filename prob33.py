# to find the anagram 
a= input("Enter the string: ")
b= input("Enter the string: ")
c = sorted(a)
d= sorted(b)

if(c==d):
    print("anagram")
else:
    print("Not a anagram")