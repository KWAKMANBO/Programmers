# Input1
# 2
# 홍길동 95
# 이순신 77

import sys

input = sys.stdin.readline

N = int(input())

scores = []

for _ in range(N):
    name, score = input().split()
    score = int(score)
    scores.append([name, score])

scores.sort(key=lambda x: (x[1], x[0]))

for s in scores:
    print(s[0], end = ' ')