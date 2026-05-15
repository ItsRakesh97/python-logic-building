# Count the number of digits in a given number

n = int(input("\nenter the number: "))

count = 0
while n > 0:
    digit = n % 10
    count += 1
    n = n // 10

print(count)
