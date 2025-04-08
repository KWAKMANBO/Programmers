from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

rx, ry, bx, by = 0, 0, 0, 0

visited = []

for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            bx, by = r, c
        if board[r][c] == 'R':
            rx, ry = r, c


def move(board, x, y, dx, dy):
    move_cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_cnt += 1

    return x, y, move_cnt


q = deque()

q.append((rx, ry, bx, by, 1))
visited.append((rx, ry, bx, by))
flag = False

while q:
    rx, ry, bx, by, result = q.popleft()
    if flag :
        break
    if result > 10:
        break

    for i in range(4):
        rnx, rny, rcnt = move(board, rx, ry, dx[i], dy[i])
        bnx, bny, bcnt = move(board, bx, by, dx[i], dy[i])
        if board[bnx][bny] == 'O':
            continue

        if board[rnx][rny] == 'O':
            print(result)
            flag = True
            break

        if rnx == bnx and rny == bny:
            if rcnt > bcnt:
                rnx -= dx[i]
                rny -= dy[i]
            else:
                bnx -= dx[i]
                bny -= dy[i]

        if (rnx, rny, bnx, bny) not in visited:
            visited.append((rnx, rny, bnx, bny))
            q.append((rnx, rny, bnx, bny, result + 1))
if not flag:
    print(-1)
