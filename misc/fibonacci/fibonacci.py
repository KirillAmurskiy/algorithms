from functools import lru_cache
from algutils.graph import compare
from algutils.time import timed
from sys import setrecursionlimit


def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache(None)
def fib_recursive_cached(n):
    if n <= 1:
        return n
    else:
        return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)


def fib_array(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def fib_turbo(n):
    if n <= 1:
        return n
    f1, f2 = 0, 1
    for i in range(n - 1):
        f1, f2 = f2, f1 + f2
    return f2


if __name__ == "__main__":
    # setrecursionlimit(10_000)
    # print(timed(fib_recursive_cached, 1_000, n_iter=1))
    # print(timed(fib_array, 1_000, n_iter=1))
    # print(timed(fib_turbo, 1_000, n_iter=1))

    args = list(range(0, 15_000, 1000))
    compare([fib_array, fib_turbo], args)

