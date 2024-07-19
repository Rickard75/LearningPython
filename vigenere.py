'''Encryption and decryption using the Vigenere cipher'''

text = 'Hello Zaira!'
custom_key = 'python'

def vigenere(message, key, direction=1): # default direction is straight(=encryption)
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
    
        # Append any non-letter character to the message
        if char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
    
encryption = vigenere(text, custom_key) # default direction=1: encryption
print('Plain text:      ', text)
print('Encrytpted text: ', encryption)
decryption = vigenere(encryption, custom_key, -1) # decryption
print('Decrypted text:  ', decryption)