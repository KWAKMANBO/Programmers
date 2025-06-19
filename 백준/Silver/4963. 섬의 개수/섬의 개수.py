import sys

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def dfs(start_node):
    stack = [start_node]
    visited[start_node[0]][start_node[1]] = 1  # 시작점 방문 처리

    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx, ny))


while True:
    M, N = map(int, input().split())

    if N == 0 and M == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    island = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                dfs((i, j))
                island += 1
    print(island)
