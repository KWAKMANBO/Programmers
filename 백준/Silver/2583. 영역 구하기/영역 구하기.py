import sys

from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

board = [[0] * N for _ in range(M)]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())

    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []


def bfs(start_node):
    queue = deque()
    x, y = start_node
    board[x][y] = 1
    queue.append((x, y))
    extent = 0
    while queue:
        x, y = queue.popleft()
        extent += 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny))

    answer.append(extent)


for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            bfs((i, j))

answer.sort()

print(len(answer))
print(*answer)
