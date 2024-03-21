def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength = 0
    feedback = []

    if length >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if has_upper and has_lower:
        strength += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if has_digit:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if has_special:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

def main():
    while True:
        password = input("Enter your password: ")
        if not password:
            break

        strength, feedback = check_password_strength(password)

        if strength == 4:
            print("Password is strong.")
        else:
            print("Password is weak.")
            print("Feedback:")
            for message in feedback:
                print("-", message)

if __name__ == "__main__":
    main()
