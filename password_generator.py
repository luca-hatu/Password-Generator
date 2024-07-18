import random
import string

def get_user_preferences():
    while True:
        try:
            length = int(input("Length ?: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    return length, include_uppercase, include_lowercase, include_digits, include_special

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    character_pool = ''
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("No character types selected for password generation.")

    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    length, include_uppercase, include_lowercase, include_digits, include_special = get_user_preferences()
    try:
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)
