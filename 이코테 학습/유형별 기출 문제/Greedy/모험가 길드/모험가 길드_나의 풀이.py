# 현 재그룹의 인원이 공포도보다 높으면 그룹을 만듬
# 모든 헌터들을 사용할 필요가 없고 최대를 만들어라 → 그리디로 풀이해봄

import sys

input = sys.stdin.readline

n = int(input())
peoples = list(map(int, input().split()))

peoples.sort()

answer = 0
score = 0

for p in peoples:
    score += 1
    if score >= p:
        answer += 1
        score = 0

print(answer)
