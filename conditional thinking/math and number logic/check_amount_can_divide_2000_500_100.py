# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes

amount = int(input("\nenter the amount: "))

if amount % 100 != 0:
    print("not possible")

else:
    print("possible")