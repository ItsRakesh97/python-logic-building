# Take electricity units consumed and calculate the bill as per slabs (using if-else)

unit = int(input("\n enter the unit: "))
bill = 0

if unit <= 100:
    bill = unit * 5

elif unit <= 200:
    bill = (100 * 5) + ((unit - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((unit - 200) * 10)

print("electricity bill", bill)