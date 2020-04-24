"""По данному числу 1≤n≤109 найдите максимальное число k, для которого n можно представить как сумму k различных
натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых. """


def get_max_k(n):
    cur_sum = 0
    k = 0
    sums = []
    for i in range(1, n + 1):
        k += 1
        if cur_sum + i + (i + 1) > n:
            sums.append(n - cur_sum)
            cur_sum += n - cur_sum
            break
        else:
            sums.append(i)
            cur_sum += i
    return k, sums


if __name__ == '__main__':
    n = int(input())
    k, sums = get_max_k(n)
    print(k)
    print(*sums)
