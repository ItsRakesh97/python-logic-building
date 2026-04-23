# Take two numbers and determine whether both are even, both are odd, or one is
# even and one is odd.

n1 = int(input("\nenter the first number: "))
n2 = int(input("enter the second number: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print(f"{n1} and {n2} both are even number")

elif n1 % 2 != 0 and n2 % 2 != 0:
    print(f"{n1} and {n2} both are odd number")

else:
    print("one id odd and one is even number")
