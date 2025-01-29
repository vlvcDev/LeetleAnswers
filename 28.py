# Write a function solve that reverses the digits of an integer. If the reversed integer overflows, return 0.

def solve(n):
    sign = -1 if n < 0 else 1
    n *= sign
    result = 0

    while n:
        result = result * 10 + n % 10
        n //= 10

    result *= sign

    if result > 2**31 - 1 or result < -2**31:
        return 0

    return result
