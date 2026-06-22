from collections import deque


def solution(maps):
    N, M = len(maps), len(maps[0])

    q = deque()
    q.append((0, 0, 1))
    visited = set()

    while q:
        x, y, c = q.popleft()

        if (x,y) == (N-1,M-1):
            return c

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):

            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 0 and (nx, ny) not in visited:
                q.append((nx, ny, c + 1))
                visited.add((nx, ny))

    return -1