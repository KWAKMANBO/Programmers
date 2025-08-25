# Input
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

import sys
from collections import deque

input = sys.stdin.readline

# v는 정점의 개수, e는 간선의 개수
v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]
# 진입 차수를 저장
degree = [0] * (v + 1)

for _ in range(e):
    s, e = map(int, input().split())
    graph[s].append(e)
    degree[e] += 1





queue = deque([i for i in range(1,v+1) if degree[i] == 0])
answer = []

while queue:
    node = queue.popleft()
    answer.append(node)
    for e in graph[node]:

        degree[e] -= 1
        if degree[e] == 0:
            queue.append(e)

for a in answer:
    print(a, end = " ")
