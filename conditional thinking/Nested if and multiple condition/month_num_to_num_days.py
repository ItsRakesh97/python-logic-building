# Take a month number (1–12) and print the number of days in that month (ignore leap
# years).

months = int(input("\nenter the number of month (1 to 12): "))

if months in [1, 3, 5, 7, 8, 10, 12 ]:
    print("31 days")

elif months in [2, 4, 6, 9, 11]:
    print("30 days")

elif months == 2:
    print("28 days")

else:
    print("invalid days")