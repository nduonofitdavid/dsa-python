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


print(recursive_max([1,2,3,4,5,6,7]))
print(recursive_max([5, 1, 2, 10, 14]))

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



