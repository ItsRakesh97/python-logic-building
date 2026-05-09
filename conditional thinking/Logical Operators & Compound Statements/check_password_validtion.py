# Take a password string and check basic rules (length ≥ 8 and contains at least one
# digit)

password = input("\nenter the password: ")

if len(password) >= 8:
    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if has_digit:
        print("valid password")

    else:
        print("password must contain one digit")

else:
    print("password length nust contain 8 digit")


