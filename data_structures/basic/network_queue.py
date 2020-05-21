"""Обработка сетевых пакетов.
Реализовать обработчик сетевых пакетов.
Вход.
Размер буфера size и число пакетов n, а так-﻿же две последовательности
arrival1, ..., arrivaln и duration1, ..., durationn, обозначающих время поступления
и длительность обработки n пакетов.
Выход. Для каждого из данных n пакетов необходимо вывести время начала его обработки или −1,
если пакет не был обработан (это происходит в случае, когда пакет поступает в момент, когда
в буфере компьютера уже находится size пакетов)."""


import sys
from collections import deque

if __name__ == '__main__':
    reader = (map(int, s.split()) for s in sys.stdin)
    size, n = next(reader)
    # store completion time of task
    queue = deque()
    for arrival, duration in reader:
        while queue and queue[0] <= arrival:
            queue.popleft()
        if len(queue) < size:
            start_time = arrival
            if queue:
                start_time = max(arrival, queue[-1])
            print(start_time)
            queue.append(start_time + duration)
        else:
            print(-1)
