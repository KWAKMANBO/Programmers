import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

visited = [0] * (N + 1)


def bfs(start_node, K):
    queue = deque()
    queue.append((start_node, 0))
    visited[start_node] = 1
    answer = []

    while queue:
        node, cnt = queue.popleft()
        if cnt == K:
            answer.append(node)

        for n in graph[node]:
            if visited[n] == 0:
                queue.append((n, cnt + 1))
                visited[n] = 1
    return answer


answer = bfs(X, K)
answer.sort()
if answer:
    for n in answer:
        print(n, end = " ")
else:
    print(-1)