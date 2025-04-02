from collections import deque


def solution(maps):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    m = len(maps)
    n = len(maps[0])
    q = deque([[0, 0]])

    # BFS
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                if nx == 0 and ny == 0 :
                    continue
                q.append([nx, ny])
                maps[nx][ny] = maps[x][y] + 1

    return maps[m-1][n-1] if maps[m-1][n-1] != 1 else -1