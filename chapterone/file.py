def is_even(a: int) -> bool:
    """an easy way to check if a function is even or not without using 
    the modulo operator, compares the least significant bit, and returns
    true if the bit is 0 and false otherwise"""

    if a & 1 == 0:
        return True
    return False


print(is_even(5))

# bitwise compliment in action
print(~(0b100))


# bitwise right shift
print(20 >> 4)

# bitwise left shift
print(20 << 4)


A = {1, 2, 3, 4, 5}
B = {6, 7, 8, 9, 10}

# union
print(A | B)

# intersection
print(A & B)

# in A but not in B
print(A - B)

# precisely in one of A or B
print(A ^ B)



# lists work differently whenw working with shorthand operators


alpha = [1, 2, 3]
beta = alpha # this creates an alias for alpha
beta += [4, 5] # extends the original list by 2 more elements
beta = beta + [6, 7] # reassignas beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha)
print(beta)