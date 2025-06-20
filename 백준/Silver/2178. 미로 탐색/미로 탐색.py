import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
            cnt += 1
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))

print(visited[N - 1][M - 1])
