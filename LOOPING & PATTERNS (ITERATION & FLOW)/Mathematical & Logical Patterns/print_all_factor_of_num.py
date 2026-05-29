# Print all factors of a given number

num = int(input('\nenter the number: '))

for i in range(1,num + 1):
    if num % i == 0:
        print(i)