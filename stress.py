import random
import sys
import os

# accept the number of test as a command line parameter
tests = int(sys.argv[1])
# accept the number of integers in the list as a command line parameter
n = int(sys.argv[2])

for i in range(tests):
    print("Test #", i)
    # run the gen.py script with parameter n and seed i
    os.system("python3 gen.py " + str(n) + " " + str(i) + " > input.txt")
    # run the 1-max-pair-products_naive.py script
    os.system("python3 1-max-pair-products_naive.py < input.txt > output1.txt")
    # run the 1-max-pair-products.py script
    os.system("python3 1-max-pair-products.py < input.txt > output2.txt")
    # compare the output of the two scripts
    with open("output1.txt") as file1: naive = file1.read()
    print("Naive: ",naive)
    with open("output2.txt") as file2: optimized = file2.read()
    print("Optimized: ",optimized)

    if naive != optimized:
            print("Test failed")
            break
