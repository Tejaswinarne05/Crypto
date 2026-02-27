import random
import string


alphabet = list(string.ascii_uppercase)
shuffled = alphabet.copy()
random.shuffle(shuffled)

key = dict(zip(alphabet, shuffled))

print("Substitution Key:")
for k in key:
    print(k, "->", key[k])


text = input("\nEnter a word: ").upper()


cipher = ""
for ch in text:
    if ch in key:
        cipher += key[ch]
    else:
        cipher += ch

print("\nEncrypted Text:")
print(cipher)


freq = {}
for ch in cipher:
    if ch in string.ascii_uppercase:
        freq[ch] = freq.get(ch, 0) + 1


sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 Most Frequent Letters:")
for letter, count in sorted_freq[:3]:
    print(letter, ":", count)
