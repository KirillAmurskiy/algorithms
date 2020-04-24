"""
Даны целые числа 1≤n≤10**18 и 2≤m≤10**5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
"""


def fib_mod_pizano(n, m):
    if n <=1:
        return n
    fib = [0,1]
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % m)
        # Нашли период Пизано
        if fib[i-1] == 0 and fib[i] == 1:
            pi = i-1
            idx_result = n % pi
            return fib[idx_result]
    return fib[n]


def get_pizano(n, m):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % m)
        # Нашли период Пизано
        if fib[i-1] == 0 and fib[i] == 1:
            return i-1
    return n+1


def fib_mod_no_pizano(n, m):
    """
    Без периода Пизано, для тестов
    """
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append((fib[i-1] + fib[i-2]) % m)
    return fib[n]


def test():
    for n in range(300):
        for m in range(2, 30):
            no_pizano = fib_mod_no_pizano(n, m)
            pizano = fib_mod_pizano(n, m)
            if no_pizano != pizano:
                print('error n:{0}, m:{1}, no_pizano:{2}, pizano:{3}'.format(n, m, no_pizano, pizano))


if __name__ == "__main__":
    test()


