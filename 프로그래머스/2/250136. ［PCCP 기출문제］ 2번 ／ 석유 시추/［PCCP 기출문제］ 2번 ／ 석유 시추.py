from collections import deque


def solution(land):
    answer = 0
    N, M = len(land), len(land[0])

    answer = [0] * M
    visited = [[0 for _ in range(M)] for _ in range(N)]

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = 1
        cnt = 1
        cols = set()
        while q:
            x, y = q.popleft()
            cols.add(y)

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx , y + dy
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

        for c in cols:
            answer[c] += cnt

    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)



    return max(answer)