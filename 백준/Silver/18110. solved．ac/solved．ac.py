import sys

input = sys.stdin.readline

N = int(input())

def custom_round(n):
    r = n - int(n)
    if r >= 0.5:
        return int(n) + 1
    else:
        return int(n)


# 아무 의견이 없다면 난이도는 0
if N == 0:
    print(0)
# 의견이 하나라도 있다면 절사 평균으로 구함
else:

    scores = []

    for _ in range(N):
        scores.append(int(input()))

    scores.sort()
    cut = custom_round(N * 0.15)
    valid_scores = scores[cut: N - cut]

    print(custom_round(sum(valid_scores) / (N - (2 * cut))))
