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
# 5 3 1
# 5 6 2

import sys

input = sys.stdin.readline

# n은 노드의 개수, m은 간선의 개수
n, m = map(int, input().split())
start = int(input())
INF = int(1e9)

# 2차원 배열로 인접 행렬을 생성
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 출발점에서 다른 노드들로의 비용을 담을 배열
dist = [INF] * (n + 1)
visited = [0] * (n + 1)

for _ in range(m):
    s, e, v = map(int, input().split())
    # s에서 e로 가는데 v의 비용이 듦
    graph[s][e] = v


def get_smallest():
    min_val = INF
    idx = 0
    for i in range(1, n + 1):
        # start에서 i로 가는 직접적인 경로가 있고 방문한 적이 없다면
        # dist에 저장하기
        if dist[i] < min_val and visited[i] != 1:
            min_val = dist[i]
            idx = i
    return idx


def dijkstra(start):
    dist[start] = 0
    visited[start] = 1

    for i in range(1, n + 1):
        if graph[start][i] != INF:
            dist[i] = graph[start][i]
    for i in range(n - 1):
        smallest = get_smallest()
        visited[smallest] = 1
        for j in range(1, n + 1):

            if graph[smallest][j] != INF:
                cost = dist[smallest] + graph[smallest][j]

                if cost < dist[j]:
                    dist[j] = cost


dijkstra(start)

for i in range(1, n + 1):
    print(f"{start} -> {i} : {dist[i] if dist[i] != INF else "INF"}")
