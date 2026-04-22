#Take a character and check whether it’s uppercase, lowercase, a digit, or a special
#character.

ch = input("enter the character: ")

if ch.isupper():
    print("the character is upprcase")

elif ch.islower():
    print("the character is lowercase")

elif ch.isdigit():
    print("the character is digit")

else:
    print("the character is special")
