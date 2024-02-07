def fib_last_digit(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b % 10

n = int(input())
print(fib_last_digit(n))
