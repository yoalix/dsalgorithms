import sys
import random

def max_pairwise_product_naive(n, numbers):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if (numbers[i] * numbers[j] > result):
                result = numbers[i] * numbers[j]
    return result

# read from input
# read a list of integers into and array
n = int(input())
numbers = [int(x) for x in input().split()]
print(max_pairwise_product_naive(n, numbers))
