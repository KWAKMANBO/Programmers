from collections import Counter


def solution(topping):
    answer = 0
    l = {}
    r = Counter(topping)

    for t in topping:
        if t not in l:
            l[t] = 1
        else:
            l[t] += 1

        r[t] -= 1
        if r[t] == 0:
            del r[t]

        if len(r) == len(l):
            answer += 1
    return answer