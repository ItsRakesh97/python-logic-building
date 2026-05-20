# take two dates (day and month) and determine which one comes first in the
# calendar.

day1 = int(input("\nenter the date day: "))
month1 = int(input("enter the date month: "))

day2 = int(input("enter the second date day: "))
month2 = int(input("enter second date month: "))

if month1 < month2:
    print("first date comes first")

elif month1 > month2:
    print("second date comes first")


else:
    if day1 < day2:
        print("first date comes first")

    elif day1 > day2:
        print("second date comes first")

    else:
        print("both dates are same")
        