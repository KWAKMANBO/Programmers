import sys


input = sys.stdin.readline


def dfs(start_node):
    cnt = 1
    visited[start_node] = 1
    stack = [start_node]
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if visited[n] == 0:
                stack.append(n)
                visited[n] = 1
                cnt += 1
    return cnt


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)

answer = [0] * (N + 1)

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    answer[i] = dfs(i)

max_cnt = max(answer)

for i in range(1, N + 1):
    if answer[i] == max_cnt:
        print(i, end=" ")
