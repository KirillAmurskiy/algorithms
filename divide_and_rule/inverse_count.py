"""Первая строка содержит число 1≤n≤105, вторая — массив A[1…n], содержащий натуральные числа, не превосходящие 109.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j]. (Такая пара элементов называется инверсией
массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например,
в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют
каждые два элемента.) """

from collections import deque


class MergeSorter:

    def __init__(self, arr):
        self.arr = arr
        self.tmp = arr.copy()
        self.inverseCount = 0

    def run_sort(self):
        self.sort(0, len(self.arr))

    def sort(self, l, r):
        if l >= r - 1:
            return
        m = (l + r) >> 1
        self.sort(l, m)
        self.sort(m, r)
        self.merge(l, m, r)

    def merge(self, l, m, r):
        il, ir = l, m
        for i in range(l, r):
            if ir == r or (il < m and self.arr[il] <= self.arr[ir]):
                self.tmp[i] = self.arr[il]
                il += 1
            else:
                self.tmp[i] = self.arr[ir]
                self.inverseCount += m - il
                ir += 1
        for i in range(l, r):
            self.arr[i] = self.tmp[i]


count = 0


def inverse_count_nlogn(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    return merge(inverse_count_nlogn(arr[0:m]), inverse_count_nlogn(arr[m:]))


def merge(left, right):
    l, r = 0, 0
    global count
    result = []
    for i in range(len(left) + len(right)):
        if r == len(right) or (l < len(left) and left[l] <= right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            count += len(left) - l
            r += 1
    return result


def inverse_count_n2(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                counter += 1
    return counter


def max_inverse(n):
    return n * (n - 1) // 2


def test():
    global count

    examples = [
        ([1], 0),
        ([1, 2, 3, 4, 5], 0),
        ([2, 3, 9, 2, 9], 2),
        ([2, 1, 3, 4, 5], 1),
        ([8, 7, 6, 5, 4, 3, 2, 1], max_inverse(8))
    ]

    for example, inverseCount in examples:
        count = 0
        inverse_count_nlogn(example)
        sorter = MergeSorter(example.copy())
        sorter.run_sort()
        assert inverse_count_n2(example) == count == sorter.inverseCount == inverseCount

    import random

    for i in range(100):
        n = random.randint(1, 10 ** 3)
        arr = [random.randint(0, 10 ** 9) for j in range(n)]
        count = 0
        inverse_count_nlogn(arr)
        sorter = MergeSorter(arr.copy())
        sorter.run_sort()
        assert inverse_count_n2(arr) == count == sorter.inverseCount <= max_inverse(n)


def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    sorter = MergeSorter(arr)
    sorter.run_sort()
    print(sorter.inverseCount)


if __name__ == "__main__":
    #test()
    main()


def inverse_count_nlogn1(arr):
    """
    Посчитать количество инверсий алгоритмом основанном на очереди не удалось.
    Сбивается порядок, какой массив левый, какой правый.
    Сортирует нормально, а вот с подсчетом инверсий не прокатило
    """
    queue = deque()
    for i in range(len(arr)):
        queue.append([arr[i]])
    while len(queue) > 1:
        queue.append(merge(queue.popleft(), queue.popleft()))
    return queue.pop()
