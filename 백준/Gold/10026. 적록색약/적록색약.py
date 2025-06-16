import sys

from collections import deque

input = sys.stdin.readline

N = int(input())

board = [list(input().strip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(start_node, val):
    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and board[nx][ny] == val:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


# 빨강이랑 초록을 똑같이 판단
def bfs2( start_node, val):
    if val == 'G':
        val = 'R'

    queue = deque()
    queue.append(start_node)
    visited[start_node[0]][start_node[1]] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and board[nx][ny] == val:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


area1 = []
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs1((i, j), board[i][j])
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
            bfs2((i, j), board[i][j])
            area2.append(board[i][j])
            
print(len(area1))
print(len(area2))