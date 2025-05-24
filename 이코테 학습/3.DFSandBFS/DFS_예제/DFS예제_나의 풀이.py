# 인접 리스트
graph = [
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [0] * len(graph)


def dfs(startNode, graph, visited, answer):
    if visited[startNode - 1] == 0:
        visited[startNode - 1] = 1
        answer.append(startNode)

    for node in graph[startNode - 1]:
        if visited[node - 1] == 0:
            dfs(node, graph, visited, answer)

    return answer


print(dfs(1, graph, visited, []))
