from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# n(보드의 행,열 크기) 입력 받기
N = int(input())


# 출력용 함수
def print_board(board):
    for b in board:
        for i in b:
            print(i, end=" ")
        print()


# 매개변수로는 탐색 시작점을 받기
def bfs(cr, cc):
    q = deque()
    q.append((cr, cc))
    visited[cr][cc] = 1
    groups[-1].add((cr, cc))

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == board[cr][cc]:
                q.append((nr, nc))
                visited[nr][nc] = 1
                groups[-1].add((nr, nc))
        # 보드 설정


board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
Mid = N // 2
for k in range(4):  # 4번의 라운드 반복

    # 1. 그룹핑

    # 그룹핑에 사용할 변수 선언
    groups = []  # 각 그룹별 좌표가 [set()] 형식으로 저장될 예정
    nums = []  # 각 그룹별 Value값을 저장할 변수
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                curr_r, curr_c = (i, j)  # 처음으로 탐색 할 노드 의 좌표
                groups.append({(curr_r, curr_c)})
                nums.append(board[curr_r][curr_c])
                # BFS에 사용할 방문행렬 선언
                bfs(curr_r, curr_c)

    # 2. 점수 계산
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            g1, v1 = len(groups[i]), nums[i]
            g2, v2 = len(groups[j]), nums[j]
            score = (g1 + g2) * v1 * v2

            tmp = 0
            for ti, tj in groups[i]:
                for l in range(4):
                    if (ti + dr[l], tj + dc[l]) in groups[j]:
                        # print(f'{ti, tj} -> {ti + dr[l], tj + dc[l]} ')
                        tmp += 1
            answer += tmp * score

    # 3. 회전
    new_board = [[0] * N for _ in range(N)]

    for j in range(N):
        new_board[j][Mid] = board[Mid][N - 1 - j]
    for i in range(N):
        new_board[Mid][i] = board[i][Mid]

    parts = [(0, 0), (Mid + 1, 0), (0, Mid + 1), (Mid + 1, Mid + 1)]
    for pi, pj in parts:
        for i in range(Mid):
            for j in range(Mid):
                new_board[pi + i][pj + j] = board[pi + Mid - 1 - j][pj + i]

    board = new_board

    if k == 3:
        break

print(answer)
