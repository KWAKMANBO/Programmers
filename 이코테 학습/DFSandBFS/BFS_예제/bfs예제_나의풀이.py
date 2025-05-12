from collections import deque

# 인접 리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

queue = deque([1])
visited = [False] * len(graph)
answer = []
while queue:
    node = queue.popleft()

    if not visited[node]:
        visited[node] = True
        answer.append(node)
        for n in graph[node]:
            queue.append(n)
print(answer)