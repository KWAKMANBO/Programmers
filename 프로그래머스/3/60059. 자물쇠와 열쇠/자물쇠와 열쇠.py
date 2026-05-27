def solution(key, lock):
    M = len(key)
    N = len(lock)

    board = [[0] * (3 * N) for _ in range(3 * N)]

    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            board[i][j] = lock[i - N][j - N]

    def check(board):
        for i in range(N, 2 * N):
            for j in range(N, 2 * N):
                if board[i][j] != 1:
                    return False

        return True

    def rotate(key):
        tmp = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                tmp[j][M - i - 1] = key[i][j]

        return tmp

    for _ in range(4):
        for s in range(2*N):
            for e in range(2*N):
                for i in range(M):
                    for j in range(M):
                        board[s + i][e +j] += key[i][j]

                if check(board):
                    return True

                for i in range(M):
                    for j in range(M):
                        board[s + i][e +j] -= key[i][j]

        key = rotate(key)

    return False