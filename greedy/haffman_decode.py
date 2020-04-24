"""
Восстановите строку по её коду и беспрефиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв, встречающихся в
строке, и размер получившейся закодированной строки, соответственно. В следующих k строках записаны коды букв в
формате "letter: code". Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке. В
качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке
хотя бы один раз. Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв
непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.


В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит 104 символов. """

"""По данной непустой строке s длины не более 104, состоящей из строчных букв латинского алфавита, постройте
оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки. В следующих k строках запишите коды букв в формате "letter: code". В
последней строке выведите закодированную строку. """


class TreeItem:

    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right


class HaffmanDecoder:
    tree = None

    def __init__(self, code_map: dict):
        self.tree = TreeItem()
        for char, code in code_map.items():
            current_item = self.tree
            for c in code:
                if c == '0':
                    if not current_item.left:
                        current_item.left = TreeItem()
                    current_item = current_item.left
                else:  # c == '1'
                    if not current_item.right:
                        current_item.right = TreeItem()
                    current_item = current_item.right
            current_item.char = char

    def decode(self, coded_s: str):
        result = []
        current_item = self.tree
        for c in coded_s:
            if c == '0':
                current_item = current_item.left
            if c == '1':
                current_item = current_item.right
            if current_item.char:
                result.append(current_item.char)
                current_item = self.tree
        return ''.join(result)


if __name__ == '__main__':
    k, l = map(int, input().split())

    code_map = dict()

    for i in range(k):
        char, code = input().split(sep=': ')
        code_map[char] = code

    coded_s = input()

    decoder = HaffmanDecoder(code_map)
    decode_string = decoder.decode(coded_s)
    print(decode_string)
