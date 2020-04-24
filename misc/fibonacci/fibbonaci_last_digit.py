"""
Дано число 1 ≤ n ≤ 10^7, необходимо найти последнюю цифру n-го числа Фибоначчи.
"""


def fib_last_digit(n):
    if n <= 1:
        return n
    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = (fib[i-1] + fib[i-2]) % 10
    return fib[n]


if __name__ == "__main__":
    n = int(input())
    print(fib_last_digit(n))
