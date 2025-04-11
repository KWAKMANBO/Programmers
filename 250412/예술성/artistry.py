import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
Mid = N // 2

answer = 0


def bfs(si, sj):
    q = deque()
    q.append((si, sj))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[si][sj] = 1
    groups[-1].add((si, sj))  # 새좌표를 그룹에 추가

    while q:
        ci, cj = q.popleft()
        for di, dj in zip(dx, dy):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and board[ni][nj] == board[ci][cj]:
                # ni,nj가 범위를 안벗어나고, 방문하지 않은 점이고, 같은 값이라면
                q.append((ni, nj))
                visited[ni][nj] = 1
                groups[-1].add((ni, nj))


# 점수는 4번 구해야하므로
for k in range(4):
    # 1. 예술점수 구하기
    # 1-1. 그룹나누기
    # 1-2. 그룹의 조합 구하고 그룹의 점수 구하기
    groups = []  # gropu들을 set로 저장하기위한 리스트
    nums = []  # 각 그룹별 index를 저장할 리스트

    # 미방문 숫자를 만나면 BFS
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 미방문이라면
            if visited[i][j] == 0:
                groups.append(set())
                nums.append(board[i][j])
                # bfs구현하기
                bfs(i, j)

    # 1-2. 점수구하기
    cnt = len(nums)
    for i in range(0, cnt - 1):
        for j in range(i + 1, cnt):
            # 가능한 모든 조합 구하기
            point = (len(groups[i]) + len(groups[j])) * nums[i] * nums[j]  # 인접면 마다 계산
            for ci, cj in groups[i]:
                for ni, nj in ((ci + 1, cj), (ci - 1, cj), (ci, cj + 1), (ci, cj - 1)):
                    if (ni, nj) in groups[j]:  # 인접한 좌표가 그룹 j에 있다면
                        answer += point

    # 2. 회전 시키기
    # 2-1. 십자가 모형 반시계 방향으로 회전 시키기
    # 2-2. 부분 사각형 시계 방향으로 회전 시키기

    new_arr = [[0] * N for _ in range(N)]
    # 십자가 회전
    for i in range(N):
        new_arr[Mid][i] = board[i][Mid]
    for j in range(N):
        new_arr[j][Mid] = board[Mid][N - 1 - j]

    # 부분 네모 회전
    for (si, sj) in ((0, 0), (Mid + 1, 0), (0, Mid + 1), (Mid + 1, Mid + 1)):
        for i in range(Mid):
            for j in range(Mid):
                new_arr[si + i][sj + j] = board[si + Mid - 1 - j][sj + i]
    board = new_arr
    if k == 3:  # 4번째 시도 후에는 회전시킬 필요가 없음
        break

print(answer)
