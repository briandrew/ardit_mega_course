

def password_validation(password):
    length, caps, digits = False, False, False

    if len(password) >= 8:
        length = True
    for char in password:
        if char.isupper():
            caps = True
        if char.isdigit():
            digits = True
    if length and caps and digits:
        return "strong password"
    else:
        return "weak password"


user_password = input("Enter your password for validation: ")

result = password_validation(user_password)
print(result)
