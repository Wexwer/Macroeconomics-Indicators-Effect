def characters_long(password: str) -> bool:
    return 6 <= len(password) <= 10

def has_only_letters_and_digits(password: str) -> bool:
    return password.isalnum()

def has_minimum_number(password: str, minimum: int = 2) -> bool:
    return sum(1 for ch in password if ch.isdigit()) >= minimum

def password_validator(password: str) -> None:
    errors = []

    if not characters_long(password):
        errors.append("Password must be between 6 and 10 characters")

    if not has_only_letters_and_digits(password):
        errors.append("Password must consist only of letters and digits")

    if not has_minimum_number(password):
        errors.append("Password must have at least 2 digits")

    if errors:
        print("\n".join(errors))
    else:
        print("Password is valid")

password = input()
password_validator(password)