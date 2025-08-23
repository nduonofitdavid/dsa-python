from typing import TypeAlias, Callable
import time

Number: TypeAlias = int | float

data: list[Number] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# O(n^2) approach

def prefix_average1(array: list[Number]) -> list[Number]:
    n = len(array)
    A: list[Number] = [0] * n
    for i in range(n):
        total = 0
        for j in range(i+1):
            total += array[j]
        A[i] = total / (i + 1)
    return A

# Linear-Time Algorithm O(n) approach

def prefix_average2(array: list[Number]) -> list[Number]:
    n = len(array)
    A: list[Number] = [0] * n
    total: Number = 0
    for i in range(n):
        total += array[i]
        A[i] = total / (i + 1)
    return A

def get_runtime(function: Callable, data: list[Number]) -> float:
    start = time.time()
    function(data)
    end = time.time()
    return start - end

print(get_runtime(prefix_average1, data=data))
print(get_runtime(prefix_average2, data=data))