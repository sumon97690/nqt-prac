# leap year or not


year = int(input("Enter the year: "))

if (year%4==0) or (year%400==0) and (year%100!=0) :
    print("This year is a leap year")
else:
    print("This year is not a leap year")