from math import gcd
from functools import reduce

# Encrypt
def encrypt(p, k):
    p = p.upper()
    k = k.upper()
    c = ""
    for i in range(len(p)):
        if p[i].isalpha():
            c += chr((ord(p[i])-65 + ord(k[i % len(k)])-65) % 26 + 65)
    return c

# Decrypt
def decrypt(c, k):
    p = ""
    for i in range(len(c)):
        p += chr((ord(c[i])-65 - (ord(k[i % len(k)])-65)) % 26 + 65)
    return p

# Find repeated 3-letter sequences
def kasiski(c):
    dist = []
    for i in range(len(c)-3):
        seq = c[i:i+3]
        for j in range(i+3, len(c)-3):
            if c[j:j+3] == seq:
                dist.append(j-i)
    if dist:
        return reduce(gcd, dist)
    return None

# Main
plain = input("Enter Plaintext: ")
key = input("Enter Keyword: ")

cipher = encrypt(plain, key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, key))
print("Estimated Key Length:", kasiski(cipher))
