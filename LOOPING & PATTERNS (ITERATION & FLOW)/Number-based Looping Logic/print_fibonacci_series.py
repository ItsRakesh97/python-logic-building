#print_fibonacci series upto n terms

n = int(input("\nenter the number of term: "))

a = 0
b = 1 
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c