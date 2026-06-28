def solution(board):
    answer = 0
    N, M = len(board), len(board[0])
    if N == 1:
        return max(board[0])
    else:
        for i in range(1, N):
            for j in range(1, M):
                if board[i][j] == 1:
                    board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                    answer = max(answer, board[i][j])

    return answer ** 2