n = 10
for i in range(1,n+1):
    for j in range(n - i):      #for space in the pyramid so every time n - iteration will be the space
        print(" ",end="")           
    for k in range(2 * i -1):
        print("*",end="")
    print()