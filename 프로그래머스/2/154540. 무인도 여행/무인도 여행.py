from collections import deque


def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    visited = set()

    def bfs(start_node):
        sum_value = int(maps[start_node[0]][start_node[1]])
        q = deque()
        q.append(start_node)
        visited.add(start_node)

        while q:
            node = q.popleft()

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = node[0] + di, node[1] + dj

                if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] != 'X' and (ni, nj) not in visited:
                    q.append((ni, nj))
                    visited.add((ni, nj))
                    sum_value += int(maps[ni][nj])

        return sum_value

    for i in range(N):
        for j in range(M):
            if maps[i][j] !='X' and (i,j) not in visited:
                answer.append(bfs((i,j)))

    answer.sort()

    return answer if answer else [-1]