# Take a single digit (0–9) and print its word form (“Zero” to “Nine”)

digit = int(input("\n select the number from 0 to 9: "))
words = ["zero" , "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

if digit >= 0 and digit <= 9:
    print(words[digit])

else:
    print("invalid digit")