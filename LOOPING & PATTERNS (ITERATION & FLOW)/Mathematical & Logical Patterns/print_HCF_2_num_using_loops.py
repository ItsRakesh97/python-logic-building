# Find HCF (GCD) of two numbers using loops

num1 = int(input("\nenter the first number: "))
num2 = int(input("enter the second number: "))

small_num = min(num1,num2)
HCF = 1

for i in range(1,small_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        HCF = i

print("HCF is", HCF)