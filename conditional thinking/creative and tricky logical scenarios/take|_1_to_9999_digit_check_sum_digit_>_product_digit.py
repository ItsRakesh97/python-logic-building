# take an integer (1–9999) and check if the sum of its digits is greater than the productof its digits.

num = int(input("\nenter the number (1 to 9999): "))

temp = num
sum_digit = 0
product_digit = 1

while temp > 0:
    digit = temp % 10
    sum_digit += digit
    product_digit *= digit
    temp = temp // 10

print(sum_digit)
print(product_digit)

if sum_digit > product_digit:
    print("sum_digit is bigger than product_digit")

else:
    print("no the sum digit is not greater than the prodect digit")