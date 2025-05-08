import copy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
answer = 0



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    tmp = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < N and -1 < ny < M:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2
                    q.append((nx, ny))

    global answer
    cnt = 0
    for i in tmp:
        for j in i:
            if j == 0:
                cnt += 1

    answer = max(answer, cnt)


def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                make_wall(cnt + 1)
                board[i][j] = 0

for _ in range(N):
    board.append(list(map(int, input().split())))

make_wall(0)
print(answer)
