import sys
import random

# def max_pairwise_product_naive(n, numbers):
#     result = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if (numbers[i] * numbers[j] > result):
#                 result = numbers[i] * numbers[j]
#     return result

def max_pairwise_product(n, numbers):
    max1 = 0
    max2 = 0
    for i in range(n):
        if (numbers[i] > max1):
            max2 = max1
            max1 = numbers[i]
        elif (numbers[i] > max2):
                max2 = numbers[i]
    return max1 * max2


# Generate a list of positive integers from 1 to 1 million
# print(numbers)
# Print the number of integers in the list
# print(len(numbers))
# def main():
#     while(True):
#         n = random.randint(2, 100)
#         a = random.sample(range(1, 100000), n)
#         print(n)
#         print(a)

#         res1 = max_pairwise_product_naive(n, a)
#         res2 = max_pairwise_product(n, a)
#         if (res1 != res2):
#             print('Wrong answer: {} {}'.format(res1, res2))
#             break
#         else:
#             print('OK')

# main()
# numbers = list(range(1, 1000001))
# print(max_pairwise_product(len(numbers), numbers))

# read from input
# read a list of integers into and array
n = int(input())
numbers = [int(x) for x in input().split()]
print(max_pairwise_product(n, numbers))
