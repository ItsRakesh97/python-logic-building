# Print the sum of first n natural numbers


n = int(input("\n enter the number: "))
total = 0

for i in range(1,n+1):
    total += i

print(total)