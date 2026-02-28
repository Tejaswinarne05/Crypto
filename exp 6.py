# Rail Fence Cipher

def rail_encrypt(text, rails):
    fence = ['' for _ in range(rails)]
    row, step = 0, 1

    for ch in text:
        fence[row] += ch
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return ''.join(fence)


def rail_decrypt(cipher, rails):
    pattern = [[] for _ in range(rails)]
    row, step = 0, 1

    for ch in cipher:
        pattern[row].append('*')
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    index = 0
    for r in range(rails):
        for c in range(len(pattern[r])):
            pattern[r][c] = cipher[index]
            index += 1

    result = ''
    row, step = 0, 1
    for _ in cipher:
        result += pattern[row].pop(0)
        if row == 0:
            step = 1
        elif row == rails - 1:
            step = -1
        row += step

    return result


text = input("Enter text: ").replace(" ", "").upper()
r = int(input("Enter rails: "))
cipher = rail_encrypt(text, r)
print("Encrypted:", cipher)
print("Decrypted:", rail_decrypt(cipher, r))
