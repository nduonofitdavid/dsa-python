import random
from typing import Sequence

# R-1.1
def is_multiple(n: int, m: int) -> bool:
    return m % n == 0


# R-1.2
def is_even(k: int) -> bool:
    """
    How it works: This function works by checking the least significant bit of k
    and 2, if they are equal, that means k is even.
    """
    lsb_k, lsb_two = k & 1, 2 & 1
    return lsb_k == lsb_two


# R-1.3
def minmax(data: list[int]) -> tuple:
    min, max = data[0], data[0]
    for i in range(1, len(data)):
        if data[i] < min:
            min = data[i]
        if data[i] > max:
            max = data[i]
    return min, max

# R-1.4
def sum_small(n: int) -> int:
    """
    Description: THis function takes a positive integer n and returns the sum of the squares of all 
    the positive integers smaller than n.
    Params:
        n: int
    Return:
        sum: int
    """
    sum = 0
    for i in range(n):
        sum += i ** 2
    return sum


# R-1.5
def comphen_sum_small(n: int) -> int:
    return sum(i ** 2 for i in range(n))


# R-1.6
def odd_sum_small(n: int) -> int:
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            sum += i ** 2
    return sum


# R-1.7
def odd_sum_comphen(n: int) -> int:
    return sum(i ** 2 for i in range(n) if i % 2 != 0)

# R-1.8
# The equivalent of j is n + k
    

# R-1.9

a = range(50,90,10)
print(*a)


# R-1.10

b = range(8,-10,-2)
print(*b)


# R-1.11




# R-1.12
def custom_rand_choice(data: Sequence):
    length = len(data)
    index = random.randrange(length)
    return data[index]