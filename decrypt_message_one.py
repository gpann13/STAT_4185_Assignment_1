cipher = {
    'a': 'v',
    'b': 'h',
    'c': 'r',
    'd': 'j',
    'e': 't',
    'f': 'x',
    'g': 's',
    'h': 'a',
    'i': 'e',
    'j': 'f',
    'k': 'b',
    'l': 'n',
    'm': 'o',
    'n': 'i',
    'o': 'g',
    'p': 'l',
    'q': 'm',
    'r': 'z',
    's': 'q',
    't': 'u',
    'u': 'c',
    'v': 'k',
    'w': 'd',
    'x': 'p',
    'y': 'y',
    'z': 'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ': ': '-',
    ')': '*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

## Flips cipher dict keys and values
def flip_cipher(cipher):
    flipped_cipher = {}
    for key in cipher:
        flipped_cipher[cipher[key]] = key
    return flipped_cipher

## Decodes encrypted message using the flipped cipher
## Pullls each character from the encrypted message and checks if it is in the flipped cipher
def decode(code):
    decrypted_message = ""
    for char in encrypted_message:
    decrypted_message += flip_cipher(cipher).get(char, char)
    print(decrypted_message)

decode(encrypted_message)


