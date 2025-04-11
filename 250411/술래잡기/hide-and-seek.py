import sys

input = sys.stdin.readline

# 규칙
# m명의 도망자, h명의 나무
# 도망자는 좌우, 또는 상하로만 움직일 수 있음
# 좌우는 오른쪽 보며 시작
# 상하는 아래를 보며 시작
# 술래는 정중앙에서 시작
# 도망자가 먼저 움직이고 -> 술래가 움직임 -> K번 반복

# 도망자는 술래와 거리가 3이하인 경우에만 이동
# 격자를 벗어나지 않는다면
# 술래가 있으면 움직이지 않기
# 술래가 없다면 해당 칸으로 이동
# 격자를 벗어나는 경우
# 방향을 반대로 틀고 술래가 없다면 1칸 이동
# 술래는 이동 후 이동 방향으로 탐색
# 나무가 있다면 도망자 못잡음
# 나무가 없다면 도망자 잡음
# K + 잡은 도망자의수

# 설계
# 굳이 board를 생성해서 할필요는 없어보임
# 1. 달팽이 이동 구현하기
# 1-1. 2번 같은 칸 수 만큼 움직이고 한칸씩 이동하는 규칙을 이용해서 구현
# 1-2. 반대로 돌아오는 방법 구현하기
# 출력용 보드만 생성했다가 지우기
# 2. 술래 이동 구현하기
# 3. 술래 탐색 구현하기


# 입력 받기
N, M, H, K = map(int, input().split())

# 도망자 좌표 입력받기
arr = []
for _ in range(M):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    arr.append([x, y, d])

# 도망자 이동방향
# 1이면 좌우 -> 우 먼저, 2이면 상하 -> 하 먼저
# 좌우하상 으로 선언
rdx = [0, 0, 1, -1]
rdy = [-1, 1, 0, 0]
opposite_dir = {0: 1, 1: 0, 2: 3, 3: 2}

# 나무 좌표 입력받기
tree = set()
for _ in range(H):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    tree.add((x, y))

# 술래 좌표 저장
Mid = N // 2
sx, sy = Mid, Mid

# 달팽이 이동 방향 구현에 사용할 변수들
# move_cnt : 현재 이동한 수를 담을 변수
# max_cnt : 현재 차례에서 이동해야하는 수를 의미 move_cnt와 비교하는데 사용
# flag : 2번 이동하고 max_cnt에 +1을 해줘야하는데 이를 판별하는데 사용하는 변수
# val :  역방향을 구현하는데 필요함 정방향일때는 1, 역방향일때는 -1
move_cnt, max_cnt, flag, val = 0, 1, 0, 1
# 상우하좌 방향
sdx = (-1, 0, 1, 0)
sdy = (0, 1, 0, -1)
sdir = 0

board = [[0 for _ in range(N)] for _ in range(N)]
answer = 0
for k in range(1, K + 1):

    # 1. 도망자의 이동
    for i in range(len(arr)):
        rx, ry, rdir = arr[i][0], arr[i][1], arr[i][2]
        # 해당 도망자와 술래와의 거리가 3이하라면 움직이게 하기
        if abs(rx - sx) + abs(ry - sy) <= 3:
            rnx, rny = rx + rdx[rdir], ry + rdy[rdir]
            # 격자를 벗어나지 않는다면
            if 0 <= rnx <= N - 1 and 0 <= rny <= N - 1:
                if (rnx, rny) != (sx, sy):  # 술래와 좌표가 다르다면
                    arr[i][0], arr[i][1] = rnx, rny
            else:  # 격자를 벗어난다면
                rdir = opposite_dir[arr[i][2]]
                arr[i][2] = rdir
                rnx, rny = rx + rdx[rdir], ry + rdy[rdir]
                # 이동하려는 칸에 술래가 없다면 이동하기
                if (rnx, rny) != (sx, sy):
                    arr[i][0], arr[i][1] = rnx, rny

    # 2. 술래의 이동
    # 달팽이 정방향 구현

    # 술래가 한번 이동 했음
    move_cnt += 1
    sx = sx + sdx[sdir]
    sy = sy + sdy[sdir]

    board[sx][sy] = k

    # 역뱡향으로 바꾸는 지점
    if (sx, sy) == (0, 0):
        # move_cnt 역방향일떄는 max_cnt가 1 더크므로 수를 맞추기 위해 1로시작
        # ex) 5일때는 정방향 최종 max_cnt가 5인데 (0,0)에서 (4,0)까지 4칸 이동해야하므로 cnt를 1로 설정
        # flag 역방향으로 돌떄는 한방향으로 이동후 바로 다음 방향으로 변경해줘야함
        # 원래는 두방향으로 이동후 max_cnt를 변경하지만
        # 역방향 맨처음에만 한방향으로 이동 후 max_cnt를 변경함
        # flag를 1로 설정하면 한 방향으로 이동 후 바로 max_cnt가 변경됨
        # val 역방향일때는 max_cnt가 줄어들어야하므로 val을 -1로 설정
        move_cnt, flag, val = 1, 1, -1
        # 역방향일때는 하방향으로 시작
        sdir = 2
    # 역방향에서 정방향으로 다시 탐색할떄 조건을 재설정
    elif (sx, sy) == (Mid, Mid):
        move_cnt, max_cnt, flag, val = 0, 1, 0, 1
        sdir = 0
    # 이동한 거리가 현재 방향에서 이동할 최대 거리에 도달했다면
    else:
        if move_cnt == max_cnt:
            move_cnt = 0
            sdir = (sdir + val) % 4
            if flag:
                flag = False
                max_cnt += val
            else:
                flag = True

    # 3 점수 계산
    sset = set()
    for i in range(3):
        sset.add((sx + sdx[sdir] * i, sy + sdy[sdir] * i))

    for i in range(len(arr) - 1, -1, -1):
        rx, ry = arr[i][0], arr[i][1]
        if (rx, ry) in sset and (rx, ry) not in tree:
            answer += k

print(answer)
