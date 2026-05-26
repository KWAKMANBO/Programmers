def solution(n):
    # [왼대각선 아래, 오른쪽, 왼대각선 위]
    directions = [(1, 0), (0, 1), (-1, -1)]
    d_idx = 0
    pos = (0, 0)
    pyramid = []
    answer = []
    for i in range(1, n + 1):
        tmp = [0] * i
        pyramid.append(tmp)

    pyramid[0][0] = 1
    i = 2
    cnt = 1
    while cnt < n * (n + 1) // 2:

        ni, nj = pos[0] + directions[d_idx][0], pos[1] + directions[d_idx][1]
        if -1 < ni < n and -1 < nj < len(pyramid[ni]) and pyramid[ni][nj] == 0:
            pyramid[ni][nj] = i
            cnt += 1
            pos = (ni, nj)
            i += 1
        else:
            d_idx += 1
            d_idx %= 3

    for p in pyramid:
        answer.extend(p)
    return answer