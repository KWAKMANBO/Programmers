# Input 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

#Input 2
# 2 4
# 7 3 1 8
# 3 3 3 4

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

mins = []
# 이중 for문 사용하기
for b in board:
    # 최소값을 저장할 변수 m
    m = 10001
    for i in b:
        # 현재 행에 존재하는 원소중 최솟값을 m에 저장
        if i < m:
            m = i
    # 최솟갓 리스트를 mins에 저장
    mins.append(m)

# 각 행에 최소값중에서 최댓값을 찾기
m = -1
for i in mins:
    if i > m:
        m = i

print(m)
