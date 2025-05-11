import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

# 전체 map을 저장할 board
board = []
# board에서 0인 즉 비어 있는 공간의 좌표를 저장할 리스트
empties = []
# virus의 좌표를 저장할 리스트
virus = []
# 3개의벽을 세운 좌표를 저장할 리스트
wall_combinations = []

for i in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    # virus의 좌표와, 비어 있는 곳의 좌표를 저장
    for j in range(M):
        if line[j] == 0:
            empties.append((i, j))
        if line[j] == 2:
            virus.append((i, j))


def infect_virus_bfs(maps):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dir[0]
            ny = y + dir[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                queue.append((nx, ny))
    return maps

def count_safe_area(maps):
    count = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                count += 1
    return count


def solve(walls):
    tmp_board = copy.deepcopy(board)
    for x, y in walls:
        tmp_board[x][y] = 1
    tmp_board = infect_virus_bfs(tmp_board)
    return count_safe_area(tmp_board)


wall_combinations = combinations(empties, 3)

result = 0
for c in wall_combinations:
    result = max(result, solve(c))
print(result)