import sys
from collections import deque

input = sys.stdin.readline

N = 26

dp = deque()
dp.append((N, 0))
answer = 0
while True:
    num, cnt = dp.popleft()
    if num == 1:
        answer = cnt
        break

    if num % 5 == 0:
        dp.append((num // 5, cnt + 1))
    if num % 3 == 0:
        dp.append((num // 3, cnt + 1))
    if num % 2 == 0:
        dp.append((num // 2, cnt + 1))
    dp.append((num - 1, cnt + 1))

print(answer)
