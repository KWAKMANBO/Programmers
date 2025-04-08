# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# board = [list(input().strip()) for _ in range(N)]
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# rx, ry, bx, by = 0, 0, 0, 0
#
# visited = []
#
# for r in range(N):
#     for c in range(M):
#         if board[r][c] == 'B':
#             bx, by = r, c
#         if board[r][c] == 'R':
#             rx, ry = r, c
#
#
# def move(board, x, y, dx, dy):
#     move_cnt = 0
#     while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
#         x += dx
#         y += dy
#         move_cnt += 1
#
#     return x, y, move_cnt
#
#
# q = deque()
#
# q.append((rx, ry, bx, by, 1))
# visited.append((rx, ry, bx, by))
# flag = False
#
# while q:
#     rx, ry, bx, by, result = q.popleft()
#     if flag :
#         break
#     if result > 10:
#         break
#
#     for i in range(4):
#         rnx, rny, rcnt = move(board, rx, ry, dx[i], dy[i])
#         bnx, bny, bcnt = move(board, bx, by, dx[i], dy[i])
#         if board[bnx][bny] == 'O':
#             continue
#
#         if board[rnx][rny] == 'O':
#             print(result)
#             flag = True
#             break
#
#         if rnx == bnx and rny == bny:
#             if rcnt > bcnt:
#                 rnx -= dx[i]
#                 rny -= dy[i]
#             else:
#                 bnx -= dx[i]
#                 bny -= dy[i]
#
#         if (rnx, rny, bnx, bny) not in visited:
#             visited.append((rnx, rny, bnx, bny))
#             q.append((rnx, rny, bnx, bny, result + 1))
# if not flag:
#     print(-1)

from collections import deque
import sys

input = sys.stdin.readline

# board의 행과 열 입력받기
N, M = map(int, input().split())

# 방문 여부를 담을 list
visited = []

# 보드 입력
board = [list(input().strip()) for _ in range(N)]

# R과 B의 위치 저장
# rx,ry는 Red
# bx,by는 Blue
rx, ry = 0, 0
bx, by = 0, 0

for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            bx, by = r, c
        if board[r][c] == 'R':
            rx, ry = r, c


# Red또는 Blue구슬을 움직이는 함수 구현
# 각 구슬별로 따로 진행
def move(board, x, y, dx, dy):
    # 구슬이 이동한 거리를 담을 변수
    # Red와 Blue가 겹쳐있을 경우 어떤 구슬을 뒤로 보내야할지 정하는데 사용
    move_cnt = 0

    # 구슬이 이동할 위치가 벽이아니고
    # 현재 구슬 위치가 빠져나가는 구멍이 아니라면 구슬을 이동 시키기
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        move_cnt += 1

    return x, y, move_cnt


#  Queue에는 Red의 좌표(rx,ry), Blue의 좌표(bx,by), 현재 Depth를 삽입
q = deque([(rx, ry, bx, by, 1)])

visited.append((rx, ry, bx, by))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = False

while q:
    rx, ry, bx, by, cnt = q.popleft()
    if flag:
        break
    if cnt > 10:
        break

    for i in range(4):
        rnx, rny, rcnt = move(board, rx, ry, dx[i], dy[i])
        bnx, bny, bcnt = move(board, bx, by, dx[i], dy[i])
        # blue가 상자를 빠져나가면 용납 X
        if board[bnx][bny] == 'O':
            continue

        if board[rnx][rny] == 'O':
            print(cnt)
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
            q.append((rnx, rny, bnx, bny, cnt + 1))
            visited.append((rnx, rny, bnx, bny))
if not flag:
    print(-1)