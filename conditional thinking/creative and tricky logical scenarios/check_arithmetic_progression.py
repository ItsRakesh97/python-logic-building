# take three numbers and check if they are in arithmetic progression


a = int(input("\nenter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if (b - a) == (c - b):
    print("arithmetic progression")

else:
    print("not an arithmetic progression")