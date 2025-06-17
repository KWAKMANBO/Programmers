import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def is_exist_zero(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return True
    return False


def bfs(start_nodes):
    queue = deque(start_nodes)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 0
    while queue:
        x, y, cnt = queue.popleft()
        answer = max(answer, cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
    return answer if not is_exist_zero(board) else -1


lst = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            lst.append((i, j, 0))

print(bfs(lst))
