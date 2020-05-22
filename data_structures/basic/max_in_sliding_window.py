"""Максимум в скользящем окне.
Найти максимум в каждом окне размера m данного массива чисел A[1...n].
Вход.Массив чисел A[1...n] и число 1≤m≤n.
Выход.Максимум подмассива A[i...i+m−1] для всех 1≤i≤n−m+ 1."""

from collections import deque


class MaxQueue:
    def __init__(self):
        self.forward = deque()
        self.backward = deque()
        self.max_backward = deque()
        self.max_forward = deque()
        self.max_backward.append(-1)
        self.max_forward.append(-1)

    def enqueue(self, value):
        self.forward.append(value)
        self.max_forward.append(max(self.max_forward[-1], value))

    def dequeue(self):
        self.move_to_backward_if_need()
        value = self.backward.pop()
        self.max_backward.pop()
        return value

    def get_max(self):
        self.move_to_backward_if_need()
        return max(self.max_forward[-1], self.max_backward[-1])

    def move_to_backward_if_need(self):
        if not self.backward:
            while self.forward:
                value = self.forward.pop()
                self.max_forward.pop()
                self.backward.append(value)
                self.max_backward.append(max(self.max_backward[-1], value))


if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())

    queue = MaxQueue()
    result = []

    for i in range(m):
        queue.enqueue(a[i])
    result.append(queue.get_max())

    for i in range(m, n):
        queue.dequeue()
        queue.enqueue(a[i])
        result.append(queue.get_max())

    print(*result, sep=" ")
