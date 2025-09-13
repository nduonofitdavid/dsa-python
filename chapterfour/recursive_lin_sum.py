def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S ,n-1) + S[n-1]
    

print(linear_sum([1,2,3,4,5], 5))


"""

When considering summation of integers in a list S, if S is trivally 0, if n = 0, and otherwise
that it is the sum of the first n - 1 integers in S plus the last element in S.

So we can use this to recursively sum the whole list.

"""

def loop_sum(S, n):
    sum = 0
    if n == 0:
        return sum
    for i in range(n):
        sum += S[i]
    return sum
    

# binary recursive sum

def binary_sum(S, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return S[start]
    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)