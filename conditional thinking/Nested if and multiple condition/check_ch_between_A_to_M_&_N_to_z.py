# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

ch = input("\nenter the character you want to check: ").lower()

if ch.isalpha():
    if ch >= "a" and ch <= "m":
        print(f" character {ch} is lies between a to m ")

    else:
        print(f"character {ch} is lies between n to z")

else:
    print("invalid character")

