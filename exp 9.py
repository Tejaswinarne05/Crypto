# Double Transposition Cipher

def double_encrypt(text, key1, key2):
    return encrypt(encrypt(text, key1), key2)

def double_decrypt(cipher, key1, key2):
    return decrypt(decrypt(cipher, key2), key1)

text = input("Enter text: ").replace(" ", "").upper()
key1 = input("Enter first key: ").upper()
key2 = input("Enter second key: ").upper()

cipher = double_encrypt(text, key1, key2)
print("Encrypted:", cipher)
print("Decrypted:", double_decrypt(cipher, key1, key2))
