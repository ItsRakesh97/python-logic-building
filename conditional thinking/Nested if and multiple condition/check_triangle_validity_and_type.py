# Take three sides and check if they form a valid triangle.
# If the sides form a valid triangle, determine whether it is equilateral, isosceles, or
# scalene.



a = int(input("\nenter the first side of a triangle: "))
b = int(input("enter the second side of a triangle: "))
c = int(input("enter the third side of a triangle: "))

if a <= 0 or b <= 0 or c <= 0:
    print("side must be positive")

elif a + b > c and a + c > b or b + c > a:
    print("yes it is a valid triangle")

    if a == b and b == c:
        print("this is a equilateral triangle ")

    elif a == b or b == c or c == a:
        print("this is an isosceles triangle")

    else:
        print("this is an scalene triangle ")

else:
    ("not a triangle")