from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        lst = []
        for o in orders:
            for co in combinations(o,c):
                tmp = list(co)
                tmp.sort()
                lst.append("".join(tmp))
        cnt = Counter(lst)

        t = cnt.most_common(1)[0][1] if len(cnt) > 0 else -1
        if t == -1:
            continue
            
        for l in set(lst):

            if cnt[l] == t and cnt[l] > 1:
                answer.append(l)

    answer.sort()

    return answer