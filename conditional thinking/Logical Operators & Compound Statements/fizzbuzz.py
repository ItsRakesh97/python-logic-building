# Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and
# “FizzBuzz” if divisible by both


num = int(input("\nenter the number: "))

if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")

elif num % 3 == 0:
    print("fizz")

elif num % 5 == 0:
    print("buzz")

else:
    print("not divisible by both 3 and 5")