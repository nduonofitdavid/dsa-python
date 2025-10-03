def str_to_int(s: str, index=0) -> int:
    """
    returns the integer representation of a string
    Note:
    At no time should the index parameter be provided
    """
    power = (len(s) - index) - 1
    int_value = ord(s[index]) - ord('0')
    value = int_value * (10 ** power)
    new_index = index + 1
    if new_index < len(s):
        value += str_to_int(s, new_index)
    return value

int_val = str_to_int('1353100000')
print(int_val)
print(type(int_val))

int_val = str_to_int('50')
print(int_val)
print(type(int_val))