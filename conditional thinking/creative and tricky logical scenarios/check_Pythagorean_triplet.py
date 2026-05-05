# Take three numbers and check if they can form a Pythagorean triplet.

a = int(input("\nenter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("this is pythagorean triplet")

else:
    print("not pythagorean triplet")