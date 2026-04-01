import math


def solution(signals):
    periods = [0] * len(signals)

    MAX_SECOND = 1
    for i in range(len(signals)):
        periods[i] = sum(signals[i])
        MAX_SECOND = (MAX_SECOND * periods[i]) // math.gcd(MAX_SECOND, periods[i])

    yellow_board = []
    for i in range(len(signals)):
        tmp = [0] * periods[i]
        g, y = signals[i][0], signals[i][1]

        for i in range(g, g + y):
            tmp[i] = 1

        yellow_board.append(tmp)

    for t in range(1, MAX_SECOND + 1):

        all_yellow = True
        for i in range(len(signals)):
            idx = (t - 1) % periods[i]
            if yellow_board[i][idx] != 1:
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1
