# Check whether a given integer is single-digit, double-digit, or multi-digit.

num = int(input("\nenter the number: "))

digit = len(str(abs(num)))

if digit == 1:
    print("single digit")

elif digit == 2:
    print("double digit")

else:
    print("multi digit")