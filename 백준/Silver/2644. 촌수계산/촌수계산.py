import sys
from collections import deque

input = sys.stdin.readline
P = int(input())
t1, t2 = map(int, input().split())

# N = int(input())
# graph = {i: 0 for i in range(1, P + 1)}
#
# for _ in range(N):
#     parent, child = map(int, input().split())
#     graph[child] = parent

N = int(input())
graph = {i: [] for i in range(1, P + 1)}
visited = [0] * (P + 1)

for _ in range(N):
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)


# def dfs(start_node):
#     stack = [start_node]
#     pedigree = [start_node]
#     while stack:
#         node = stack.pop()
#         if graph[node]:
#             stack.append(graph[node])
#             pedigree.append(graph[node])
#
#     return pedigree
#
# p1 = dfs(t1)
# p2 = dfs(t2)

def bfs(target1, target2):
    queue = deque()
    visited[target1] = 1
    cnt = 0
    queue.append((target1, cnt))
    while queue:
        node, cnt = queue.popleft()
        if node == target2:
            return cnt

        for n in graph[node]:
            if visited[n] == 0:
                queue.append((n, cnt + 1))
                visited[n] = 1

    return -1


print(bfs(t1, t2))
