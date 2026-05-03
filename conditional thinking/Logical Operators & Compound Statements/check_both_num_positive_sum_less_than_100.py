# take two numbers and check if both are positive and their sum is less than 100

num1 = int(input("\nenter the first number: "))
num2 = int(input("enter the second number: "))

if num1 > 0 and num2 > 0 and (num1 + num2) < 100:
    print("condition satisfied")

else:
    print("condition not satisfied")