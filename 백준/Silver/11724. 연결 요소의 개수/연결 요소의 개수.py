import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N + 1)

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)


def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = 1


answer = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        answer += 1
print(answer)

