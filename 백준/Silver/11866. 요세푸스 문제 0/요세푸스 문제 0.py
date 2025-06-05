import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

# 1 2 3 4 5 6 7


lst = [i for i in range(1, N + 1)]
queue = deque(lst)
answer = []
idx = 0

while queue:
    for i in range(K):
        if i == K - 1:
            answer.append(queue.popleft())
        else:
            queue.append(queue.popleft())

print(f"<{', '.join(map(str, answer))}>")
