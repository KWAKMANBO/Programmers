# Input 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# Input 2
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
    mins.append(min(b))

# 각 행에 최소값중에서 최댓값을 찾기
print(max(mins))
