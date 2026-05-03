# Take a weekday number (1–7) and determine if it is a weekday or weekend.

day = int(input("\n enter the day number(0-7): "))

if day > 0 and day <= 5:
    print("weekday")

elif day == 6 or day == 7:
    print("weekend")

else:
    print("invalid day number")