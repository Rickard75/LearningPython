'''Encrpit text using Caesar Cipher'''

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower(): # convert text to lowercase
    if char == ' ':
        print('space!')
    index = alphabet.find(char) # find the index of the character in the alphabet
    new_index = index + shift # shift the index by the shift value
    encrypted_text += alphabet[new_index] # add the new character to the encrypted text
    print('char:', char, 'encrypted text:', encrypted_text) # print the character and the encrypted text
