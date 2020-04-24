"""По данной непустой строке s длины не более 104, состоящей из строчных букв латинского алфавита, постройте
оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате "letter: code". В
последней строке выведите закодированную строку. """

from collections import Counter, namedtuple
from heapq import heappush, heappop, heapify


class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, code_map, code):
        code_map[self.char] = code or '0'

    def __lt__(self, other):
        return True


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code_map, code):
        self.left.walk(code_map, code + '0')
        self.right.walk(code_map, code + '1')

    def __lt__(self, other):
        return True


class HaffmanCoder:

    code_map = None

    def __init__(self, s: str):

        heap = [(f, Leaf(char)) for char, f in Counter(s).items()]
        heapify(heap)

        tree = self.make_tree(heap)

        self.code_map = dict()
        tree.walk(self.code_map, '')

    def char_count(self):
        return len(self.code_map)

    @staticmethod
    def make_tree(heap):

        while len(heap) > 1:
            f1, left = heappop(heap)
            f2, right = heappop(heap)
            heappush(heap, (f1 + f2, Node(left, right)))

        f, root = heappop(heap)
        return root

    def code(self, s):
        result = []
        for c in s:
            result.append(self.code_map[c])
        return ''.join(result)


if __name__ == '__main__':

    s = input()

    coder = HaffmanCoder(s)
    coded_s = coder.code(s)

    print(coder.char_count(), len(coded_s))
    for k, v in coder.code_map.items():
        print('{0}: {1}'.format(k, v))
    print(coded_s)
