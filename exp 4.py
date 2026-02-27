from math import gcd

# modular inverse
def mod_inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None

# Take key matrix
print("Enter 2x2 key matrix values:")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

det = (a*d - b*c) % 26

# Check validity
if gcd(det, 26) != 1:
    print("Invalid Key! Determinant not coprime with 26.")
    exit()

inv_det = mod_inverse(det)

# Inverse matrix
inv = [
    [( d * inv_det) % 26, (-b * inv_det) % 26],
    [(-c * inv_det) % 26, ( a * inv_det) % 26]
]

text = input("Enter Plaintext: ").upper().replace(" ", "")

# Make even length
if len(text) % 2 != 0:
    text += 'X'

# Encryption
cipher = ""
for i in range(0, len(text), 2):
    x = ord(text[i]) - 65
    y = ord(text[i+1]) - 65
    c1 = (a*x + b*y) % 26
    c2 = (c*x + d*y) % 26
    cipher += chr(c1 + 65) + chr(c2 + 65)

print("Encrypted:", cipher)

# Decryption
plain = ""
for i in range(0, len(cipher), 2):
    x = ord(cipher[i]) - 65
    y = ord(cipher[i+1]) - 65
    p1 = (inv[0][0]*x + inv[0][1]*y) % 26
    p2 = (inv[1][0]*x + inv[1][1]*y) % 26
    plain += chr(p1 + 65) + chr(p2 + 65)

print("Decrypted:", plain)
