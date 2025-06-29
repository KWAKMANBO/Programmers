import sys

input = sys.stdin.readline
P = int(input())
t1, t2 = map(int, input().split())

N = int(input())
graph = {i: [] for i in range(1, P + 1)}
visited = [0] * (P + 1)

for _ in range(N):
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)

flag = False


def dfs(target1, target2, depth):
    global flag
    visited[target1] = 1
    if target1 == target2:
        flag = True
        print(depth)
        return
    for n in graph[target1]:
        if not visited[n]:
            dfs(n, target2, depth + 1)


dfs(t1, t2, 0)

if not flag:
    print(-1)
