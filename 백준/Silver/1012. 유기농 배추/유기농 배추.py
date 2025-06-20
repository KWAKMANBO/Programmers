import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_node):
    queue = deque()
    queue.append(start_node)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = 0
                queue.append((nx,ny))

for tc in range(TC):
    N, M, C = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    for _ in range(C):
        x, y = map(int, input().split())
        board[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs((i, j))
                cnt += 1

    print(cnt)
