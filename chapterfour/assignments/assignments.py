"""
Write an algorithm that finds the solution to cryptarithmetic puzzles, some of the
test cases are:

    pot + pan = bib
    dog + cat = pig
    boy + girl = baby
    
"""

def cryptarithmetic(): ...


"""

Implement the binary search algorithm using the iterative method

"""

def binary_search(data: list[int|float], target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] > target:
            high = mid - 1
        elif data[mid] < target:
            low = mid + 1
        
    return -1
    
data: list[int|float] = [1,2,3,4,5,6,7]
print(binary_search(data, 7))