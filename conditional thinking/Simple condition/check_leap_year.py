year = int(input("enter the year you want to check: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("the year is a leap year")

else:
    print("not a leap year")
    