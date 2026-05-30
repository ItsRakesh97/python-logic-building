# Find the sum of all factors of a number

num = int(input("\nenter the number: "))

sum = 0
for i in range(1,num+1):
    if num % i == 0:
        sum += i

print(sum)