def solution(k, ranges):
    answer = []
    lst = [(0, k)]
    volumes = {}
    n = 0
    while k != 1:
        tmp = k
        n += 1
        if k % 2 == 0:
            k //= 2
            lst.append((n, k))
        elif k % 2 == 1:
            k = k * 3 + 1
            lst.append((n, k))
        volumes[(n-1,n)] = (k + tmp) / 2

    # print(volumes)
    for r in ranges:
        s = r[0]
        e = n + r[1]

        tmp = 0
        if s < e:
            for i in range(s, e):
                tmp += volumes[(i,i+1)]
        elif s == e:
            tmp = 0.0
        else:
            tmp = -1.0
        answer.append(tmp)


    return answer