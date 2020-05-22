"""Высота дерева.
﻿Вычислить высоту данного дерева.
Вход. Корневое дерево с вершинами {0, ..., n−1}, заданное как последовательность
parent0, ...,parentn−1, где parenti — родитель i-й вершины.
Выход. Высота дерева."""

from collections import deque

if __name__ == "__main__":
    n = int(input())
    parents = [int(parent) for parent in input().split()]

    root = None
    adjacency_list = [deque() for i in range(n)]
    for item in range(len(parents)):
        parent = parents[item]
        if parent == -1:
            root = item
            continue
        adjacency_list[parent].append(item)

    stack = deque()
    stack.append((root, 1))
    max_height = 0
    while stack:
        item, height = stack.pop()
        if height > max_height:
            max_height = height
        for child in adjacency_list[item]:
            stack.append((child, height + 1))

    print(max_height)
