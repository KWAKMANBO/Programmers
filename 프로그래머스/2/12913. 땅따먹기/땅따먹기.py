def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            lst = []
            for k in range(4):
                if j != k:
                    lst.append(land[i][j] + land[i - 1][k])
                else:
                    lst.append(land[i][j])
            land[i][j] = max(lst)
    return max(land[-1])