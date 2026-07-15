# 가입자를 최대한 늘리는 것 > 이모티콘 판마액을 최대한 늘리는 것
import itertools
# 할인율은 10, 20, 30, 40% 만 가능

from itertools import product


def solution(users, emoticons):
    answer = []
    percent = [10, 20, 30, 40]

    le = len(emoticons)
    for p in itertools.product(percent, repeat=len(emoticons)):
        profit = 0
        count = 0
        new_emoticons = [(emoticons[i], p[i], emoticons[i] * (1 - p[i] / 100)) for i in range(le)]

        for u in users:
            tmp = 0
            for e in new_emoticons:
                if u[0] <= e[1]:
                    tmp += e[2]
            if tmp >= u[1]:
                count += 1
            else:
                profit += tmp
        answer.append((count, profit))

    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]