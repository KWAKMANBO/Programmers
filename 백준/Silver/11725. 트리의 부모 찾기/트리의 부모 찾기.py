import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

graph = {i: [] for i in range(1, N + 1)}

for i in range(N - 1):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)


answer = [0] * (N + 1)
answer[1] = 1


def dfs(start_node):
    stack = [start_node]
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if answer[n] ==0:
                answer[n]= node
                stack.append(n)
dfs(1)

for i in range(2, N+1):
    print(answer[i])