# input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

import sys

input = sys.stdin.readline

# 보드 크기 입력 받기
N, M = map(int, input().split())
# 시작 위치와 시작 방향 입력받기
x, y, dir = map(int, input().split())

# 북동남서 순서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# board입력받기
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

board[x][y] = 2

# 시작위치를 2로바꾸기
# 1이면 바다, 2이면 이미 방문한 곳임을 나타냄 즉 0이면 이동가능 1또는 2이면 이동 불가능
turn_cnt = 0
count = 1

while turn_cnt != 4:
    # 왼쪽 회전
    dir = (dir - 1) % 4

    nx = x + directions[dir][0]
    ny = y + directions[dir][1]
    # 경계를 벗어나지 않고
    if -1 < nx < N and -1 < ny < M:
        # 이동할 수 있는 곳이라면
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            x, y = nx, ny
            count += 1
        else:
            turn_cnt += 1

    if turn_cnt == 4:
        nx = x - directions[dir][0]
        ny = y - directions[dir][1]
        if -1 < nx < N and -1 < ny < M:
            if board[nx][ny] != 1:
                x = nx
                y = ny
                turn_cnt = 0
print(count)
