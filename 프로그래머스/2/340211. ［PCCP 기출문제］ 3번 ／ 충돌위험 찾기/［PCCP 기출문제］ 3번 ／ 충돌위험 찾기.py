from collections import Counter


def solution(points, routes):
    answer = 0
    robots = []
    ln = 0
    for r in routes:
        tmp = []
        for i in range(len(r) - 1):
            src = [points[r[i] - 1][0], points[r[i] - 1][1]]
            dest = [points[r[i + 1] - 1][0], points[r[i + 1] - 1][1]]
            if i == 0:
                tmp.append((src[0], src[1]))

            dir = 1 if src[0] < dest[0] else -1
            while src[0] != dest[0]:
                src[0] += dir
                tmp.append((src[0], src[1]))
            dir = 1 if src[1] < dest[1] else -1
            while src[1] != dest[1]:
                src[1] += dir
                tmp.append((src[0], src[1]))
        robots.append(tmp)
        ln = max(len(tmp), ln)

    for i in range(ln):
        t = []
        for r in robots:
            if i < len(r):
                t.append(r[i])
        cnts = Counter(t)
        for c in cnts:
            if cnts[c] > 1:
                answer += 1

    return answer