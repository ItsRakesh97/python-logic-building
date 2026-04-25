# Take a 4-digit number and check if the first and last digits are equal.

num = int(input("\nenter the four digit number: "))

first = num // 1000
last = num % 10

if first == last:
    print("yes first and last digit are same")

else:
    print("no first and last digit are not same")