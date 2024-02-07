def fib_naive (n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib(n):
    if n <=1:
        return n
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input())
print(fib(n))
