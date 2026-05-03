# take income and age, and check if eligible for tax (age > 18 and income > 5 L).

age = int(input("\nenter the age : "))
income = float(input("enter the income: "))

if age > 18 and income > 500000:
    print("eligible for tax")

else:
    print("not eligible for tax")