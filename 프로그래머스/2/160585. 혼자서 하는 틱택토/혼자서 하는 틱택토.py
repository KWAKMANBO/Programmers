def solution(board):
    answer = -1

    o_cnt = 0
    x_cnt = 0

    def check(ox):
        # 가로 확인
        for b in board:
            if b == ox * 3:
                return True

        # 세로 확인
        for i in range(3):
            tmp = board[0][i] + board[1][i] + board[2][i]
            if tmp == ox * 3:
                return True

        # 대각선 확인
        if board[0][0] + board[1][1] + board[2][2] == ox * 3:
            return True

        if board[0][2] + board[1][1] + board[2][0] == ox * 3:
            return True

        return False

    for b in board:
        o_cnt += b.count('O')
        x_cnt += b.count('X')

    # 1. O는 X와 같거나 X보다 1이 많아야한다 -> O와 X의 차이가 2이상이면 문제
    if o_cnt - x_cnt > 1:
        return 0

    # 2. X는 O와 같거나 작아야 한다. -> X는 O보다 클 수 없음
    if x_cnt > o_cnt:
        return 0

    # 3. O가 완성 되었을때 X의 개수가 같다면 문제
    if check('O') and x_cnt == o_cnt:
        return 0

    # 4. X가 완성 되었을때 O의 개수와 같아야함 -> X가 O보다 더크다면 문제
    if check('X') and x_cnt != o_cnt:
        return 0

    return 1
