# Keyed Columnar Transposition

import math

def get_order(key):
    return sorted(range(len(key)), key=lambda k: key[k])

def encrypt(text, key):
    cols = len(key)
    rows = math.ceil(len(text) / cols)
    text += 'X' * (rows * cols - len(text))
    matrix = [text[i:i+cols] for i in range(0, len(text), cols)]
    order = get_order(key)
    cipher = ''
    for col in order:
        for row in matrix:
            cipher += row[col]
    return cipher

def decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols
    order = get_order(key)
    matrix = ['' for _ in range(rows)]
    index = 0
    for col in order:
        for row in range(rows):
            matrix[row] += cipher[index]
            index += 1
    return ''.join(matrix).rstrip('X')

text = input("Enter text: ").replace(" ", "").upper()
key = input("Enter keyword: ").upper()
cipher = encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, key))
