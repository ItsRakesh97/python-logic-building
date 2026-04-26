# Check if a number is a multiple of 7 or ends with 7.

num = int(input("\nenter the number: "))

if num % 7 == 0 or num % 10 == 7:
    print("the number is multiple of 7 or ends with 7")

else:
    print(" the number is not multiple of 7 and does not ends with 7")
