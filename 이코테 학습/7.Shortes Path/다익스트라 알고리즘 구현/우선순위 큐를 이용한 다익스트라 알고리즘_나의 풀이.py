# Input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 6 2
# 5 3 1

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
dist = [INF] * (n + 1)

for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    dist[start] = 0

    # # 시작점에서 갈 수 있는 노드로의 비용을 추가하기
    # for g in graph[start]:
    #     dist[g[0]] = g[1]
    #     heapq.heappush(hq, (g[1],g[0]))

    while hq:
        smallest = heapq.heappop(hq)
        # 방문을 안했따면
        if visited[smallest[1]] == 1:
            continue
        visited[smallest[1]] = 1
        for g in graph[smallest[1]]:
            cost = dist[smallest[1]] + g[1]
            if cost < dist[g[0]]:
                dist[g[0]] = cost
                heapq.heappush(hq, (cost, g[0]))


dijkstra(start)

for i in range(1,n+1):
    if dist[i] == INF:
        print(INF)
    else:
        print(dist[i])
