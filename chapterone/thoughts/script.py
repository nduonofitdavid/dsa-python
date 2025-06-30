def int_to_binary(n: int):
    """
    Description: Takes an integer and returns the binary version of that integer as a string.
    Params:
        n: int
    Return:
    """
    binary_str = ''
    while True:
        quotient, remainder = divmod(n, 2)
        binary_str = binary_str + f"{remainder}"
        n = quotient
        if quotient < 1:
            break   
    if len(binary_str) < 4:
        binary_str += '00'            
    return binary_str[::-1]


if __name__ == '__main__':
    print(int_to_binary(3))
    

