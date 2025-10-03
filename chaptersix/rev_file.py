from arrayadt import ArrayStack

def reverse_file_content(filename: str):
    S = ArrayStack()

    with open(filename, 'r') as fp:
        for line in fp:
            S.push(line.rstrip('\n'))

    with open(filename, 'w') as fp:
        while not S.is_empty():
            fp.write(S.pop() + '\n')


reverse_file_content('note.txt')
