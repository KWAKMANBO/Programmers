import sys

input = sys.stdin.readline
ans = 0
# 초기 입력
N, M, H, K = map(int, input().split())

# 도망자 입력받기
arr = [list(map(int, input().split())) for _ in range(M)]

# 트리 입력받기
tree = set()
for _ in range(H):
    tree.add(tuple(map(int, input().split())))

# 도망자의 방향 정의
# 0(좌) 1(우) 2(하) 3(상)
rdx = [0, 0, 1, -1]
rdy = [-1, 1, 0, 0]
# 반대방향을 저장할 dictionary 선언
opposite = {0: 1, 1: 0, 2: 3, 3: 2}

# 방향 상 우 하 좌 -> 바깥 방향으로 돌때
tdx = [-1, 0, 1, 0]
tdy = [0, 1, 0, -1]

# mx_cnt는 최대 움직일 횟수를 의미
# cnt 현재 까지 움직인 횟수를 의미
# flag는 2번에 한번씩 mx_cnt 를 +1 해줘야되므로 해당 사실을 나타내는 flag
mx_cnt, cnt, flag, val = 1, 0, 0, 1
Mid = (N + 1) // 2
# 술래의 초기위치랑 이동 방향을 저장
ti, tj, td = Mid, Mid, 0

# K턴만큼 반복
for k in range(1, K + 1):
    # 1. 도망자의 이동
    for i in range(len(arr)):
        rx = arr[i][0]
        ry = arr[i][1]
        rdir = arr[i][2]
        # 술래와 도망자의 거리가 3 이하인 경우에만 이동 하도록
        if abs(rx - ti) + abs(ry - tj) < 4:
            rnx, rny = rx + rdx[rdir], ry + rdy[rdir]
            # 범위 내면 이동
            if 1 <= rnx <= N and 1 <= rny <= N:
                # 이동할 위치에 술래가 있다면
                if (rnx, rny) != (ti, tj):
                    arr[i][0], arr[i][1] = rnx, rny
            else:
                # 벽에 부딫친다면 방향을 바꾸기
                # 도망자의 방향을 바꾸기 위한 변수 rndx
                rnd = opposite[rdir]
                rnx, rny = rx + rdx[rnd], ry + rdy[rnd]
                # 술래가 아니면
                if (rnx, rny) != (ti, tj):
                    # 이동하고 방향을 변경
                    arr[i] = [rnx, rny, rnd]

            # 범위 밖이면

    # 2. 술래의 이동
    cnt += 1
    ti, tj = ti + tdx[td], tj + tdy[td]
    if (ti, tj) == (1, 1):
        # cnt를 1로 시작해야 N-1만큼 이동하기 때문에 1로 할당
        # 한방향으로 이동 하고 바로 꺾어야 하므로 1
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        # 방향은 아래방향으로 설정
        td = 2
    elif (ti, tj) == (Mid, Mid):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
    else:
        if cnt == mx_cnt:
            cnt = 0
            td = (td + val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val

    # 3 도망자 잡기
    # 술래가 자기 자리 포함 총 3칸을 탐색
    # (나무가 없는곳 이면 도망자를 잡음)
    tset = set(((ti, tj), (ti + tdx[td], tj + tdy[td]), (ti + tdx[td] * 2, tj + tdy[td] * 2)))
    for i in range(len(arr) - 1, -1, -1):
        # 술래가 탐색하는 영역에 현재 도망자가 재하고, 해당 칸에 나무가 없다면
        if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
            arr.pop(i)
            ans += k

    # 도망자가 없다면 더이상 점수가 없으므로 종료
    if not arr:
        break

print(ans)
