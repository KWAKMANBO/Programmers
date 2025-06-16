import sys

input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs1(start_node, val):
    x, y = start_node
    visited[x][y] = 1
    stack = [start_node]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] == val:
                stack.append((nx, ny))
                visited[nx][ny] = 1


area1 = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs1((i, j), board[i][j])
            area1.append(board[i][j])

area2 = []
visited = [[0] * N for _ in range(N)]
new_board = []

# 일반 영역 찾기
for i in range(N):
    new_board.append([])
    for j in range(N):
        if board[i][j] == 'R' or board[i][j] == 'G':
            new_board[i].append('R')
        else:
            new_board[i].append('B')
# 적록생명 영역 찾기
board = new_board
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            val = 'R' if board[i][j] != 'B' else 'B'
            dfs1((i, j), board[i][j])
            area2.append(board[i][j])

print(len(area1))
print(len(area2))
