# Print first n terms of a geometric progression (a, r).

a = int(input("\nenter first term: "))
r = int(input("enter common ratio: "))
n = int(input("enter number of terms: "))

for i in range(n):
    print(a * (r ** i), end=" ")