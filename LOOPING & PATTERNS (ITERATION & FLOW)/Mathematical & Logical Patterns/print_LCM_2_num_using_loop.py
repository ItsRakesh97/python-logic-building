# Find LCM of two numbers using loops.

num1 = int(input("\nenter the first num: "))
num2 = int(input("enter the second num: "))

greater = max(num1,num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        LCM = greater
        break
    greater += 1

print(LCM)
