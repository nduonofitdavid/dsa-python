def harmonic_number(n: int) -> int | float:
    harmonic_no = 1
    for i in range(2, n+1):
        harmonic_no += 1/i
    return harmonic_no
    

# print(harmonic_number(10))
        

def harmonic_number_recursive(n: int) -> int | float:
    harmonic_no = 1/n
    n_copy = n - 1
    if n_copy > 0:
        harmonic_no += harmonic_number_recursive(n_copy)
    return harmonic_no


# print(harmonic_number_recursive(10))