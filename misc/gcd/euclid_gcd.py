"""
По данным двум числам 1 ≤ a,b ≤ 2⋅10**9 найдите их наибольший общий делитель.
"""

import random

from algutils.graph import compare


def gcd_naive(a, b):
    assert a >= 0 and b >= 0
    for d in reversed(range(max(a, b) + 1)):
        if d == 0 or a % d == 0 and b % d == 0:
            return d


def euclid(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def euclid_recurse(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    elif a >= b:
        return euclid_recurse(a % b, b)
    else:
        return euclid_recurse(a, b % a)


def euclid_recurse_turbo(a, b):
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return max(a, b)
    return euclid_recurse_turbo(b % a, a)


def test(gcd):
    c = random.randint(1, 1024)
    a = c * random.randint(1, 128)
    b = c * random.randint(1, 128)
    assert gcd(a, a) == gcd(a, 0) == a
    assert gcd(b, b) == gcd(b, 0) == b
    assert gcd(a, 1) == gcd(b, 1) == 1
    expected = gcd_naive(a, b)
    d = gcd(a, b)
    assert a % d == b % d == 0 and d == expected


def run_tests(n_iter=100):
    for i in range(n_iter):
        test(gcd_naive)
        test(euclid)
        test(euclid_recurse)
        test(euclid_recurse_turbo)


if __name__ == "__main__":

    #run_tests()

    n = 10_000
    step = 1000
    steps = range(step, n+step, step)

    x_args = [x for x in steps]
    f_args = [(random.randint(10**(x-1), 10**x), random.randint(10**(x-1), 10**x)) for x in steps]
    print(x_args)
    print(f_args)

    compare([euclid], f_args, xs=x_args)
