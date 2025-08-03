import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

q = deque(range(1, N + 1))

while len(q) > 1:
    q.popleft()           # 제일 위 카드 버림
    q.append(q.popleft()) # 다음 카드 아래로

print(q[0])