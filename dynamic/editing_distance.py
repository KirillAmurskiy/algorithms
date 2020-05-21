"""Расстояние редактирования.
Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита."""

if __name__ == "__main__":
    s1 = input()
    s2 = input()

    d = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        d[i][0] = i
    for j in range(len(s2) + 1):
        d[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            c = 0 if s1[i - 1] == s2[j - 1] else 1
            ins = d[i][j - 1] + 1
            delete = d[i - 1][j] + 1
            replace = d[i - 1][j - 1] + c
            d[i][j] = min(ins, delete, replace)

    print(d[len(s1)][len(s2)])
