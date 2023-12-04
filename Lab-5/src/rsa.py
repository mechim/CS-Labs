import random
from sympy import isprime
import math

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1 
        
        if isprime(num):
            return num


def choose_public_exponent(phi_n):
    e = 65537

    while not (1 < e < phi_n and math.gcd(e, phi_n) == 1):
        e = random.randint(2, phi_n - 1)

    return e

msg = "Echim Mihail"
m = int(''.join(str(ord(char)) for char in msg))
print("Message ~ 'Echim Mihail' ~", m)

bits = 1054
prime1 = generate_large_prime(bits)
prime2 = generate_large_prime(bits)

n = prime1 * prime2
phi_n = (prime1 - 1) * (prime2 - 1)

e = choose_public_exponent(phi_n)


d = pow(e, -1, phi_n)
print("Prime 1:", prime1)
print("Prime 2:", prime2)
print("Product (n):", n)
print("Bit Length of Product:", n.bit_length())
print("Phi(n):", phi_n)
print("Public Exponent (E):", e)
print("Private Exponent (D):", d)

ciphertext = pow(m, e, n)
print("\nCiphertext:", ciphertext)

decrypted_message = pow(ciphertext, d, n)
print("Decrypted Message:", decrypted_message)
print(f"RSA works? ==> {m == decrypted_message}")