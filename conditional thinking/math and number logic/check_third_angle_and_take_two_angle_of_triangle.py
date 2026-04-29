# Take two angles of a triangle and compute the third angle.

a = float(input("\nenter the first angle of triangle: "))
b = float(input("enter the second angle of a triangle: "))

c = 180 - (a + b)

print("the third angle is: " , c)