# Input
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
edges = []


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa


for _ in range(m):
    s, e, c = map(int, input().split())
    edges.append((c, s, e))

edges.sort()
answer = 0
biggest = 0
for e in edges:
    cost, start, end = e
    if find(parent, start) == find(parent, end):
        continue
    union(parent, start, end)
    answer += cost
    biggest = cost
print(answer - biggest)
