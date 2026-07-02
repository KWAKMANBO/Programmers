from collections import deque
import copy


def solution(storage, requests):
    answer = 0
    N, M = len(storage), len(storage[0])

    # padding
    board = [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            board[i + 1][j + 1] = storage[i][j]

    def crain(req):
        for r in req:
            for i in range(1, N + 1):
                for j in range(1, M + 1):
                    if board[i][j] == r:
                        board[i][j] = 1

    def bfs(i, j):
        q = deque(())
        q.append((i, j))
        visited = set()
        visited.add((i, j))

        while q:
            x, y = q.popleft()

            if board[x][y] == 0:
                return True

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx <= N + 1 and 0 <= ny <= M + 1 and (nx, ny) not in visited:
                    if board[nx][ny] == 0 or board[nx][ny] == 1:
                        q.append((nx, ny))
                        visited.add((nx, ny))

        return False

    def forklift(req):

        new_board = copy.deepcopy(board)
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if board[i][j] == req and bfs(i, j):
                    new_board[i][j] = 1
        return new_board

    for req in requests:
        if len(req) > 1:
            crain(req)
        else:
            board = forklift(req)

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if board[i][j] != 0 and board[i][j] != 1:
                answer += 1
    return answer