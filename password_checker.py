import string

def check_password_strength(password):
    length = len(password) >= 8
    has_punctuation = any(char in string.punctuation for char in password)
    has_digit = any(char in string.digits for char in password)
    has_lowercase = any(char in string.ascii_lowercase for char in password)
    has_uppercase = any(char in string.ascii_uppercase for char in password)

    score = sum([length, has_punctuation, has_digit, has_lowercase, has_uppercase])

    if score == 5:
        strength = "Very strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Good"
    elif score == 2:
        strength = "Medium"
    elif score == 1:
        strength = "weak"
    else:
        strength = "Very weak"
    print("\nPassword Strength:", strength)
    print("Details:")
    print(f"- Minimum 8 characters: {'✅' if length else '❌'}")
    print(f"- Uppercase letter: {'✅' if has_uppercase else '❌'}")
    print(f"- Lowercase letter: {'✅' if has_lowercase else '❌'}")
    print(f"- Number: {'✅' if has_digit else '❌'}")
    print(f"- Special character: {'✅' if has_punctuation else '❌'}")
    print(score)

password = input("Enter your password: ")
check_password_strength(password)