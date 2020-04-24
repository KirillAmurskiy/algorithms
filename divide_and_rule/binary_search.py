"""В первой строке даны целое число 1≤n≤105 и массив A[1…n] из n различных натуральных чисел, не превышающих 109,
в порядке возрастания, во второй — целое число 1≤k≤105 и k натуральных чисел b1,…,bk, не превышающих 109. Для каждого
i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет. """


def binary_search(arr, val):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == val:
            return m
        if arr[m] > val:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == '__main__':

    n, A = input().split(maxsplit=1)
    n, A = int(n), [int(num) for num in A.split()]

    k, B = input().split(maxsplit=1)
    k, B = int(k), [int(num) for num in B.split()]

    result = []
    for b in B:
        idx = binary_search(A, b)
        result.append(idx if idx == -1 else idx+1)

    print(*result)
