# Take three numbers and print the median value (neither maximum nor minimum).

a = int(input("\nenter the first number: "))
b = int(input("enter the second number:  "))
c = int(input("enter the third number: "))

if (a > b and a < c) or (a < b and a > c):
    print(f"{a} is the median value")

elif (b > a and b < c) or (b < a and b > c):
    print(f"{b} is the median value")

else:
    print(f"{c} is the median value")