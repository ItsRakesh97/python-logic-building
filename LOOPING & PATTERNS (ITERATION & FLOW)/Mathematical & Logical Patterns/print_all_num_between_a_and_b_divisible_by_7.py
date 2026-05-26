# Print all numbers between a and b divisible by 7

a = int(input('\nenter the first number: '))
b = int(input('enter the ssecond number: '))

for i in range(a , b+1):
    if i % 7 == 0:
        print(i)
