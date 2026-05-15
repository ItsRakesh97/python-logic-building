# Print the product of digits of a given number

n = int(input("\nenter the number: "))

product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n = n // 10

print(product)

