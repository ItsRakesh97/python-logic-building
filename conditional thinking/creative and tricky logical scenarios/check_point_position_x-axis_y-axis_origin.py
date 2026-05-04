# Take coordinates (x, y) and check if the point lies on the X-axis, Y-axis, or at the origin.

x = int(input("\nenter x coordinates: "))
y = int(input("enter y coordinates: "))

if x == 0 and y == 0:
    print("point is at origin")

elif x == 0:
    print("point lies at y axis")

elif y == 0:
    print("point lies at x axis")

else:
    print("point does not lies on any axis")