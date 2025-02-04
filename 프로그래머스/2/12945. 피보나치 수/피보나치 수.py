def solution(n):
    f1 = 0
    f2 = 1

    for i in range(2, n + 1):
        tmp = f2
        f2 = f1 + f2
        f1 = tmp

    return f2 % 1234567