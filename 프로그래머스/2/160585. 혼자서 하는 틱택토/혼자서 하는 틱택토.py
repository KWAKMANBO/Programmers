def solution(board):
    answer = -1

    def check(ox):
        for b in board:
            if b == ox * 3:
                return True

        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == ox:
                return True

        if board[0][0] == board[1][1] == board[2][2] == ox:
            return True

        if board[0][2] == board[1][1] == board[2][0] == ox:
            return True

    o = 0
    x = 0

    for b in board:
        o += b.count('O')
        x += b.count('X')

    if x > o:
        return 0

    if o - x > 1:
        return 0

    if check('O') and check('X'):
        return 0

    if check('O') and x == o:
        return 0

    if check('X') and x != o:
        return 0

    return 1