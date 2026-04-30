# Take a character and check if it is a letter, a digit, or neither

ch = input("\nenter the character")

if ch.isdigit():
    print("character is digit")

elif ch.isalpha():
    print("character is letter or alphabet")

else:
    print("neither")