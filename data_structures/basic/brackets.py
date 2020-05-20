"""Скобки в коде
Проверить, правильно ли расставлены скобки в данном коде.
Вход.Исходный код программы.
﻿Выход.Проверить, верно ли расставлены скобки. Если нет,выдать индекс первой ошибки.
Индексация с 1."""


class Item:

    def __init__(self, value, idx):
        self.value = value
        self.idx = idx
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value, idx):
        item = Item(value, idx)
        item.next = self.top
        self.top = item

    def pop(self):
        if self.top is None:
            return None
        res = self.top
        self.top = res.next
        return res

    def empty(self):
        return self.top is None


open_brackets = ['{', '(', '[']
close_brackets = ['}', ')', ']']

if __name__ == "__main__":
    s = input()
    stack = Stack()
    result = 'Success'

    for i in range(len(s)):
        c = s[i]
        if c in open_brackets:
            stack.push(c, i)
        elif c in close_brackets:
            pop_item = stack.pop()
            if pop_item is None \
                    or c == '}' and pop_item.value != '{' \
                    or c == ']' and pop_item.value != '[' \
                    or c == ')' and pop_item.value != '(':
                result = i + 1
                break

    if result == 'Success' and not stack.empty():
        unclosed_bracket = stack.pop()
        result = unclosed_bracket.idx + 1

    print(result)
