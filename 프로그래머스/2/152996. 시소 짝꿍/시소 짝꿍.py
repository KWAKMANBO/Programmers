from collections import Counter


def solution(weights):
    answer = 0
    counter = Counter(weights)

    # 1:1 비율 부터 계산
    for k, v in counter.items():
        if v > 1:
            answer += v * (v - 1) // 2

        if (2/3)*k in counter:
            answer += v * counter[(2/3)*k]
        if (1/2)*k in counter:
            answer += v * counter[(1/2)*k]
        if (3/4)*k in counter:
            answer += v * counter[(3/4)*k]

    return answer