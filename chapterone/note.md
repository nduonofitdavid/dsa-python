# Bitwise operations

- Bitwise operations are operations that are performed on the bits of a number. When the number is passed in, that number is converted into binary, and then operations are performed on the bits of that number.


## Examples of bitwise operations

- ~ bitwise compliment
- & bitwise and
- | bitwise or
- ^ bitwise x-or
- << shifts bits left, filling in with zeros
- \>> shifts bits right, filling in with sign bit.

## Bitshifting

- The bit shifts are sometimes considered bitwise operations, because they treat a value as a series of bits rather than as a numerical quantity. In these operations, the digits are moved, or shifted, to the left or right.

- Since registers have a fixed boundary, some bits will be shfted out of one end, while the same number of bits are shifted in from the other end.

- So what this basically does is shift a bit a number of places to the right or to the left.



# Sequence types
- All sequences defines comparison operations based on lexicographic order, performing an element by element comparison until the first difference is found.

- Therefore [5, 6, 9] < [5, 7] because of the entries at index 

- Comparison operators in sets are not done lexicographically, because they are not ordered, but are rather done based on mathematical notation of a subset.

## Lexicographically

- This means in alphabetical order, like words in a dictionary. It describes the way things are ordered based on their position in a dictionary or similar reference, comparing characters or elements from left to right.

## Iterators and Generators

- In python, the mechanism for iteration is based upon the following convensions:

1. An iterator: This is an object that manages an iteration through a series of values. If i is an iterator object, next(i) returns the next element in the underlying series, and a StopIteration exception is raised if the object reaches the end of its lifecycle.

2. An iterable: This is an object that produces an iterator via the syntax iter(obj).

- The for loop syntax automates this, creating an iter object for the iterable, and then repeatedly calling the next function until it catches a StopIteration exception.

- The iterator object does not create a copy of the iterable, but instead maintains a current index to the original iterable, so if the original list is modified after the iterator is constructed, but before the iteration is complete, the iterator will be reporting the updated contents of the list.

- Python's range function uses lazy evaluation, it does not return a list of numbers, but instead a range object that is iterable, this object generates a list of numbers; It returns a range object that is iterable. This object generates n number of values one at a time, only as needed. This is advantageous as in the case of the premature termination of a loop over that range, that was no extra computational resources was spent for the remaining values, only for the values that were used.

- The keys function, values function and items function all use lazy evaluation.

- It is illegal to combine both yield and return to indicate a result. This indicates to python that we are defining a generator, rather than a traditional function. Except during zero return statements, where you are trying to stop the generators execution.


- Python's conditional expression is a substitute for ternary operators found in other programming languages.

- A conditional statement itself can serve as a parameter to a function.

- Generator comprehensions are preferable when you dont want to store the values in memory.

- data = 1, 2, 3, 4, 5 -> this will be treated as a tuple. This behaviour is called automatic packing of a tuple. This is useful when returning a tuple from a function e.g return x, y -> this returns a tuple (x, y).

- the divmod function returns the pair of values (a // b, a % b) associated with a single integer division.


# Packing and Unpacking of Sequences

- Python supports automatic packing, in automatic packing, comma seperated values on the rhs are treated as a tuple and then assigned to the identifier on the lhs.

e.g

data = 1, 2, 3, 4, 5

data will be treated as a tuple containing (1, 2, 3, 4, 5)

# Random Number Generation

- Random numbers in python are generated using a pseudo-random number generator. This type of algorithm needs a seed, a starting point in which other random numbers will be generated from. Since making use of the same seed will produce the same results, one can use a timed user input or the current system time in milliseconds.


# Operations on Least Significant Bits

- The LSB is the rightmost bit in a binary representation of a number, holding the lowest place value (2 ^ 0).

## Common operations on LSB

- Getting the LSB. To obtain the value of the LSB, you can use the bitwise AND operator with 1

``` python

lsb = num & 1

```

- To ensure the LSB is set to 1, use the bitwise OR operator | with 1

``` python

lsb = num | 1

```

- In order to set the LSB to 0, use the bitwise AND operator with the bitwise NOT of 1.

``` python

num = 11
num_clear_lsb = num & ~1

```

- To toggle the LSB (0 to 1, 1 to 0), use the bitwise XOR operator with 1.

``` python

num = 10
num_toggled_lsb = num ^ 1

```

- To extract the N least significant bits, you can use a bitmask created by (1 << N) - 1 and then perform a bitwise AND operation.

``` python

num = 25
n_bits = 3
mask = (1 << n_bite) - 1
extracted_bit = num & mask

```

## Bitmask

- A bitmask is a sequence of bits used to manipulate other bits within a binary number or data structure.

