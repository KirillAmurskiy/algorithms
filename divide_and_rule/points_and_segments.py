"""  В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой,
соответственно. Следующие nn строк содержат по два целых числа a_i и b_i (a_i ≤b_i) — координаты концов отрезков.
Последняя строка содержит mm целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке
появления во вводе выведите, скольким отрезкам она принадлежит.

Основные идеи решения:

1. Точка может находиться только на отрезке, начало которого меньше либо равны точке.
2. Нужно исключить из множества этих отрезков такие отрезки, на которых точка находиться
не может.
3. Точка не может находиться на отрезке, конец которого меньше чем точка.

Решение:

1. Сортируем отдельно начала отрезков и концы отрезков.
2. Для каждой точки:
2.1. Находим количество отрезков начала которых меньше либо равны точке.
2.2. Находим количество отрезков концы которых строго меньше точки.
2.3. Разность первого и второго значения и будет искомым значением.

Замечания:
1. Для сортировки используется алгоритм quick_sort3 со случайным выбором опорного элемента
и элиминацией хвостовой рекурсии, что позволяет гарантировать глубину рекурсии lon(n)
в худшем случае.
2. Сложность решения O((n+m)*log(n))
O(n*log(n) + n*log(n) + m*log(n) + m*log(n)) => O(2*n*log(n) + 2*m*log(n)) => O(2*log(n)*(n+m))
"""

import random


def quick_sort3(arr):
    if len(arr) < 2:
        return
    quick_sort_recursive_elimination(arr, 0, len(arr) - 1)


def quick_sort_recursive_elimination(arr, l, r):
    while l < r:
        m1, m2 = partition(arr, l, r)
        if (m1 - 1) - l < r - (m2 + 1):
            quick_sort_recursive_elimination(arr, l, m1 - 1)
            l = m2 + 1
        else:
            quick_sort_recursive_elimination(arr, m2 + 1, r)
            r = m1 - 1


def quick_sort_simple(arr, l, r):
    if l >= r:
        return

    m1, m2 = partition(arr, l, r)
    quick_sort_simple(arr, l, m1 - 1)
    quick_sort_simple(arr, m2 + 1, r)


def partition(arr, l, r):
    # get x randomly
    swap(arr, l, random.randint(l, r))
    x = arr[l]

    # partition
    j1 = l
    j2 = l
    for i in range(l + 1, r + 1):
        if arr[i] > x:
            continue
        elif arr[i] == x:
            j2 += 1
            swap(arr, j2, i)
        else:
            if j1 == j2:
                # have no elements that are equal to x
                j1 += 1
                j2 += 1
                swap(arr, j1, i)
            else:
                # have elements that are equal to x
                j1 += 1
                swap(arr, j1, i)
                j2 += 1
                swap(arr, j2, i)

    # set x in its place
    swap(arr, l, j1)
    return j1, j2


def swap(arr, idx1, idx2):
    tmp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = tmp


def bisect_left(arr, val):
    """Находим idx в отсортированном массиве для которого arr[0:idx-1] <= val.
    Практический смысл idx:
    1. По этому индексу нужно вставить val, чтобы массив остался отсортированным.
    2. idx=количество элементов в массиве меньших либо равных данному.
    Если в массиве все элементы больше val, то idx=0.
    Если в массиве все элементы меньше либо равны val, то idx=len(arr)."""
    l, r = 0, len(arr)
    m = 0

    while l < r:
        m = (l + r) // 2
        if arr[m] > val:
            r = m
        else:
            l = m + 1

    return l


def test():
    for i in range(10):
        n = random.randint(9, 10 ** 3)
        arr1 = [random.randint(0, 10 ** 3) for j in range(n)]
        arr2 = arr1.copy()
        arr1.sort()
        quick_sort3(arr2)
        assert arr1 == arr2


def main():
    n, m = map(int, input().split())

    starts = []
    ends = []
    for i in range(n):
        start, end = map(int, input().split())
        starts.append(start)
        ends.append(end)

    points = [int(i) for i in input().split()]

    quick_sort3(starts)
    quick_sort3(ends)

    for p in points:
        count_appropriate_starts = bisect_left(starts, p)
        count_inappropriate_ends = bisect_left(ends, p - 1)

        count_appropriate_segments = count_appropriate_starts - count_inappropriate_ends
        print(count_appropriate_segments, end=' ')


if __name__ == "__main__":
    # test()
    main()
