"""По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков
содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤109,
задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек
несколько, выведите любое из них. """


def min_points_set(segments):
    last_point = segments[0][1]
    result = [last_point]
    for l, r in segments:
        if l > last_point:
            last_point = r
            result.append(last_point)
    return result


if __name__ == '__main__':
    n = int(input())
    segments = [[d for d in map(int, input().split())] for i in range(n)]
    segments.sort(key=lambda seg: seg[1])

    result = min_points_set(segments)

    print(len(result))
    print(*result)
