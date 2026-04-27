# Take coordinates (x, y) and determine which quadrant the point lies in.

x = int(input("\nenter the number: "))
y = int(input("enter the number: "))

if x > 0 and y > 0:
    print("quadrant 1")

elif x < 0 and y > 0:
    print("quadrant 2")

elif x < 0 and y < 0:
    print("quadrant 3")

elif x > 0 and y < 0:
    print("quadrant 4")

elif x == 0 and y == 0:
    print("origin")

elif x == 0:
    print("y axis")

else:
    print("x axis")