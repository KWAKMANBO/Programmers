import math


def solution(signals):
    periods = [0] * len(signals)

    def is_yellow(t, g, y, r):
        cycle = g + y + r
        status = (t - 1) % cycle
        return g <= status < g + y

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
        for s in signals:
            if not is_yellow(t, s[0], s[1], s[2]):
                all_yellow = False

        if all_yellow:
            return t

    return -1

