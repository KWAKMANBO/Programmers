# Input1
# 3 3
# 1 2
# 1 3
# 2 3

# Input2
# 4 3
# 1 2
# 1 3
# 2 4

import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)

    if px == py:
        return True

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
flag = False
for _ in range(m):
    s, e = map(int, input().split())
    flag = union(parent, s, e)
    if flag:
        break
if flag:
    print("사이클 발생!!")
else:
    print("사이클 발생 X")

