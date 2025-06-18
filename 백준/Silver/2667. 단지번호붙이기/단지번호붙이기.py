import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(start_node, val):
    x, y = start_node
    board[x][y] = val
    visited[x][y] = 1
    count = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                count += dfs((nx, ny), val)

    return count


val = 1
answer = []
nums = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            nums.append(dfs((i, j), val))
            answer.append(val)
            val += 1

print(len(answer))
nums.sort()

for n in nums:
    print(n)