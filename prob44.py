# change case of each character in the string 
a = input("Enter the string: ")
chara = " "
for i in a:
    ascii = ord(i)
    if ascii>=65 and ascii<=90:
        chara = chara  + chr(ascii+32)
    elif ascii>=97 and ascii<=132:
        chara = chara + chr(ascii-32)
    elif i == " ":
        chara = chara+" "
    else:
        pass

print(chara)