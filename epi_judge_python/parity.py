from test_framework import generic_test

# Parity of a binary word is 1 if number of 1s in the word is odd otherwise its 0
# 1011 is 1 and 10001000 is 0

# My solution, brute force
def parity(x: int) -> int:
    num_of_ones = 0
    while (x != 0):
        num_of_ones += x & 1
        x >>= 1
    return (num_of_ones % 2)

def parity_solution_one(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
