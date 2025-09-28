def linear_power(x, n):
    if n == 0:
        return 1
    return x * linear_power(x, n-1)

# print(linear_power(2, 1000))

# You quickly see that this method is inefficient as it uses linear time and there is potential for it
# to make use of the limited number of activation records (Reaching the recursion depth).

def log_power(x, n) -> int | float:
    if n == 0:
        return 1
    partial = log_power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
        result *= x
    return result

def exp(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    if n % 2 == 0:
        return exp(x*x, n//2)
    return x * exp(x*x, n//2)


# this was my solution to the leetcode problem, but this solution is inefficient, as it uses O(n) runtime
# so it means that for the power n, it will perform n - 1 operations, this approach is not feasible for large powers

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        is_minus: bool = False
        if n + abs(n) == 0:
            is_minus = True
            n = abs(n)
        result = 0
        power = x
        for _ in range(1, n):
            power = power * x
        result = 1 / power if is_minus else power
        return result
    

solution = Solution()
print(solution.myPow(-3,3))


# other loop approach

class Solution:
    def myPow(self, x: float, n: int) -> float:

        result = 1.0

        n_copy = n

        if n_copy < 0:
            x = 1.0 / x
            n_copy = -n_copy

        while n_copy > 0:
            if n_copy % 2 != 0:
                result *= x

            x *= x
            n_copy //= 2

        return result 