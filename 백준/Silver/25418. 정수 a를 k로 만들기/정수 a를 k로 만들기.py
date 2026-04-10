from collections import deque
import sys

input = sys.stdin.readline

A, K = map(int, input().split())
visited = [0] * (K + 1)


def bfs(start):
    # (현재 값, 연산 횟수) 튜플로 저장
    dq = deque([(start, 0)])
    visited[start] = 1

    while dq:
        n = dq.popleft()
        if n[0] == K:
            return n[1]
        for top in (n[0] + 1, n[0] * 2):
            if top > K:
                continue
            if visited[top] == 0 and top <= K:
                visited[n[0]] = 1
                dq.append((top, n[1] + 1))


print(bfs(A))
