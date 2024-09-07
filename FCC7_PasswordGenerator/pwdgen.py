import secrets # Secure random number generator (more powerful than random)
import string  # String constants


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols
print(all_characters)
print(secrets.choice(all_characters))