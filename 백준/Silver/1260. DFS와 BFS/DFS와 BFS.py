import sys
from collections import deque

input = sys.stdin.readline

N, M, S = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs_answer = []

for k in graph:
    graph[k].sort()


def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = True
    bfs_answer.append(start_node)
    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True
                bfs_answer.append(n)


dfs_answer = []


def dfs(start_node):
    dfs_answer.append(start_node)
    visited[start_node] = True
    for n in graph[start_node]:
        if not visited[n]:
            dfs(n)

visited = [False] * (N + 1)
dfs(S)
for i in dfs_answer:
    print(i, end = " ")
print()
visited = [False] * (N + 1)
bfs(S)
for i in bfs_answer:
    print(i, end = " ")


