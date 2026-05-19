# take a3-digit number and check if the sum of the first and last digit equals the middle digit

num = int(input("\nenter the 3 digit number:  "))

a = num // 100
b = (num // 10) % 10
c = num % 10

if a + c == b:
    print("yes sum of  first and last digit number is equal to middle digit ")

else:
    print("not sum is not equal to middle digit")