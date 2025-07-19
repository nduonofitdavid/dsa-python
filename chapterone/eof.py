def eoferror():
    input_list: list = []
    try:
        while True:
            user_input = input('Enter a value: ')
            input_list.append(user_input)
    except EOFError:
        print("\n",input_list[::-1])


eoferror()