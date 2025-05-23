# BFS로 풀어보기

# input1
# 4 5
# 00110
# 00011
# 11111
# 00000

# input2
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0


def bfs(start_node):
    global answer
    queue = deque([start_node])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = start_node
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '0':
                    if visited[nx][ny] == 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = 1
    answer += 1


for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            if visited[i][j] == 0:
                bfs((i, j))

print(answer)
