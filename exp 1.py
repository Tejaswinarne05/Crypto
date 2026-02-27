# Function to encrypt
def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            shift = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - shift + key) % 26 + shift)
        else:
            result += ch
    return result

# Function to decrypt
def decrypt(text, key):
    return encrypt(text, -key)

# Brute force attack
def brute_force(cipher):
    print("\nBrute Force Results:")
    for k in range(1, 26):
        print("Key", k, ":", decrypt(cipher, k))


# Main program
text = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))

cipher = encrypt(text, key)
print("\nEncrypted Text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted Text:", plain)

# If key unknown → try all possibilities
brute_force(cipher)
