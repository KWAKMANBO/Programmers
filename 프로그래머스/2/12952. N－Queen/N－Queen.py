def solution(n):
    answer = 0

    board = [[0] * n for _ in range(n)]

    def check(r, c):
        # col확인
        i = r - 1
        while i >= 0:
            if board[i][c] == 1:
                return False
            i -=1

        # 왼쪽 대각선 위 확인
        i = r - 1
        j = c - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # 오른쪽 대각선 위 확인
        i = r - 1
        j = c + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def dfs(r):
        nonlocal answer
        if r == n:
            answer += 1
            return

        for j in range(n):
            if check(r, j):
                board[r][j] = 1
                dfs(r + 1)
                board[r][j] = 0

    dfs(0)
    return answer
