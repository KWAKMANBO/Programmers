import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

start = (0, 0)

# 목표지점 찾기
for i in range(N):
    if 2 in board[i]:
        start = (i, board[i].index(2), 0)
        break

queue = deque()
queue.append(start)
visited[start[0]][start[1]] = 1
board[start[0]][start[1]] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, cnt = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] != 0:
            visited[nx][ny] = 1
            board[nx][ny] = cnt + 1
            queue.append((nx, ny, cnt + 1))

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and board[i][j] == 1:
            board[i][j] = -1

for b in board:
    for i in b:
        print(i, end=" ")
    print()
