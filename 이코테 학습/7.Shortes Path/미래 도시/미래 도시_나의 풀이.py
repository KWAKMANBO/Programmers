import sys

input = sys.stdin.readline

# N은 회사 수
# M은 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
dist = []

for _ in range(M):
    s, e = map(int, input())
    graph[s].append((e, 1))
    graph[e].append((s, 1))
