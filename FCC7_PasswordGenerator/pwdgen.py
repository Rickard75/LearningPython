"""Regular expression is a powerful tool for matching patterns in text."""

# Le regex (o espressioni regolari) sono un modo potente per cercare, confrontare e manipolare stringhe di testo in base a schemi specifici.
# Sono particolarmente utili quando vuoi trovare modelli specifici come numeri, lettere, parole, o formati di testo (es. email, numeri di telefono, ecc.).

# Cosa fanno le regex?
# Immagina di voler cercare delle cose specifiche in una stringa:

# Tutte le cifre in un testo.
# Parole che iniziano con una lettera maiuscola.
# Un indirizzo email in un documento.
# Le regex ti permettono di creare uno "schema" che rappresenta ciò che stai cercando e poi di usarlo per trovare corrispondenze.

# Alcune regex comuni:
# \d: Trova un numero.
# \w: Trova una lettera.
# \s: Trova uno spazio bianco.
# . : Trova qualsiasi carattere.
# ^ : Trova qualcosa all'inizio della stringa.
# $ : Trova qualcosa alla fine della stringa.
# [a-z]: Trova qualsiasi lettera minuscola.
# [A-Z]: Trova qualsiasi lettera maiuscola.
# [0-9]: Trova qualsiasi numero.
# [^a]: Trova qualsiasi carattere che non sia 'a'.
# (a|b): Trova 'a' o 'b'.
# \b: Trova un bordo di parola.
# \d{3}: Trova esattamente 3 cifre.
# \d{3,7}: Trova da 3 a 7 cifre.
# \d{3,}: Trova 3 o più cifre.
# \d{,7}: Trova fino a 7 cifre.



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