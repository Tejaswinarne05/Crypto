# Simple Columnar Transposition

import math

def encrypt(text, key):
    rows = math.ceil(len(text) / key)
    text += 'X' * (rows * key - len(text))
    matrix = [text[i:i+key] for i in range(0, len(text), key)]
    cipher = ''
    for col in range(key):
        for row in matrix:
            cipher += row[col]
    return cipher


def decrypt(cipher, key):
    rows = len(cipher) // key
    matrix = ['' for _ in range(rows)]
    index = 0
    for col in range(key):
        for row in range(rows):
            matrix[row] += cipher[index]
            index += 1
    return ''.join(matrix).rstrip('X')


text = input("Enter text: ").replace(" ", "").upper()
k = int(input("Enter key length: "))
cipher = encrypt(text, k)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, k))
