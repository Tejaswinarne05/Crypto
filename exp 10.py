# Brute Force Columnar (key length 2 to 5)

import itertools

def brute_force(cipher):
    for key_len in range(2, 6):
        print("\nTrying key length:", key_len)
        perms = itertools.permutations(range(key_len))
        for p in perms:
            try:
                rows = len(cipher) // key_len
                matrix = ['' for _ in range(rows)]
                index = 0
                for col in p:
                    for row in range(rows):
                        matrix[row] += cipher[index]
                        index += 1
                print("Key:", p, "->", ''.join(matrix))
            except:
                pass

cipher = input("Enter ciphertext: ").upper()
brute_force(cipher)
