import sys

c = int(input())
l = int(input())
graph = {i: [] for i in range(1, c + 1)}
for _ in range(l):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)

visited = [0] * (c + 1)

cnt = 0


def dfs(graph, start_node):
    global cnt
    visited[start_node] = 1
    for n in graph[start_node]:
        if visited[n] == 0:
            cnt += 1
            dfs(graph, n)

dfs(graph,1)
print(cnt)

