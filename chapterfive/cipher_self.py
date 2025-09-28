from string import ascii_lowercase

def ceasars_cipher(S: str, shift=3):
    """the approach to avoid nested a quadratic runtime was to use two hashes,
    one containing letter -> index, and the other containing index -> letter. but this would have doubled
    the running time."""
    ...

def  ceasars_cipher2(S: str, shift=3):
    """this approach works for lower case characters"""
    start_index = ord('a')
    end_index = ord('z')
    new_str = []
    for i in S:
        if i.isalpha():
            new_value = ord(i) + shift
            if new_value > end_index:
                distance = end_index - ord(i)
                new_value = (shift - distance) - 1
                new_value = start_index + new_value

            new_str.append(chr(new_value))
        else:
            new_str.append(i)

    return ''.join(new_str)

print(ceasars_cipher2('watermelon', 3))
print(ceasars_cipher2('zuccini', 3))
print(ceasars_cipher2('the eagle is in play; meet at joe\'s'))
