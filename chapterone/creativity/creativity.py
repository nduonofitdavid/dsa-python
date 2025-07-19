from typing import Sequence
from string import punctuation

# C-1.13

def reverse_list(data: list[int]) -> list[int]:
    """This method uses slicing to reverse the list"""
    return data[::-1]

def reverse_list_2(data: list[int]) -> list[int]:
    """This method uses swapping operations to reverse the list"""
    length = len(data) - 1
    midpoint: int = length // 2
    for i in range(midpoint):
        data[i], data[length - i] = data[length - i], data[i]
    return data

# print(reverse_list_2([1, 2, 3, 4, 5]))

a: list = [1, 2, 3, 4, 5]

# python's builtin reverse method

a.reverse()
# print(a)


# C-1.14

def distinct_pair_odd(data: Sequence) -> bool:
    """this is the first approach using two loops, I still have to find
    a way to use one loop though
    """
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (data[i] * data[j]) % 2 != 0:
                return True
    return False


# C-1.15

def distinct_sequence(data: Sequence) -> bool:
    sum = 0
    for i in data:
        sum+=i
    if sum / len(data) == data[0]:
        return False
    return True


# C-1.16

"""This is because when it creates a new instance, with the new data, it assigns the identifier of the parameter to the new instance, while the garbage collector removes the previous instance to free up memory"""

# C-1.17

"""
In short, no the function would not work proply because the logic is flawed. Why?
The proposed approach in C-1.17 uses a value based for loop, so what this does is that it returns
each value from a list and then the value is scaled by a factor, but since we are scaling just the value returned and not the values in the list
itself as supposed to if we were using an indexed based for loop, when the loop ends, the values of the data sequence will still remain the same. That is to say we are not scaling in place, but rather just the individual values.
"""

# C-1.18
c_1_18 = [i * (i+1) for i in range(10)]
print(c_1_18)


#  C-1.19

chr_list = [chr(i) for i in range(97, 123)]
print(chr_list)


# C-1.20


# C-1.20

def eoferror():
    input_list: list = []
    try:
        while True:
            user_input = input('Enter a value: ')
            input_list.append(user_input)
    except EOFError:
        print("\n",input_list[::-1])


# eoferror()

# C-1.21


# C-1.22

def dot_product(a: Sequence, b: Sequence) -> Sequence:
    rows = len(a)
    col = a[0]
    if isinstance(col, Sequence):
        cols = len(a[0])
        # fix this 
    return [a[i] * b[i] for i in range(rows)]
    # they will have the same length, cause a and b must be of the same dimension
    # in order to take their dot product


# C-1.23

def c_1_23():
    c_twothree = [1, 2, 3, 4, 5]
    try:
        c_twothree[5] = 10
    except IndexError:
        raise IndexError("Don't try buffer overflow attacks in Python!")
    

# C-1.24
def count_vowels(word: str) -> int:
    vowels: set = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count


# C-1.25
def strip_punctuations(word: str) -> str:
    punctuations = set(punctuation)
    striped_string = ''.join([i if i not in punctuations else '' for i in word ])        
    return striped_string


# C-1.26
def corct_arth_order() -> bool:
    inputs = str(input("Enter the values of a, b and c seperated by a whitespace: "))
    inputs = inputs.split(' ')
    if len(inputs) > 3 or len(inputs) < 3:
        raise ValueError('You did not enter the values correctly try again')
    inputs = map(int,inputs)
    a, b, c = inputs
    return (a + b == c) or (a == b - c) or (a * b == c)