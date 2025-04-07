from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().strip()) for _ in range(n)]
visited = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

rx, ry, bx, by = 0, 0, 0, 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 'R':
            rx, ry = r, c
        if board[r][c] == 'B':
            bx, by = r, c


def move(x, y, dx, dy):
    move_cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_cnt += 1

    return x, y, move_cnt


def bfs(Rx, Ry, Bx, By):
    q = deque()
    q.append((Rx, Ry, Bx, By, 1))
    visited.append((Rx, Ry, Bx, By))

    while q:
        rx, ry, bx, by, result = q.popleft()

        if result > 10:
            break

        for i in range(4):
            rnx, rny, rcnt = move(rx, ry, dx[i], dy[i])
            bnx, bny, bcnt = move(bx, by, dx[i], dy[i])

            if board[bnx][bny] == 'O':
                continue

            if board[rnx][rny] == 'O':
                print(result)
                return

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
    print(-1)

bfs(rx, ry, bx, by)