def gcd(a, b):
    if b== 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)

def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    x_prime, y_prime, d = extended_gcd(b, a % b)
    x = y_prime
    y = x_prime - (a // b) * y_prime
    return (x, y, d)

# a = int(input())
# b = int(input())
# print(gcd(a, b))
