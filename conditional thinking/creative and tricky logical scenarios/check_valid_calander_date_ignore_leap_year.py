# Take day and month and check if it forms a valid calendar date (ignoring leap years)

days = int(input("\nenter the day: "))
months = int(input("enter the month: "))

valid = False

if months >= 1 and months <=12:

    if months == 2:
        if days >= 1 and days <= 28:
            valid = True

    elif months in [4,6,9,11]:
        if days >= 1 and days <= 30:
            valid = True

    else:
        if days >= 1 and days <= 31:
            valid = True

if valid:
    print("valid date")

else:
    print("invalid date")