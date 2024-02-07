import random
import time

def primality(n):
    if n <= 1:
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
            return False

    for i in range(100):
        a = random.randint(2, n - 1)

        if pow(a, n - 1, n) != 1:
            return False
    return True

# n = int(input())
# prime_17 = 2281
# # took 4 seconds
# prime_18 = 3217
# # took 13 seconds
# prime_19 = 4253
# # took 27.863 seconds
# prime_20 = 4423
# # took 31.558 seconds

# n = pow(2, prime_20)-1
# # print(n)
# start_time = time.time()
# print(primality(n))
# end_time = time.time()
# print("Time taken:", end_time - start_time)
