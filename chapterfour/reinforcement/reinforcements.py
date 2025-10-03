# R-4.1

def recursive_max(sequence: list[int]) -> int:
    max_v = 0
    if len(sequence) > 0:
        max_v = sequence[0]
        max_inner = recursive_max(sequence[1:])
        if max_inner > max_v:
            max_v = max_inner
    else:
        raise Exception('Cannot find the maximum value in an empty list')
    return max_v


# print(recursive_max([1,2,3,4,5,6,7]))
# print(recursive_max([5, 1, 2, 10, 14]))

"""
The function recursive sum can be defined as f(x) => max(x), where x is a sequence.

While the length of the sequence is greater than zero, function f(x) compares the first element of the sequence, to the max of the other
elements in a new sequence, excluding the first element in the sequence recursively, if the value is greater than the max, which is assumed to be 
the first element in the sequence, they are swapped.

The function has a linear runtime, because only one activation record is created on each recursive call.
The space usage is 0(n), for still the same reason, lol, I dont know


"""


# R-4.2 ./R_4.2.png

# R-4.3 ./R_4.3.png

# R-4.4 ./rev_rcr.png

# R-4.6

"""
The function receives an integer n and then calculates the harmonic number of that integer
we can have a variable harmonic_no, and assign it the value of 1/n, then we subtract 1 from n, then if n
is greater than zero, we add a recursive call of the function with the decremented n to the harmonic_no variable, 
and then return it.
"""

# R-4.7

"""
The recursive function that will convert a string to its integer representation:

a function str_to_int, will take a string, and an index, the index is not to be used by the public, it is used during recursive calls only
by the function.

we will get the integer representation of an element in a string, by subtracting its ascii code from that of zero, and then we calculate a power n
by subtracting the length of the string from the position of the current character and 1, then we multiply the integer value for that string by 10 ** n, where n
is the power we computed, then we add 1 to the index, then if the new index is less than the length of the string, we add to the resulting value after computing the power
the recursive call of the string and the new index, otherwise we return the value.

see str_to_int.py
"""


# R-4.8

# The running time of isabel's algorithm is O(n)

def isabels_seq_sum(A):
    if len(A) % 2 != 0:
        raise Exception('The length of the sequence must be a multiple of 2')
    n_half = len(A) // 2
    B = [0] * n_half
    for i in range(len(B)):
        B[i] = A[2*i] + A[2*i + 1]
    if len(B) == 1:
        return B[0]
    return isabels_seq_sum(B)


# print(isabels_seq_sum([1,2,3,4,5,6,7,8]))

    