# Input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)
indegree = [0] * (n + 1)

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    prerequisite = lst[1:-1] if len(lst) > 2 else []

    for j in prerequisite:
        graph[j].append(i)
        indegree[i] += 1


def topology_sort():
    queue = deque()
    result = [t for t in time]

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                queue.append(i)

    for r in result[1:]:
        print(r)


topology_sort()
