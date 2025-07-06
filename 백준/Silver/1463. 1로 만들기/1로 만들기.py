import sys
from collections import deque

input = sys.stdin.readline

dp = deque()

N = int(input())

dp.append((N, 0))

answer = 0
while dp:
    val, cnt = dp.popleft()

    if val == 1:
        answer = cnt
        break

    if val % 3 == 0:
        dp.append((val // 3, cnt + 1))

    if val % 2 == 0:
        dp.append((val // 2, cnt + 1))

    dp.append((val - 1, cnt + 1))

print(answer)