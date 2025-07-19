import sys

input = sys.stdin.readline

# N 세로, M은 가로
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

island = 0
max_vol = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(start_node):
    vol = 0
    stack = [start_node]
    board[start_node[0]][start_node[1]] = 0

    while stack:
        x, y = stack.pop()
        vol += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx)
            # print(ny)
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = 0
                stack.append((nx, ny))

    return vol


for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            max_vol = max(max_vol, dfs((i, j)))
            island += 1

print(island)
print(max_vol)
