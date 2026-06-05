from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        lst = []
        for o in orders:
            lst.extend(combinations(sorted(o), c))

        most_ordered = Counter(lst).most_common()
        if len(most_ordered) < 1:
            continue
        most_value = most_ordered[0][1]
        tmp = []
        for k,v in most_ordered:
            if v == most_value and v > 1:
                tmp.append("".join(k))
        answer.extend(tmp)


    answer.sort()

    return answer
