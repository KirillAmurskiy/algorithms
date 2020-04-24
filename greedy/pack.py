
"""Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. Каждая из следующих n строк
задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106 предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость
частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально
уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой. """


class Item:
    def __init__(self, c, w):
        self.c = int(c)
        self.w = int(w)
        self.c0 = self.c/self.w

    def __str__(self):
        return '{0} {1} {2}'.format(self.c, self.w, self.c0)


def get_max_с(items, W):
    items.sort(key=lambda item: item.c0, reverse=True)

    sum_c = 0
    for item in items:
        if item.w < W:
            sum_c += item.c
            W -= item.w
        else:
            sum_c += item.c0 * W
            break
    return sum_c


def test():
    items = [Item(60, 20), Item(100, 50), Item(120, 30)]
    W = 50
    c = get_max_с(items, W)
    print('{0:.3f}'.format(c))
    assert c == 180


if __name__ == '__main__':
    test()
    n, W = map(int, input().split())
    items = [Item(*input().split()) for i in range(n)]

    c = get_max_с(items, W)

    print('{0:.3f}'.format(c))
