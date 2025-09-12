# non-recursive approach

def reverse_seq(S: list, n: int) -> list:
    S_copy: list = S.copy()
    zero_b_n: int = n - 1
    midpoint: int = zero_b_n // 2
    for i in range(midpoint):
        other_half_index: int = zero_b_n - i
        S_copy[i], S_copy[other_half_index] = S_copy[other_half_index], S_copy[i]
    return S_copy


seq = [1,2,3,4,5]
print(reverse_seq(seq, 5))



# recursive approach

def reverse_seq_rec(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse_seq_rec(S, start+1, stop-1)
    return S
print(reverse_seq_rec(seq, 0, len(seq)))