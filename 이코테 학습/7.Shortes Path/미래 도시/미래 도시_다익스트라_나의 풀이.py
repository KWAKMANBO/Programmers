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
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append((e, 1))
    graph[e].append((s, 1))

x, k = map(int, input().split())


def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    # 거리, 노드 순으로 삽입
    hq = [(0, start)]

    while hq:
        d, node = heapq.heappop(hq)
        if d > dist[node]:
            continue
        for next, w in graph[node]:
            next_dis = dist[node] + w
            if next_dis < dist[next]:
                dist[next] = next_dis
                heapq.heappush(hq, (dist[next], next))
    return dist


dist1 = dijkstra(1)
dist2 = dijkstra(k)

answer = dist1[k] + dist2[x]
print(answer if answer < INF else -1)
