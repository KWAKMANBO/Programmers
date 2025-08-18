# Input1
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# Input 2
# 4 2
# 3 1
# 2 4
# 3 4

import sys
from collections import deque

input = sys.stdin.readline

# 노드 개수, 간선 개수
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

x, k = map(int, input().split())


# 비용이 1로 모두 동일하므로 BFS도 가능
def bfs(start_node):
    dist = [INF] * (n + 1)
    queue = deque()
    dist[start_node] = 0
    queue.append(start_node)

    while queue:
        cur = queue.popleft()

        for d in range(1, n + 1):
            if graph[cur][d] == 1 and dist[d] == INF:
                dist[d] = dist[cur] + 1
                queue.append(d)

    return dist


dist1 = bfs(1)
dist2 = bfs(k)

# 1에서 출발해 K로, K에서 X로
answer = dist1[k] + dist2[x]

print(answer if answer < INF else -1)
