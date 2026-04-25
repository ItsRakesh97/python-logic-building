# Take a 3-digit number and determine if the middle digit is the largest, smallest, or
# neither.

num = int(input("\nenter the 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10 

if b > a and b > c:
    print("middle digit is the largest digit")

elif b < a and b < c:
    print(" middle digit is the smallest digit")

else:
    print("middle digit is neither smallest or largest")