"""Стек с поддержкой максимума.
﻿Реализовать стек с поддержкой операций push,pop и max.
Вход. Последовательность запросов push,pop и max.
Выход. Для каждого запроса max вывести максимальное﻿ число, находящееся на стеке."""


class Item:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.max = None

    def push(self, value):
        item = Item(value)
        item.next = self.top
        self.top = item

        max_item = Item(value)
        if self.max is not None \
                and self.max.value > value:
            max_item.value = self.max.value

        max_item.next = self.max
        self.max = max_item

    def pop(self):
        if self.top is None:
            return None
        res = self.top
        self.top = res.next

        self.max = self.max.next
        return res

    def get_max(self):
        return self.max.value

    def empty(self):
        return self.top is None


if __name__ == "__main__":
    q = int(input())
    stack = Stack()

    for i in range(q):
        command = input()
        if command.startswith("push"):
            value = int(command.split()[1])
            stack.push(value)
        elif command.startswith("pop"):
            stack.pop()
        elif command.startswith("max"):
            print(stack.get_max())
