from typing import Dict, List, Sequence

# p-1.29

# this does not work, turns out the solution is permutation.
def all_possible_strings(data: Sequence) -> int:
    length = len(data)
    return (length * length) - length

print(all_possible_strings(['c', 'a', 't', 'd', 'o', 'g']))

def all_possible_strings_2(data: Sequence) -> int:
    result = 1
    for i in range(1, len(data) + 1):
        result = result * i
    return result

print(all_possible_strings_2(['c', 'a', 't', 'd', 'o', 'g']))


# p-1.30

def repeated_divide_count(n: int) -> int:
    result = n
    count = 0
    while result >= 2:
        result = result // 2
        count += 1
    return count


print(repeated_divide_count(10))


# p-1.31

def change_machine(price: int, paid: int) -> dict:
    change: int = int(paid) - int(price)
    currency_units: List[int] = [1000, 500, 200, 100, 50, 20, 10, 5]
    temp_change: int = 0
    change_dict: Dict[int, int] = {}

    if change < 5:
        return {"message": "No change, sorry"}
    for i in currency_units:
        unit_count: int = 0

        while True:
            temp_change += i
            if temp_change > change:
                temp_change = temp_change - i
                change_dict[i] = unit_count
                break
            if temp_change == change:
                unit_count += 1
                change_dict[i] = unit_count
                break
            unit_count += 1
        
    return {"Change breakdown": change_dict}


print(change_machine(150, 30000))

# p-1.32

def simple_calculator():
    """
    use a while loop to keep reading input from the console and then appending it to a list, 
    but if the input is = or just blank as in enter, you then calculate the result, also watch out
    for strings and other signs that may cause an error.
    """
