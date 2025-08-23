# Input
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)

    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


# v는 정점 개수, e는 간선 개수
v, e = map(int, input().split())

edges = []
parent = [i for i in range(v + 1)]

for _ in range(e):
    # 출발점, 도착점, 비용 순서로 삽입
    s, e, c = map(int, input().split())
    edges.append((s, e, c))

edges.sort(key=lambda x: x[2])

answer = 0

for e in edges:
    start, end, cost = e
    ps = find(parent, start)
    pe = find(parent, end)
    if ps == pe:
        continue
    else:
        union(parent, start, end)
        answer += cost

print(answer)
