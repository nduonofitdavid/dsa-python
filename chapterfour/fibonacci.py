def bad_fibonacci(n):
    if n <= 1:
        return n 
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
    
print(bad_fibonacci(20))
    
def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)
    

# print(bad_fibonacci(10))
# print(good_fibonacci(10))

def fibonacci_loop(n):
    first = 0
    final = 1
    for _ in range(1,n):
        temp = final
        final += first
        first = temp

    return final

print(fibonacci_loop(3))