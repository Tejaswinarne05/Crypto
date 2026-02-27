import random, string, time
from collections import Counter

# Caesar
def caesar(t): return ''.join(chr((ord(c)-65+3)%26+65) for c in t)

# Mono
def mono(t):
    a=list(string.ascii_uppercase)
    b=a[:]; random.shuffle(b)
    d=dict(zip(a,b))
    return ''.join(d[c] for c in t)

# Vigenere
def vig(t):
    k="KEY"
    return ''.join(chr((ord(t[i])-65+ord(k[i%3])-65)%26+65) for i in range(len(t)))

# Hill (fixed key 3 3 2 5)
def hill(t):
    if len(t)%2: t+='X'
    c=""
    for i in range(0,len(t),2):
        x,y=ord(t[i])-65,ord(t[i+1])-65
        c+=chr((3*x+3*y)%26+65)+chr((2*x+5*y)%26+65)
    return c

# Analysis
def analyze(name, func, text):
    s=time.time()
    c=func(text)
    t=time.time()-s
    rep=sum(1 for i in range(len(c)-1) if c[i]==c[i+1])
    print(f"{name}\t{c[:10]}...\t{rep}\t{round(t,6)}")

# Main
text=input("Enter Plaintext: ").upper().replace(" ","")

print("\nMethod\tCipher\tRepeated\tTime")
analyze("Caesar",caesar,text)
analyze("Mono",mono,text)
analyze("Vigenere",vig,text)
analyze("Hill",hill,text)
