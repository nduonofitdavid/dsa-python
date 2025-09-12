def binary_search(data, target, low, high):
    """Implementation of the binary search algorithm."""
    if low > high:
        return False
    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    if data[mid] > target:
        return binary_search(data, target, low, mid-1)
    elif data[mid] < target:
        return binary_search(data, target, mid+1, high)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
low = 0
high = len(data) - 1
print(binary_search(data, 6, low, high))

"""
The binary search algorithm runs in O(log n) time for a sorted sequence with n elements.

"""