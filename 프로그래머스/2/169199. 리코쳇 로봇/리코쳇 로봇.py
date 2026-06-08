from collections import deque


def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    INF = int(1e9)
    visited = [[INF for _ in range(M)] for _ in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                visited[i][j] = 0
                q.append((i, j, 0))
                break
        if q:
            break

    while q:
        cx, cy, cnt = q.popleft()

        if board[cx][cy] == 'G':
            return cnt

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx, cy
            while 0 <= nx + dx < N and 0 <= ny + dy < M and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if visited[nx][ny] > cnt + 1:
                visited[nx][ny] = cnt + 1
                q.append((nx, ny, cnt + 1))


    return -1