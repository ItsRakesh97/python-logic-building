# Check if a number is an Armstrong number
# armstrong number = sum of all digit raised to the power of total number of digit = original numeber

n = int(input("\nenter the number: "))

original = n
digits = len(str(n))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10

if sum == original:
    print("armstrong number")

else:
    print("not armstrong number")

