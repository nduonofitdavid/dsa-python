def factorial(n: int) -> int:
    """Implementation of factorial without using recursion"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(5))

def factorial_recur(n: int) -> int:
    """Recursive implementation of the factorial function"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial_recur(5))


"""
The running time of the algorithm above can be characterised as O(n), as the function calls itself n+1 times, and in each call
all the operations performed make use of constant time.
"""