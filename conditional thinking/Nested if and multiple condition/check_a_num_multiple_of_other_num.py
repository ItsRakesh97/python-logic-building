# Check if one of two given numbers is a multiple of the other.

a = int(input("\nenter the first number: "))
b = int(input("enter the second number: "))

if a % b == 0:
    print(f"{a} is multiple of {b}")

elif b % a == 0:
    print(f"{b} is the multiple of {a}")

else:
    print(f"both {a} and {b} and not multiple of each other")