def solution(signals):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    L = len(signals)
    LCM = 1

    periods = [0] * L

    # 주기 계산
    for i in range(L):
        periods[i] = sum(signals[i])
        LCM = lcm(LCM, periods[i])

    board = []
    for i in range(L):
        g = signals[i][0]
        y = signals[i][1]

        tmp = [0] * periods[i]

        for j in range(g, g + y):
            tmp[j] = 1
        board.append(tmp)

    for t in range(1, LCM + 1):
        all_yellow = True

        for i in range(L):
            idx = (t - 1) % periods[i]
            if board[i][idx] == 0:
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1


signal_lst = [
    [[2, 1, 2], [5, 1, 1]],
    [[2, 3, 2], [3, 1, 3], [2, 1, 1]],
    [[3, 3, 3], [5, 4, 2], [2, 1, 2]],
    [[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]
]

for s in signal_lst:
    print(solution(s))
