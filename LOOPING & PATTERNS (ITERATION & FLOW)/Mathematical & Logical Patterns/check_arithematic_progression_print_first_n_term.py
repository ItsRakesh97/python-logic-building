# Print first n terms of an arithmetic progression (a, d)

a = int(input("\nenter first term: "))
d = int(input("enter common diffrence number: "))
n = int(input("enter number terms: "))

for i in range(n):
    print(a + i * d)