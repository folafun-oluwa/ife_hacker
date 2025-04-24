userInput = input("Enter password: ")
length = len(userInput) >= 8
uppercase = any(char.isupper() for char in userInput)
digit = any(char.isdigit()for char in userInput)
special_characters = any(not char.isalnum() for char in userInput)

if length and uppercase and digit and special_characters:
    print("Password meets all requirements")
else:
    if not length:
        print("Password must contain at least 8 characters")
        if not uppercase:
            print("Password must contain at least one uppercase letter")
            if not digit:
                print("Password must contain at least one digit")
                if not special_characters:
                    print("Password must contain at least one special character")