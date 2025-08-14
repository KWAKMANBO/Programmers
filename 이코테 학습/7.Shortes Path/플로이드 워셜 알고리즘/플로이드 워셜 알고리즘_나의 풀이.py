# Input
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2

import sys

input = sys.stdin.readline

# 노드 개수
n = int(input())
# 간선 개수
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s][e] = v

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])

for i in range(1, n+1):
    print(*graph[i][1:])


