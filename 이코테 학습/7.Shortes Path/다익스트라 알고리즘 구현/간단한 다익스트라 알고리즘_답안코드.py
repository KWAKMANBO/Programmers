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
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    # a는 시작점
    # b는 종점
    # c는 a에서 b로 가는데 드는 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx


def dijkstar(start):
    distance[start] = 0
    visited[start] = True

    for i in range(1, n + 1):
        for j in graph[start]:
            distance[j[0]] = j[1]

    # n-1번 반복해서 각 노드별 최단 거리 찾기
    for i in range(n - 1):
        smallest = get_smallest()
        visited[smallest] = True
        for j in graph[smallest]:
            cost = distance[smallest] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstar(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
