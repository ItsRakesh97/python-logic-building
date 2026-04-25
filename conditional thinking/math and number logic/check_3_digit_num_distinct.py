# Take a 3-digit number and check if all digits are distinct

num = int(input("\nenter the 3 digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a != b and a != c and b != a:
    print("the number are distinct")

else:
    print("number are not distinct")