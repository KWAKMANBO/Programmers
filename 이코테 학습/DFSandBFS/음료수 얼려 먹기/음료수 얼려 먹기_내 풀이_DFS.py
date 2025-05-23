import sys

input = sys.stdin.readline

# input1
# 4 5
# 00110
# 00011
# 11111
# 00000

# input2
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# DFS는 재귀를 사용

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# visited는 매개변수로 제공 x -> 그냥 접근할 수 있음
#
def dfs(start_node):
    x, y = start_node
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and board[nx][ny] == 0:
            dfs((nx, ny))


answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and board[i][j] == 0:
            dfs((i, j))
            answer += 1

print(answer)
