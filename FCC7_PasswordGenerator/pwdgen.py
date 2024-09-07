import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters) # Randomly select a character from all_characters
        
        constraints = [                         # Constraints for the password: r stands for raw string (includes backslashes)
            (nums, r'\d'),                      # At least 1 digit r'\d' is equivalent to r'[0-9]'
            (special_chars, fr'[{symbols}]'),   # At least 1 special character fr'[{symbols}]' is equivalent to fr'[!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]'
            (uppercase, r'[A-Z]'),              # At least 1 uppercase letter
            (lowercase, r'[a-z]')               # At least 1 lowercase letter
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))    # Check if the number of characters in the password meets the constraint
            for constraint, pattern in constraints
        ):
            break
    
    return password
    
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)