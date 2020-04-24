"""Первая строка входа содержит число операций 1≤n≤105. Каждая из последующих n строк задают операцию одного из
следующих двух типов:

Insert x, где 0≤x≤109 — целое число;
ExtractMax.
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
"""


class MaxHeap:

    items = []

    def insert(self, d):
        self.items.append(d)
        self.swift_up(self.last_idx())

    def extract_max(self):
        if self.is_empty():
            return None
        result = self.items[0]
        self.change(0, self.last_idx())
        self.items.pop()
        self.swift_down(0)
        return result

    def swift_up(self, idx):
        parent_idx = self.get_parent_idx(idx)
        if parent_idx is None:
            return
        if self.items[idx] <= self.items[parent_idx]:
            return
        else:
            self.change(idx, parent_idx)
            self.swift_up(parent_idx)

    def swift_down(self, idx):
        max_child_idx = self.get_max_child_idx(idx)
        if max_child_idx is None:
            return
        if self.items[idx] < self.items[max_child_idx]:
            self.change(idx, max_child_idx)
            self.swift_down(max_child_idx)

    def last_idx(self):
        return len(self.items) - 1

    def get_parent_idx(self, child_idx):
        if child_idx == 0:
            return None
        return child_idx // 2

    def get_max_child_idx(self, parent_idx):
        child1_idx, child2_idx = self.get_children_idxs(parent_idx)
        if child1_idx is None and child2_idx is None:
            return None
        if child2_idx is None:
            return child1_idx
        return child2_idx if self.items[child2_idx] > self.items[child1_idx] else child1_idx

    def get_children_idxs(self, parent_idx):
        child1_idx = parent_idx*2 if parent_idx*2 < len(self.items) else None
        child2_idx = parent_idx*2 + 1 if parent_idx*2 + 1 < len(self.items) else None
        return child1_idx, child2_idx

    def change(self, idx1, idx2):
        self.items[idx1], self.items[idx2] = self.items[idx2], self.items[idx1]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == '__main__':

    n = int(input())
    operations = [input() for i in range(n)]

    heap = MaxHeap()

    for operation in operations:
        if 'ExtractMax' in operation:
            print(heap.extract_max())
        elif 'Insert' in operation:
            operation, arg = operation.split()
            heap.insert(int(arg))
