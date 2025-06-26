def fibonacci(count: int):
    a: int = 0
    b: int = 1
    n: int = 0
    while n < count:
        yield a
        future: int = a + b
        a = b
        b = future
        n += 1


    
print(*fibonacci(14))