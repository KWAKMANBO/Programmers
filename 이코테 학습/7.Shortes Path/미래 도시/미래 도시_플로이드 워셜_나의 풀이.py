# Input
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

import sys

input = sys.stdin.readline

# N은 회사 수
# M은 간선의 개수
N, M = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
dist = []

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1
X, K = map(int, input().split())

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer = graph[1][K] + graph[K][X]
print(answer if answer < INF else -1)
