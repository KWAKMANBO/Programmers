# Input
# 3 2 1
# 1 2 4
# 1 3 2

import sys
import heapq

input = sys.stdin.readline
# n은 도시 개수
# m은 경로 개수
# c는 출발점
n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, v = map(int, input().split())
    # graph에는 (목적지, 경로) 순으로 삽입
    graph[s].append((e, v))


def dijkstra(start):
    dist = [INF] * (n + 1)
    # 우선순위 큐에는 (비용, 목적지)순으로 삽입
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        # 우선순위 큐에서 비용과 다음 목적지를 꺼내기
        cur_cost, cur = heapq.heappop(hq)

        if cur_cost > dist[cur]:
            # 비용이 목적지의 최소 경로보다 비싸다면 이미 계산됭 경로이므로 통과하기
            continue
        for i in graph[cur]:
            nd, nc = i
            cost = dist[cur] + nc
            if cost < dist[nd]:
                dist[nd] = cost
                heapq.heappush(hq, (dist[nd], nd))
    return dist

dist = dijkstra(c)
cnt = 0
time = 0
for d in dist:
    if d != INF and d !=0:
        cnt +=1
        time= max(time,d)
print(cnt, time)