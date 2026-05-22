from collections import Counter


def solution(weights):
    answer = 0
    c = Counter(weights)
    # 1:1 비율 구하기
    for k, v in c.items():
        if v > 1:
            answer += (v * (v - 1)) // 2

    # 나머지 비율 구하기
    for w in set(weights):
        if (2 / 3 * w) in weights:
            answer += c[w] * c[2 / 3 * w]
        if (1 / 2 * w) in weights:
            answer += c[w] * c[(1 / 2 * w)]
        if (3 / 4 * w) in weights:
            answer += c[w] * c[(3 / 4 * w)]

    return answer