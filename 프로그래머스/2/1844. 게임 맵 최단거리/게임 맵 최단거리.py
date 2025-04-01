from collections import deque


def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])
    r, c = 0, 0
    # bfs
    q = deque([[r, c]])
    visited = set()
    while q:
        r, c = q.popleft()
        visited.add((r, c))
        if r + 1 <= m - 1 and maps[r + 1][c] == 1 and (r + 1, c) not in visited:
            maps[r + 1][c] = maps[r][c] + 1
            q.append([r + 1, c])
        if r - 1 >= 0 and maps[r - 1][c] == 1 and (r - 1, c) not in visited:
            maps[r - 1][c] = maps[r][c] + 1
            q.append([r - 1, c])
        if c + 1 <= n - 1 and maps[r][c + 1] == 1 and (r, c + 1) not in visited:
            maps[r][c + 1] = maps[r][c] + 1
            q.append([r, c + 1])
        if c - 1 >= 0 and maps[r][c - 1] == 1 and (r, c - 1) not in visited:
            maps[r][c - 1] = maps[r][c] + 1
            q.append([r, c - 1])

    return maps[m - 1][n - 1] if maps[m - 1][n - 1] != 1 else -1