'''Encrpit text using Caesar Cipher'''

text = 'Hello Zaira'
shift = 3
version = 0

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    global version
    version += 1

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('Cryptography call number:', version)
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

#caesar(text,shift)
#caesar(text,13)
#caesar(text,1111)
caesar('Viva la pizza', 1)
caesar('gw150914',1)