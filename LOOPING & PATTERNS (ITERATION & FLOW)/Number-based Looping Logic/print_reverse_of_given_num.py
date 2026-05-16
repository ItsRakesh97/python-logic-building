# Print the reverse of a given number.

n = int(input("\nenter the number: "))

reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(reverse)