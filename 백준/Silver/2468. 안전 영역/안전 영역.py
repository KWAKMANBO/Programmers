import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = []

minimum = 101
maximum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_node, standard):
    queue = deque()
    queue.append(start_node)
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and board[nx][ny] > standard:
                visited[nx][ny] = 1
                queue.append((nx, ny))


for _ in range(N):
    tmp = list(map(int, input().split()))
    row_min = min(tmp)
    row_max = max(tmp)
    minimum = min(row_min, minimum)
    maximum = max(row_max, maximum)
    board.append(tmp)

max_cnt = 0
for i in range(minimum-1, maximum + 1):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if board[j][k] > i and visited[j][k] == 0:
                visited[j][k] = 1
                bfs((j, k), i)
                cnt += 1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
