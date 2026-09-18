from collections import deque


def solution(n, computers):
    answer = 0
    visited = set()

    def bfs(start_node):
        q = deque()
        q.append(start_node)
        visited.add(start_node)

        while q:
            node = q.popleft()

            for i in range(n):
                if computers[node][i] == 1 and i not in visited:
                    q.append(i)
                    visited.add(i)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and j not in visited:
                bfs(j)
                answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
