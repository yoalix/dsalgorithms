from gcd import gcd, extended_gcd
from primality import primality
import random

def modinv(a, m):
    x, y, d = extended_gcd(a, m)
    if d != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m

def generatePrime(bits):
    while True:
        n = random.getrandbits(bits)
        if primality(n):
            return n

def rsaDecrypt(n, d):
    return lambda c: pow(c, d, n)

def rsaEncrypt(n, e):
    return lambda m: pow(m, e, n)

def rsaKeygen(p, q):
    n = p * q
    phi = (p - 1) * (q - 1) # find the coprimes of n
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = modinv(e, phi)
    return (n, e, d)

def main():
    p = generatePrime(2048)
    q = generatePrime(2048)
    print('p:', p)
    print('q:', q)
    n, e, d = rsaKeygen(p, q)
    print('n:', n)
    print('e:', e)
    print('d:', d)
    m = 'hello world'
    print('m:', m)
    encrypt = rsaEncrypt(n, e)
    decrypt = rsaDecrypt(n, d)
    encoded_m = []
    for c in m:
        encoded_m.append(encrypt(ord(c)))
    print('c:', encoded_m)
    decoded_m = ''
    for c in encoded_m:
        decoded_m += chr(decrypt(c))
    print('m:', decoded_m)

main()
